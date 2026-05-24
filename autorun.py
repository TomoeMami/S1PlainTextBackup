# -*- coding: UTF-8 -*-
"""
S1 论坛帖子监控脚本（优化版）
扫描指定板块首页，记录新帖和回复数变化的帖子，并清理过期的活跃帖缓存。
"""
import json
import re
import time
from pathlib import Path
from typing import Dict, Optional

import requests
from bs4 import BeautifulSoup

# ---------- 常量 ----------
ROOT_DIR = Path("/home/riko/S1PlainTextBackup")
DATA_FILE = ROOT_DIR / "RefreshingData.json"
COOKIE_FILE = Path("/home/riko/s1cookie-1.txt")
# COOKIE_ENV_VAR = "S1_COOKIE"   # 备选方案

BLACKLIST = {
    2104652, 2056385, 1842868, 334540, 1971007,
    1915305, 2023780, 2085181, 2105283, 2045161,
    2106883, 2068300, 2098345, 2120403, 2119905,
    2096884, 2143473, 2100013, 2171889, 2252991
}
HIGH_LEVEL = 10
CACHE_DAYS = 14  # 缓存天数
REPLY_REFRESH_THRESHOLD = 86400  # 1天内有新回复的帖子视为活跃

HEADERS = {
    'User-agent': ('Mozilla/5.0 (Windows NT 6.1; WOW64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/60.0.3112.113 Safari/537.36')
}

FORUM_DICT = {
    '外野': '157',
    '虚拟主播区专楼': '151',
    '游戏区': '4',
    '漫区': '6',
    '手游专楼': '135',
    '手游战斗': '156',
}


# ---------- 工具函数 ----------
def normalize_title(raw_title) -> str:
    """清理标题中的特殊字符，替换为全角符号，并包裹在方括号中。"""
    if not isinstance(raw_title, str):
        raw_title = str(raw_title)
    # 先移除HTML标签
    title = re.sub(r'<[^>]+?>', '', raw_title)
    # 字符替换表
    replacements = {
        '[': '', ']': '',
        '|': '｜', '/': '／', '\\': '＼', ':': '：',
        '*': '＊', '?': '？', '"': '＂', '<': '＜',
        '>': '＞', '...': '…', '\n': ' ',
    }
    for old, new in replacements.items():
        title = title.replace(old, new)
    # 可能还有多个省略号
    title = re.sub(r'\.{3,}', '…', title)
    return f'[{title}]'


def parse_html(html: str, thread_dict: Dict[str, dict]):
    """从列表页 HTML 中提取帖子 ID、标题、回复数和最后回复时间。"""
    soup = BeautifulSoup(html, 'html.parser')
    tbody_list = soup.find_all('tbody')

    for tbody in tbody_list:
        tbody_str = str(tbody)

        # 提取 thread id
        thread_match = re.search(r'normalthread_(\d{7})', tbody_str)
        if not thread_match:
            continue
        thread_id = thread_match.group(1)

        # 提取等级（用于判断是否置顶或高亮，排除 level 1）
        level_match = re.search(r'(\d{1,5})</a></span>', tbody_str)
        if not level_match:
            continue
        level = int(level_match.group(1))
        if level <= 1:
            continue

        # 提取标题和回复数
        title_tag = tbody.find('a', class_='s xst')
        reply_tag = tbody.find('a', class_='xi2')
        if not title_tag or not reply_tag:
            continue

        title = normalize_title(title_tag.text)
        try:
            reply_count = int(reply_tag.text) + 1  # 外部回帖数比实际楼层少1
        except ValueError:
            continue

        # 提取最后回复时间（通常有两个时间，取第二个）
        time_matches = re.findall(r'\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}', tbody_str)
        if len(time_matches) < 2:
            continue
        try:
            reply_time = time.mktime(
                time.strptime(time_matches[1], "%Y-%m-%d %H:%M")
            )
        except (ValueError, OverflowError):
            continue

        # 仅保留1天内有回复的帖子
        now = time.time()
        if (now - reply_time) <= REPLY_REFRESH_THRESHOLD:
            thread_dict[thread_id] = {
                'replytime': int(reply_time),
                'title': title,
                'replycount': reply_count,
            }


