#!/usr/bin/env python3

import asyncio
import json
import math
import re
import shutil
import time
from pathlib import Path
from typing import Any, Dict, Tuple, List

import aiohttp
from bs4 import BeautifulSoup

# 常量配置
HEADERS = {
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}
ROOT_DIR = Path("/home/riko/S1PlainTextBackup")
ARCHIVE_NAME = f"S1PlainTextArchive{time.strftime('%Y')}"
ARCHIVE_DIR = Path(f"/home/riko/{ARCHIVE_NAME}")


def sanitize_title(title_str: str) -> str:
    """过滤文件名中的非法字符"""
    replacements = {
        '[': '', ']': '', '|': '｜', '/': '／', '\\': '＼',
        ':': '：', '*': '＊', '?': '？', '"': '＂', '<': '＜',
        '>': '＞', '\n': ' ', '...': '…'
    }
    for old, new in replacements.items():
        title_str = title_str.replace(old, new)
    return f"[{title_str.strip()}]"


def parse_html(html: str) -> Tuple[List, List, int, str]:
    soup = BeautifulSoup(html, 'html.parser')
    namelist = soup.find_all(name="div", attrs={"class": "pi"})
    replylist = soup.find_all(name='div', attrs={"class": "pcb"})
    title_node = soup.find(name='span', attrs={"id": "thread_subject"})
    
    # 提取总页数
    total_page = 1
    span_page = soup.find('span', title=re.compile(r'共 \d+ 页'))
    if span_page:
        match = re.search(r'共 (\d+) 页', span_page.get('title', ''))
        if match:
            total_page = int(match.group(1))

    # 提取并清理标题
    raw_title = title_node.get_text() if title_node else ""
    titles = sanitize_title(raw_title)
    
    return namelist, replylist, total_page, titles


def thread_dict(thpath: Path, thdict: dict):
    if not thpath.exists():
        return
    content = thpath.read_text(encoding='utf-8-sig')
    parts = content.split("*****")
    for part in parts[1:]:
        match = re.search(r'\n#####\s(\d+)#', part)
        if match:
            thdict[match.group(1)] = part


def thread_merge(oripath: Path, despath: Path):
    ori: Dict[str, str] = {}
    des: Dict[str, str] = {}
    thread_dict(oripath, ori)
    if despath.exists():
        thread_dict(despath, des)
        
    new_keys = sorted(list(set(ori.keys()) - set(des.keys())))
    result = "".join(f"*****{ori[k]}" for k in new_keys)
    
    if result:
        with open(despath, 'a', encoding='utf-8-sig') as f:
            f.write(result)
            
    if oripath.exists():
        oripath.unlink()


