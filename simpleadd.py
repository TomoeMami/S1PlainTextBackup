# -*- coding: UTF-8 -*-
import codecs
import sys
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import os
import json
import io
import time

rootdir="./"

while 1:
    with open(rootdir+'RefreshingData.json',"r",encoding='utf-8') as f:
        thdata=json.load(f)
    ids = thdata.keys()
    threadid = input(u"S1 thread ID: ")
    if(threadid == '0'):
        break
    if(threadid in ids):
        print(u"早就有了！更新时间")
        thdata[threadid]['active'] = True
    else:
        print(u'请输入版面分类代号：\n1 = 外野，11 = 外野专楼\n2 = 漫区\n3 = 游戏区，33 = 手游专楼\n4 = 虚拟主播区专楼')
        threadcategory  = input(u'我选：')
        catechooser = {'1':'外野','11':'外野专楼','2':'漫区','3':'游戏区','33':'手游专楼','4':'虚拟主播区专楼'}
        thdata[threadid] = {}
        thdata[threadid]['totalreply'] = 0
        thdata[threadid]["title"] = "待更新"
        thdata[threadid]["newtitle"]= "待更新"
        thdata[threadid]["lastedit"]= int(time.time())
        thdata[threadid]["category"]= catechooser[threadcategory]
        thdata[threadid]["active"]= True
    with open(rootdir+'RefreshingData.json',"w",encoding='utf-8') as f:
            f.write(json.dumps(thdata,indent=2,ensure_ascii=False))
