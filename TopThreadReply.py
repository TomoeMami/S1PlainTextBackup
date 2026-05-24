# -*- coding: UTF-8 -*-
import re
import json
import time
from pathlib import Path
from datetime import datetime, timedelta, timezone
from collections import Counter

import requests

# 配置常量
ROOT_PATH = "./"
FORUM_URL = "https://stage1st.com/2b/forum.php"
VIEW_THREAD_URL = f"{FORUM_URL}?mod=viewthread&tid=2252916&extra=page%3D1"
REPLY_URL_TEMPLATE = f"{FORUM_URL}?mod=post&action=reply&fid=157&tid={{tid}}&extra=page%3D1&replysubmit=yes"
TARGET_THREAD_ID = 2252991
HEADERS = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78"
}
REQUEST_TIMEOUT = 10  # 秒


def get_date(offset_days: int, format_type: int = 1) -> str:
    """获取北京时间指定偏移天数的日期字符串。
    
    Args:
        offset_days: 天数偏移，正数表示几天前，负数表示几天后。
        format_type: 1 -> "YYYY-M-D", 2 -> "YYYY年M月D日"
    """
    tz_utc8 = timezone(timedelta(hours=8))
    target_date = datetime.now(tz_utc8) - timedelta(days=offset_days)
    if format_type == 2:
        return f"{target_date.year}年{target_date.month}月{target_date.day}日"
    return f"{target_date.year}-{target_date.month}-{target_date.day}"


def extract_reply(text: str) -> list[str]:
    """提取回帖的纯文本行，去除引用块、小尾巴、HTML标签、日期行和####开头的行。"""
    # 移除被引用的 blockquote 内容
    cleaned = re.sub(r"<blockquote>.*?发表于.*?</blockquote>", "", text, flags=re.DOTALL)
    # 移除客户端小尾巴（多种格式）
    tail_pattern = re.compile(
        r"—— [来來]自.+[鹅鵝].+\d+[\.\d]+(-alpha)?|"
        r"— from \[S1 Next Goose\]\(https://[^\)]+\) v\d+\.\d+\.\d+(-alpha)?|"
        r"https://s1fun\.koalcat\.com",
        re.DOTALL
    )
    cleaned = tail_pattern.sub("", cleaned)

    # 提取<blockquote>之后的部分（若存在），否则取整个文本
    if "<blockquote>" in cleaned:
        match = re.search(r"<blockquote>.*?</blockquote>(.*?)$", cleaned, re.DOTALL)
        reply_content = match.group(1).strip() if match else cleaned.strip()
    else:
        reply_content = cleaned.strip()

    # 去除所有HTML标签
    reply_content = re.sub(r"<[^>]+>", "", reply_content)
    # 去除日期行（如 2025-5-24）
    reply_content = re.sub(r"\d{4}-\d{1,2}-\d{1,2}", "", reply_content)

    # 过滤掉以 #### 开头的行
    lines = [line for line in reply_content.splitlines() if not line.startswith("####")]
    return lines


def build_reply_content(today: str, today_cn: str, board_names: list[str]) -> str:
    """根据当天数据生成完整的回帖内容（Markdown/BBcode）。"""
    reply_str = f"[b]统计日期：[/b]{today_cn}\n[url=https://github.com/TomoeMami/S1PlainTextBackup/]数据来源[/url]\n\n"
    
    with open(Path(ROOT_PATH) / "RefreshingData.json", "r", encoding="utf-8-sig") as f:
        post_data = json.load(f)

    for board in board_names:
        board_dict = {}
        board_path = Path(ROOT_PATH) / board
        for md_file in board_path.rglob("*.md"):
            with open(md_file, "r", encoding="utf-8-sig") as f:
                content = f.read()
            # 提取非空行组成的文本
            non_empty_lines = [line for line in content.splitlines() if line.strip()]
            text = "\n".join(non_empty_lines)

            if today not in text:
                continue

            # 按分隔符切分帖子
            posts = text.split("*****")
            res = []
            for post in posts:
                if today not in post:
                    continue
                # 提取发帖时间
                time_match = re.search(r"发表于\s(\d{4}-\d{1,2}-\d{1,2}) \d{2}:\d{2}", post)
                if time_match and time_match.group(1) == today:
                    res.append(today)

            if not res:
                continue

            # 从文件名中提取 thread id（连续5-9位数字）
            thread_id_match = re.search(r"\d{5,9}", md_file.name)
            if not thread_id_match:
                continue
            thread_id = thread_id_match.group(0)
            count = Counter(res).get(today, 0)
            board_dict[thread_id] = board_dict.get(thread_id, 0) + count

        total = sum(board_dict.values())
        reply_str += f"[b]{board}（+{total}）[/b]\n"
        sorted_threads = sorted(board_dict.items(), key=lambda x: x[1], reverse=True)
        top_n = min(len(sorted_threads), 20)
        for i, (tid, cnt) in enumerate(sorted_threads[:top_n], start=1):
            title = post_data.get(tid, {}).get("title", "未知标题")
            reply_str += f"{i}. [url=https://stage1st.com/2b/thread-{tid}-1-1.html]{title}[/url]（[b]+{cnt}[/b]）\n"
        reply_str += "===========\n\n"
    return reply_str


def get_formhash(session: requests.Session) -> str:
    """从指定帖子获取 formhash。"""
    resp = session.get(VIEW_THREAD_URL, headers=HEADERS, timeout=REQUEST_TIMEOUT)
    content = resp.text  # 使用文本而非 bytes
    match = re.search(r'<input type="hidden" name="formhash" value="([^"]+)"', content)
    if not match:
        raise RuntimeError("无法获取 formhash，请检查页面结构或登录状态")
    return match.group(1)


def post_reply(session: requests.Session, formhash: str, message: str):
    """使用 formhash 和 session 回帖。"""
    url = REPLY_URL_TEMPLATE.format(tid=TARGET_THREAD_ID)
    data = {
        "formhash": formhash,
        "message": message,
        "subject": "",
        "posttime": int(time.time()),
        "wysiwyg": 1,
        "usesig": 1,
    }
    resp = session.post(url, data=data, headers=HEADERS, timeout=REQUEST_TIMEOUT)
    print(f"回帖状态码: {resp.status_code}")
    return resp


def main():
    board_names = ["外野", "游戏区", "漫区", "手游战斗"]
    today = get_date(1)           # "2026-5-24" 格式
    today_cn = get_date(1, 2)     # "2026年5月24日" 格式

    reply_content = build_reply_content(today, today_cn, board_names)
    print(reply_content)
    # 从环境变量加载 Cookie
    cookie_str = os.environ.get("S1_COOKIE", "")
    if not cookie_str:
        raise RuntimeError("环境变量 S1_COOKIE 未设置，请检查 GitHub Secrets 配置。")
    cookies = {}
    for item in cookie_str.split(";"):
        if "=" in item:
            key, value = item.split("=", 1)
            cookies[key.strip()] = value.strip()

    # 创建带 Cookie 的会话
    session = requests.Session()
    session.cookies.update(cookies)

    # 获取 formhash 并回帖
    formhash = get_formhash(session)
    print(f"formhash: {formhash}")
    post_reply(session, formhash, reply_content)


if __name__ == "__main__":
    import os
    main()