def FormatStr(namelist: list, replylist: list, totalreply: int) -> Tuple[str, int]:
    nametime = []
    for i in namelist:
        text = re.sub(r'[\r\n]', ' ', i.get_text())
        nametime.append(text)
        
    names = nametime[::2]
    timestamp = nametime[1::2]
    
    times = []
    replynumber = []
    for i in timestamp:
        i = re.sub(r'[\r\n]', ' ', i).replace('电梯直达', '1#')
        j = re.search(r'\d+[\S\s]+发表于\s\d+-\d+-\d+\s\d+:\d+', i)
        k = re.search(r'\d+', i)
        if j and k:
            times.append(j.group(0))
            replynumber.append(int(k.group(0)))
        else:
            times.append("未知时间")
            replynumber.append(0)

    replys = []
    for item in replylist:
        i = str(item).replace('\r', '\n')
        i = i.replace('<blockquote>', '[[[[blockquote]]]]')
        i = i.replace('</blockquote>', '[[[[/blockquote]]]]')
        i = i.replace('<strong>', '[[[[strong]]]]')
        i = i.replace('</strong>', '[[[[/strong]]]]')
        i = i.replace('<span class="icon_ring vm">', '﹍﹍﹍\n\n')
        i = i.replace('<td class="x.1">', '|')
        i = i.replace('\n</td>', '').replace('</td>\n', '')
        
        i = re.sub(r'<div class="modact">(.+?)</div>', r'\n\n *\1* \n\n', i)
        i = re.sub(r'<a href="http(.+?)" target="_blank">(.+?)</a>', r'[\2](http\1)', i)
        i = re.sub(r'<img alt=".*?" border="\d+?" smilieid="\d+?" src="', '[[[[img src="', i)
        i = i.replace('"/>', '"/)')
        i = re.sub(r'<img .*?file="', '[[[[img src="', i)
        
        # 批量处理常见格式后缀
        for ext in ['jpg', 'png', 'gif', 'jpeg', 'webp', 'tif']:
            i = re.sub(rf'{ext}".+\)', f'{ext}" referrerpolicy="no-referrer"]]]]', i)
            
        i = re.sub(r'<.+?>', '', i)
        i = re.sub(r'\n(.*?)\|(.*?)\|(.*?)\n', r'\n|\1|\2|\3|\n', i)
        i = i.replace('收起\n理由', '|昵称|战斗力|理由|\n|----|---|---|')
        i = re.sub(r'\|\n+?\|', '|\n|', i)
        i = i.replace('[[[[', '<').replace(']]]]', '>')
        i = re.sub(r'\[(.+?发表于.+?\d)\]\((http.+?)\)', r'<a href="http\2" target="_blank">\1</a>', i)
        replys.append(i)
        
    output = ''
    limit_len = min(len(replylist), len(names), len(times), len(replynumber))
    for i in range(limit_len):
        if totalreply < replynumber[i]:
            output += f'\n*****\n\n#### {names[i]}\n##### {times[i]}\n{replys[i]}\n'
            
    output = output.replace('\r', '\n')
    output = re.sub(r'\n{2,}', '\n\n', output)
    lastreply = replynumber[-1] if replynumber else totalreply
    return output, lastreply


# 解析 Cookie
def load_cookies() -> dict:
    cookie_path = Path('/home/riko/s1cookie-1.txt')
    if not cookie_path.exists():
        return {}
    cookie_str = cookie_path.read_text(encoding='utf-8').strip()
    cookies = {}
    for line in cookie_str.split(';'):
        line = line.strip()
        if '=' in line:
            key, value = line.split('=', 1)
            cookies[key] = value
    return cookies


cookies = load_cookies()

# 初始化基础归档目录
for category in ["外野", "手游专楼", "手游战斗", "游戏区", "漫区", "虚拟主播区专楼"]:
    (ARCHIVE_DIR / category).mkdir(parents=True, exist_ok=True)

# 加载待刷新的JSON数据
thdata_path = ROOT_DIR / 'RefreshingData.json'
with open(thdata_path, "r", encoding='utf-8-sig') as f:
    thdata = json.load(f)