def load_cookies(file_path: Path) -> dict:
    """从文件加载 cookie 字符串并解析为字典。"""
    if not file_path.exists():
        raise FileNotFoundError(f"Cookie 文件未找到: {file_path}")

    cookie_str = file_path.read_text(encoding='utf-8').strip()
    # 如果内容包含引号，去除首尾引号（兼容旧逻辑）
    if cookie_str.startswith('"') and cookie_str.endswith('"'):
        cookie_str = cookie_str[1:-1]

    cookies = {}
    for part in cookie_str.split(';'):
        if '=' in part:
            key, value = part.split('=', 1)
            cookies[key.strip()] = value.strip()
    return cookies


def load_existing_data(data_file: Path) -> dict:
    """加载已有的帖子数据文件，若不存在则返回空字典。"""
    if data_file.exists():
        with data_file.open('r', encoding='utf-8-sig') as f:
            return json.load(f)
    return {}


def save_data(data: dict, data_file: Path):
    """保存数据到 JSON 文件（保持 utf-8-sig 编码以兼容旧逻辑）。"""
    data_file.parent.mkdir(parents=True, exist_ok=True)
    with data_file.open('w', encoding='utf-8-sig') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ---------- 主逻辑 ----------
def main():
    # 加载 cookie
    try:
        cookies = load_cookies(COOKIE_FILE)
    except FileNotFoundError:
        print("Cookie 文件不存在，尝试从环境变量加载...")
        cookie_env = os.getenv('S1_COOKIE')
        if not cookie_env:
            raise RuntimeError("无法获取 Cookie，请检查文件或环境变量 S1_COOKIE")
        # 简单处理环境变量（假设已正确提供）
        cookies = {}
        for part in cookie_env.split(';'):
            if '=' in part:
                k, v = part.split('=', 1)
                cookies[k.strip()] = v.strip()

    # 读取已有数据
    thread_data = load_existing_data(DATA_FILE)

    session = requests.Session()
    now = time.time()

    for forum_name, forum_id in FORUM_DICT.items():
        # 确保板块目录存在（原脚本功能保留）
        forum_dir = ROOT_DIR / forum_name
        forum_dir.mkdir(parents=True, exist_ok=True)

        # 抓取第一页
        url = f'https://stage1st.com/2b/forum-{forum_id}-1.html'
        try:
            response = session.get(url, headers=HEADERS, cookies=cookies, timeout=15)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"请求板块 {forum_name} 失败: {e}")
            continue

        # 解析页面，获取当前活跃帖子
        current_posts = {}
        parse_html(response.text, current_posts)

        # 更新已有数据或添加新帖
        for post_id, info in current_posts.items():
            post_id_int = int(post_id)
            if post_id_int in BLACKLIST:
                continue

            if post_id in thread_data:
                old = thread_data[post_id]
                if old['totalreply'] < info['replycount']:
                    print(f"{old['totalreply']} : {info['replycount']}")
                    old['active'] = True
                    old['update'] = True
                    old['lastedit'] = info['replytime']
                # 否则维持原状，不改变 active/update
            else:
                thread_data[post_id] = {
                    'totalreply': 0,
                    'title': info['title'],
                    'newtitle': info['title'],
                    'lastedit': info['replytime'],
                    'category': forum_name,
                    'active': True,
                    'update': True,
                }
                print(f'add:{post_id}')

    # 保存完整的 thread_data（包含所有记录）
    save_data(thread_data, DATA_FILE)

    # 清理：仅保留活跃帖子或高回复数帖子
    active_data = {}
    for post_id, info in thread_data.items():
        try:
            last_edit = int(info.get('lastedit', 0))
            total_reply = int(info.get('totalreply', 0))
        except (ValueError, TypeError):
            continue

        is_active = info.get('active', False)
        is_recent = (now - last_edit) < (CACHE_DAYS * 86400)
        is_high_reply = (total_reply // 40) > HIGH_LEVEL

        if is_active or is_recent or is_high_reply:
            active_data[post_id] = info

    # 最终保存清洗后的数据
    save_data(active_data, DATA_FILE)


if __name__ == '__main__':
    # 设置标准输出编码（Python 3.10 通常不需要，但保留以防止 Windows 下问题）
    import sys
    sys.stdout.reconfigure(encoding='utf-8') if hasattr(sys.stdout, 'reconfigure') else None
    main()
