# -*- coding: UTF-8 -*-
#!/usr/bin/env/ python3
import re
import sys
import io
import os
import json
import math
#sys.excepthook = lambda *args: exit(1)
# def remov(path):
#     path=path.encode('utf-8')
#     if(os.path.exists(path)):
#         os.remove(path)

if __name__ == '__main__':

    rootdir="/home/riko/S1PlainTextBackup/"
    with open(rootdir+'RefreshingData.json',"r",encoding='utf-8') as f:
        thdata=json.load(f)
    for i in range(len(thdata)):
        if(thdata[i]['active']):
            ThreadID = thdata[i]['id']
            totalreply = int(thdata[i]['totalreply'])

            titles = thdata[i]['title']
            #if(lastreply%30):
            #    lastpage = totalreply//30+1
            #else:
            #    lastpage = totalreply//30
            replys = []
            lastpage = int(thdata[i]['totalpage']) #无论是否是第30*n层，都应该把整除30当成上次的页数
            if(lastpage > 50):
                filedir = rootdir+thdata[i]['category']+'/'+str(ThreadID)+titles+'/'
            else:
                filedir = rootdir+thdata[i]['category']+'/'
                #为了确保刚好有50页时能及时重新下载而不是直接跳至51页开始
                #startpage = (lastpage-1)//50*50+1
            pages = '%02d' %math.ceil(lastpage/50)
            filename = str(ThreadID)+'-'+str(pages)+titles+'.md'
            with open((filedir+filename).encode('utf-8'),'r',encoding='utf-8') as f:
                findword = r'\d+#'
                pattern = re.compile(findword)
                results = re.findall(pattern,f.read())
                for result in results:
                #print result
                    replys.append(result)
                k = re.search(r'\d+',str(replys[-1]))
            thdata[i]['totalreply'] = int(k.group(0))
            with open(rootdir+'RefreshingData.json',"w",encoding='utf-8') as f:
                f.write(json.dumps(thdata,indent=2,ensure_ascii=False))
