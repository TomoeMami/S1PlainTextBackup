# -*- coding: UTF-8 -*-

import re
import json
from pathlib import Path
from datetime import datetime,timedelta
import requests,os,time,sys
from collections import Counter
import signal
# from cutword import Cutter
# from snownlp import SnowNLP
# import jieba
# import hanlp

def getdate(beforeOfDay):
        system_type = sys.platform
        today = datetime.today()
        # 计算偏移量
        offset = timedelta(days=-beforeOfDay)
        # 获取想要的日期的时间
        if system_type == "win32":
            re_date = (today + offset).strftime("%Y-%#m-%#d")
        else:
            re_date = (today + offset).strftime("%Y-%-m-%-d")
        return re_date

def getdate2(beforeOfDay):
        system_type = sys.platform
        today = datetime.today()
        # 计算偏移量
        offset = timedelta(days=-beforeOfDay)
        # 获取想要的日期的时间
        if system_type == "win32":
            re_date = (today + offset).strftime("%Y年%#m月%#d日")
        else:
            re_date = (today + offset).strftime("%Y年%-m月%-d日")
        return re_date

def 提取回帖(text):
    # 正则表达式匹配 <blockquote> 中的引用内容
    blockquote_pattern = re.compile(r"<blockquote>.*?发表于.*?</blockquote>", re.DOTALL)

    # 删除 <blockquote> 中的引用内容（如果存在）
    cleaned_text = blockquote_pattern.sub("", text)
    tail_pattern = re.compile(
    r"—— [来來]自.+[鹅鵝].+\d+[\.\d]+(-alpha)?|"
    r"— from \[S1 Next Goose\]\(https://[^\)]+\) v\d+\.\d+\.\d+(-alpha)?|" # 英文小尾巴（无 alpha）
    r"https://s1fun\.koalcat\.com",  
    re.DOTALL
    )
    cleaned_text = tail_pattern.sub("", cleaned_text)   
    # 提取回帖内容
    # 如果存在 <blockquote>，则提取其后的内容；否则，提取整个内容
    if "<blockquote>" in cleaned_text:
        # 提取 <blockquote> 之后的内容
        reply_pattern = re.compile(r"<blockquote>.*?</blockquote>(.*?)$", re.DOTALL)
        reply_match = reply_pattern.search(cleaned_text)
        if reply_match:
            reply_content = reply_match.group(1).strip()
        else:
            reply_content = cleaned_text.strip()
    else:
        # 如果没有 <blockquote>，直接提取整个内容
        reply_content = cleaned_text.strip()
    reply_content = re.sub(r"<.*?>", "", reply_content)
    reply_content = re.sub(r"\d{4}-\d{1,2}-\d{1,2}", "",reply_content)
    # 过滤掉以 #### 开头的行
    filtered_lines = [line for line in reply_content.splitlines() if not line.startswith("####")]

    # # 将过滤后的行重新组合成字符串
    # final_reply_content = "\n".join(filtered_lines).strip()
    # final_reply_content = re.sub(r"\s+", "", final_reply_content)
    # final_reply_content = re.sub(r"<.*?>", "", final_reply_content)
    return filtered_lines

def timeout_handler(signum, frame):
    raise TimeoutError("Function execution has timed out.")

