#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import re
from pathlib import Path

def getallfile(dirpath,allpath=[]):
    for pa in Path(dirpath).iterdir():
        if Path(pa).is_dir():
            print(pa)
            getallfile(pa)
        else:
            allpath.append(pa)
    return allpath

if __name__ == "__main__":
    vtb = './虚拟主播区专楼'
    allpath = getallfile(vtb)
    ids = re.findall(r'(\d{7,9})-\d{2}\[【A\d+】',str(allpath))
    thread = max(set(ids))
    with open ('A-Thread-id.txt','w',encoding='utf-8') as f:
        f.write(thread)
