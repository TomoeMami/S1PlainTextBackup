# -*- coding: UTF-8 -*-

rootdir="./"

import re
import json
from pathlib import Path
import datetime
import requests,os,time




def getdate(beforeOfDay):
        today = datetime.datetime.today()
        # 计算偏移量
        offset = datetime.timedelta(days=-beforeOfDay)
        # 获取想要的日期的时间
        re_date = (today + offset).strftime('%Y-%-m-%-d')
        return re_date

if __name__ == '__main__':
    p = Path(rootdir)
    # replydict = {
    #     '外野':{},
    #     '漫区':{},
    #     '游戏区':{},
    #     '手游区':{},
    #     '管人区':{},
    # }
    replydict = {
        '外野':{},
        '游戏区':{},
        '漫区':{}
    }
    for file in p.rglob('*.md'):
        if(('虚拟主播区专楼' not in str(file) ) and ('手游专楼' not in str(file))):
            print(str(file))
            with open (file, 'r',encoding='UTF-8') as f:
                lines = f.readlines()
                a = ''
                for line in lines:
                    a += line.strip()
                    # a += line
                b = a.split("*****")
                res = []
                for post in b:
                    post1 = post
                    post2 = post
                    data={}
                    data['id'] = ''.join(re.findall(r"^[\*]{0,2}####\s\s([^#]+)#", post))
                    # data['level'] = str(filepath)+''.join(re.findall(r"#####\s(\d+)#", post1))
                    data['time'] = ''.join(re.findall(r"^.*?发表于\s(\d{4}-\d{1,2}-\d{1,2}) \d{2}:\d{2}", post2))
                    if(data['id']):
                        res.append(data)
                threadid = re.findall(r"\d{5,9}", str(file))[0]
                temptimedict = {}
                for i in res:
                    if i['time'] in temptimedict.keys():
                        temptimedict[i['time']]['num'] = temptimedict[i['time']]['num'] + 1
                    else:
                        temptimedict[i['time']] = {}
                        temptimedict[i['time']]['num'] = 1
                    if i['id'] in temptimedict[i['time']].keys():
                        temptimedict[i['time']][i['id']] = temptimedict[i['time']][i['id']] + 1
                    else:
                        temptimedict[i['time']][i['id']] = 1
                today = str(getdate(1))
                if('外野' in str(file)):
                    board = '外野'
                elif('漫区' in str(file)):
                    board = '漫区'
                elif('游戏区' in str(file)):
                    board = '游戏区'
                # elif('手游' in str(file)):
                #     board = '手游区'
                # elif('虚拟主播区' in str(file)):
                #     board = '管人区'
                if today in temptimedict.keys():
                    if today not in replydict[board].keys():
                        replydict[board][today] = {}
                    for k in temptimedict[today].keys():
                        if k not in replydict[board][today].keys():
                            replydict[board][today][k] = {}
                            replydict[board][today][k]['num'] = 0
                        if threadid not in replydict[board][today][k].keys():
                            replydict[board][today][k][threadid] = 0
                        replydict[board][today][k]['num'] = replydict[board][today][k]['num'] + temptimedict[today][k]
                        replydict[board][today][k][threadid] = replydict[board][today][k][threadid] + temptimedict[today][k]


    rstr = '[b]统计日期：[/b]'
    rstr = rstr + (datetime.datetime.today()+datetime.timedelta(days=-1)).strftime('%Y年%-m月%-d日')+'\n[url=https://github.com/TomoeMami/S1PlainTextBackup/]数据来源[/url]\n\n'
    for k in replydict.keys():
        rstr = rstr + '[b]' + k + '（+'+str(replydict[k][today]['num']['num'])+'）[/b]\n'
        thdict = replydict[k][today]['num']
        thdict.pop('num')
        threadorder=sorted(thdict.items(),key=lambda x:x[1],reverse=True)
        threadnum = min(len(threadorder),20)
        rstr = rstr + '[b]回帖数量前'+str(threadnum)+'的帖子：[/b]\n'
        namedict = {}
        replydict1 = replydict
        replydict1[k][today].pop('num')
        for i in replydict1[k][today].keys():
            namedict[i] = replydict1[k][today][i]['num']
        # namedict.pop('num')
        nameorder = sorted(namedict.items(),key=lambda x:x[1],reverse=True)
        with open(rootdir+'RefreshingData.json',"r",encoding='utf-8') as f:
            thdata=json.load(f)
        for i in range(threadnum):
            rstr = rstr +str(i+1)+'. [url=https://bbs.saraba1st.com/2b/thread-'+threadorder[i][0]+'-1-1.html]'+thdata[threadorder[i][0]]['title'] +'[/url]（[b]+'+str(threadorder[i][1])+'[/b]）\n'
        # rstr = rstr + '\n' + '[b]回帖数量前'+str(threadnum)+'的用户：[/b]\n'
        # for i in range(threadnum):
        #     nameth = replydict1[k][today][nameorder[i][0]]
        #     nameth.pop('num')
        #     norder = sorted(nameth.items(),key=lambda x:x[1],reverse=True)
        #     rstr = rstr +str(i+1)+'. '+str(nameorder[i][0][0])+'****'+str(nameorder[i][0][-1])+'（[b]+'+str(nameorder[i][1]) +'[/b]）：'+'[url=https://bbs.saraba1st.com/2b/thread-'+norder[0][0]+'-1-1.html]'+thdata[norder[0][0]]['title'] +'[/url]（[b]+'+str(norder[0][1])+'[/b]）\n'
        rstr = rstr + '===========\n\n'
    rstr = rstr + '[url=https://tomoemami.gitee.io/tomoemami.github.io/]历史日回帖统计在线图表[/url]\n'
    # print(rstr)
    with open ('/home/ubuntu/s1cookie-1.txt','r',encoding='utf-8') as f:
        cookie_str1 = f.read()
    cookie_str = repr(cookie_str1)[1:-1]
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value
    headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}
    ''' 获取formhash'''
    RURL = 'https://bbs.saraba1st.com/2b/forum.php?mod=viewthread&tid=334540&extra=page%3D1'
    s1 = requests.get(RURL, headers=headers,  cookies=cookies)
    content = s1.content
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
            threadid = 2023780
            '''回帖ID，手动修改'''
            replyurl = 'https://bbs.saraba1st.com/2b/forum.php?mod=post&action=reply&fid=151&tid='+str(threadid)+'&extra=page%3D1&replysubmit=yes'
            #url为要回帖的地址
            Data = {'formhash': formhash,'message': rstr,'subject': subject,'posttime':int(time.time()),'wysiwyg':1,'usesig':1}
            req = requests.post(replyurl,data=Data,headers=headers,cookies=cookies)
            print(req)
            break
        else:
            print('none formhash!')
            continue