if __name__ == '__main__':
    根路径="./"

    回复字典 = {
        '外野':{},
        '游戏区':{},
        '漫区':{},
        '手游战斗':{}
    }
    回帖字符串 = '[b]统计日期：[/b]'
    今日日期 = str(getdate(1))
    # 停用词表 = set(['Android','iPhone','不能','开始','最后','自己','---','次数','一个','不是','2025','来自','就是','这个','没有','还是','什么','可以','这种','因为','但是','所以','也不','知道','觉得','怎么','可能','还有','如果','然后','确实','直接','时候','出来','不会','而且','应该','已经','很多','其实','不过','那么','这么','这样','只是','需要','只有','那个','的话','当然','几个','完全','或者','一样','地方','比较','虽然','其他','感觉','一直','有点','楼主','时间','一下','还能','主要','一点','只能','以后','一般','代表','多少','结果','东西','根本','肯定','人家','现在','本来','甚至','为了','所谓','说法','认为','有人','评分','里面','本身','毕竟','那些','非常','战斗力','各种','不如','情况','起来','来说','基本','没啥','一种','看到','://','com','https','](','www','——','pgyer','v3.3','96','GcUxKd4w','xfPejhuq','alpha','……','下载次数','下载','附件','上传','KB','jpg','10','+ 1','编辑','status','真的','="','image','png','saraba1st','S1Fun','S1Fun','s1fun','koalcat','|+'])
    回帖字符串 = f"{回帖字符串}{getdate2(1)}\n[url=https://github.com/TomoeMami/S1PlainTextBackup/]数据来源[/url]\n\n"
    # cutter = Cutter(want_long_word=True)
    # tok = hanlp.load(hanlp.pretrained.tok.FINE_ELECTRA_SMALL_ZH)
    for 板块 in 回复字典.keys():
        板块字典 = {}
        # 词云数据 = []
        p = Path(f"{根路径}{板块}/")
        for file in p.rglob('*.md'):
            print(str(file))
            with open (file, 'r',encoding='utf-8-sig') as f:
                content = f.read()
                lines = content.splitlines()
                a = "\n".join(line for line in lines if line.strip())
                if 今日日期 in a:
                    b = a.split("*****")
                    res = []
                    for post in b:
                        if 今日日期 in post:
                            # print(post)
                            post1 = post
                            post2 = post
                            data={}
                            data['id'] = re.search(r"####[^#]{2}(.+)\n#####", post).group(1)
                            # data['level'] = str(filepath)+''.join(re.findall(r"#####\s(\d+)#", post1))
                            data['time'] = re.search(r"发表于\s(\d{4}-\d{1,2}-\d{1,2}) \d{2}:\d{2}", post2).group(1)
                            if data['id'] and data['time'] == 今日日期:
                                res.append(data['time'])
                                # if 板块 != "手游战斗":
                                #     for 分词结果 in tok(提取回帖(post1)):
                                #         if 分词结果 :
                                #             for 分词 in 分词结果:
                                #                 if len(分词) >1 and 分词 not in 停用词表:
                                #                     词云数据.append(分词)
                    threadid = re.findall(r"\d{5,9}", str(file))[0]
                    if Counter(res).get(今日日期, 0) > 0:
                        if threadid in 板块字典.keys():
                            板块字典[threadid] = 板块字典[threadid] + Counter(res).get(今日日期, 0)
                        else:
                            板块字典[threadid] = Counter(res).get(今日日期, 0)
        # 词云排序 = sorted(Counter(词云数据).items(),key=lambda x:x[1],reverse=True)
        回帖字符串 = f"{回帖字符串}[b]{板块}（+{sum(板块字典.values())}）[/b]\n"
        回帖排序 = sorted(板块字典.items(),key=lambda x:x[1],reverse=True)
        回帖序号 = min(len(回帖排序),20)
        with open(根路径+'RefreshingData.json',"r",encoding='utf-8-sig') as f:
            帖子数据=json.load(f)
        for i in range(回帖序号):
            回帖字符串 = f"{回帖字符串}{i+1}. [url=https://stage1st.com/2b/thread-{回帖排序[i][0]}-1-1.html]{帖子数据[回帖排序[i][0]]['title']}[/url]（[b]+{回帖排序[i][1]}[/b]）\n"
        if 板块 != "手游战斗":
            # 回帖字符串 = f"""{回帖字符串}[b]前10高频词汇[/b]：\n{"，".join([f"{word:<10}{count:>5}" for word, count in 词云排序[:5]])}\n{"，".join([f"{word:<10}{count:>5}" for word, count in 词云排序[5:10]])}\n"""
            回帖字符串 = f"{回帖字符串}===========\n\n"
    # print(回帖字符串)
    with open ('/home/riko/s1cookie-1.txt','r',encoding='utf-8') as f:
        cookie_str1 = f.read()
    cookie_str = repr(cookie_str1)[1:-1]
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value
    headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}
    ''' 获取formhash'''
    RURL = 'https://stage1st.com/2b/forum.php?mod=viewthread&tid=2252916&extra=page%3D1'
    s1 = requests.get(RURL, headers=headers,  cookies=cookies)
    content = s1.content
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(60)  # 设置超时时间为60秒
    try:
        while True:
            rows = re.findall(r'<input type=\"hidden\" name=\"formhash\" value=\"(.*?)\" />', str(content)) #正则匹配找到formhash值
            if len(rows)!=0:
                formhash = rows[0]
                print('formhash is: ' + formhash)
                subject = u''
                # Aurl = 'https://raw.fastgit.org/TomoeMami/S1PlainTextBackup/master/A-Thread-id.txt'
                # s = requests.get(Aurl)
                # threadid = s.content.decode('utf-8')
                '''回帖ID，手动修改'''
                threadid = 2252991
                '''回帖ID，手动修改'''
                replyurl = 'https://stage1st.com/2b/forum.php?mod=post&action=reply&fid=157&tid='+str(threadid)+'&extra=page%3D1&replysubmit=yes'
                #url为要回帖的地址
                Data = {'formhash': formhash,'message': 回帖字符串,'subject': subject,'posttime':int(time.time()),'wysiwyg':1,'usesig':1}
                req = requests.post(replyurl,data=Data,headers=headers,cookies=cookies)
                print(req)
                break
            else:
                print('none formhash!')
                continue
    except TimeoutError:
        print("Function execution has timed out.")
