# -*- coding: UTF-8 -*-
import codecs
import sys
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import os
import json
import io
import time
from copy import deepcopy

rootdir="/home/riko/S1PlainTextBackup/"
with open(rootdir+'RefreshingData.json',"r",encoding='utf-8') as f:
    thdata=json.load(f)
newthdata = deepcopy(thdata)
for i in thdata.keys():
    if thdata[i]['totalreply'] // 30 < 15 and not thdata[i]['active']:
        if thdata[i]['newtitle'] == '[]':
            newthdata.pop(i)
with open(rootdir+'RefreshingData.json',"w",encoding='utf-8') as f:
        f.write(json.dumps(newthdata,indent=2,ensure_ascii=False))
print("finish")