async def UpdateThread(threaddict: dict, semaphore: asyncio.Semaphore, session: aiohttp.ClientSession):
    tid = threaddict['id']
    try:
        if not threaddict['update']:
            # 超过 3 天未编辑则进行归档整理
            if (int(time.time()) - thdata[tid]['lastedit']) > 259200:
                titles = threaddict['title']
                category = thdata[tid]['category']
                if thdata[tid]['totalreply'] > 37 * 40:
                    filedir_src = ROOT_DIR / category / f"{tid}{titles}"
                else:
                    filedir_src = ROOT_DIR / category / f"{tid}-01{titles}.md"
                
                filename_des = Path(str(filedir_src).replace('S1PlainTextBackup', ARCHIVE_NAME))
                if filedir_src.exists():
                    if filename_des.exists():
                        if filedir_src.is_dir():
                            for i in filedir_src.iterdir():
                                j = Path(str(i).replace('S1PlainTextBackup', ARCHIVE_NAME))
                                thread_merge(i, j)
                        else:
                            thread_merge(filedir_src, filename_des)
                    else:
                        filedir_des = ARCHIVE_DIR / category
                        filedir_des.mkdir(parents=True, exist_ok=True)
                        shutil.move(str(filedir_src), str(filedir_des))
                thdata[tid]['active'] = False
        else:
            thdata[tid]['update'] = False
            lastpage = threaddict['totalreply'] // 40
            url = f'https://stage1st.com/2b/thread-{tid}-1-1.html'
            
            async with semaphore:
                async with session.get(url, headers=HEADERS) as response:
                    # 使用 text() 并指定 errors='replace'，防止 BS4 抛出编码警告提示
                    result = await response.text(encoding='utf-8', errors='replace')
                    
            namelist, replylist, totalpage, newtitles = parse_html(result)
            titles = threaddict['title']
            thdata[tid]['newtitle'] = newtitles
            
            if totalpage > 37:
                filedir = ROOT_DIR / thdata[tid]['category'] / f"{tid}{titles}"
                filedir.mkdir(parents=True, exist_ok=True)
            else:
                filedir = ROOT_DIR / thdata[tid]['category']
            
            contentdict = {}
            # 抓取后续页码
            for thread in range(lastpage + 1, totalpage + 1):
                rurl = f'https://stage1st.com/2b/thread-{tid}-{thread}-1.html'
                async with semaphore:
                    async with session.get(rurl, headers=HEADERS) as response:
                        # 同样进行安全的 UTF-8 文本解码
                        rdata = await response.text(encoding='utf-8', errors='replace')
                rnamelist, rreplylist, _, _ = parse_html(rdata)
                ThreadContent, lastreply = FormatStr(rnamelist, rreplylist, threaddict['totalreply'])
                contentdict[str(lastreply)] = {
                    'content': ThreadContent,
                    'page': thread
                }
            
            if contentdict:
                valid_keys = list(map(int, contentdict.keys()))
                if min(valid_keys) > threaddict['totalreply']:
                    print(f"{tid}-{list(contentdict.keys())}")
                    for replynum in sorted(valid_keys):
                        page_num = contentdict[str(replynum)]['page']
                        pages = f"{math.ceil(page_num / 37):02d}"
                        filename = f"{tid}-{pages}{titles}.md"
                        filepath = filedir / filename
                        
                        with open(filepath, 'a', encoding='utf-8-sig') as f:
                            f.write(contentdict[str(replynum)]['content'])
                            
                    thdata[tid]['totalreply'] = max(valid_keys)
                    thdata[tid]['lastedit'] = int(time.time())
                    thdata[tid]['title'] = titles
                    
    except Exception as e:
        print(f"处理帖子 ID {tid} 时发生异常: {e}")


async def main():
    semaphore = asyncio.Semaphore(12)
    threaddicts = {}
    for tid, info in thdata.items():
        if info.get('active'):
            threaddicts[tid] = {
                'id': tid,
                'totalreply': int(info['totalreply']),
                'title': info['title'],
                'update': info['update']
            }
            
    # 共用单个 ClientSession
    async with aiohttp.ClientSession(cookies=cookies) as session:
        tasks = [UpdateThread(threaddicts[tid], semaphore, session) for tid in threaddicts]
        await asyncio.gather(*tasks)
        
    # 所有协程执行完毕后，统一一次性将更新写回磁盘
    with open(thdata_path, "w", encoding='utf-8-sig') as f:
        json.dump(thdata, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    asyncio.run(main())

    # 归档后处理：将散落的 -01 存档合并至归档文件夹内
    for dir_prefix in ["外野/", "手游专楼/", "游戏区/", "漫区/", "虚拟主播区专楼/", "手游战斗/"]:
        subdir = ROOT_DIR / dir_prefix
        if not subdir.exists():
            continue
        for item in subdir.iterdir():
            if not item.is_dir():
                continue
            name_list = item.name.split("[")
            if len(name_list) < 2:
                continue
                
            old_path = subdir / f"{name_list[0]}-01[{name_list[1]}.md"
            if old_path.exists():
                print(f"正在合并：{old_path}")
                new_path = item / f"{name_list[0]}-01[{name_list[1]}.md"
                if new_path.exists():
                    # 合并内容
                    new_content = new_path.read_text(encoding='utf-8-sig')
                    with open(old_path, "a", encoding='utf-8-sig') as o:
                        o.write(new_content)
                # 覆盖原文件或移动至内部
                old_path.replace(new_path)
