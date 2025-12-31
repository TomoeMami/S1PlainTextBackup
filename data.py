 # -*- coding: UTF-8 -*-
import re
import json
from pathlib import Path
import os
import time

def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    path=path.encode('utf-8')
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)

    # 判断结果
    if not isExists:
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        return False


rawpathdict = {
    'a' :  {
        '2' : './虚拟主播区专楼/2045155[【A27】A-SOUL讨论楼（新年新气象！）]/'
        # '1' : './虚拟主播区专楼/2038500[【A26】A-SOUL讨论楼]/'
        },
    'b' : {
        # '1' : './虚拟主播区专楼/2042657[【B47】VUP综合讨论楼]/',
        '2' : './虚拟主播区专楼/2045381[【B49】VUP综合讨论楼]/',
        '3' : './虚拟主播区专楼/2045222[【B48】VUP综合讨论楼]/',
        '4' : './虚拟主播区专楼/2046797[【B50】VUP综合讨论楼]/',
        '5' : './虚拟主播区专楼/2043328[【B51】VUP综合讨论楼]/',
        '7' : './虚拟主播区专楼/2047360[【B52】VUP综合讨论楼]/'
        # 'A' : './虚拟主播区专楼/2042668-01[【B46：free】VUP综合讨论楼的应许之地].md'
     },
    'c' : { '1' : './虚拟主播区专楼/1966145[【C1】巧克拉拉／哔哩哔哩vup综合讨论楼]/'
    },
    'h' :  {'1' : './虚拟主播区专楼/2018062[ケーキアツアツ]/'
    },
    'm' :  {'1' : './虚拟主播区专楼/2018830[【M14】神楽Mea(KaguraMea)讨论楼]/'
    },
    'v' :  {'1' : './虚拟主播区专楼/1972669[【V14】虚拟YouTuber(vtuber)综合讨论楼]/'
    },
}
# apaths = ['./S1PlainTextGeneral/虚拟主播区专楼/虚拟主播【Asoul】/','./S1PlainTextBackup/虚拟主播区专楼/2019599[【A18】A-SOUL讨论楼（8月8日，20：00，乃琳生日会）]/']

# bpaths = ['./S1PlainTextGeneral/虚拟主播区专楼/虚拟主播【B综】/','./S1PlainTextBackup/虚拟主播区专楼/2017705[【B32】VUP综合讨论楼]/']

# cpaths = ['./S1PlainTextBackup/虚拟主播区专楼/1966145[【C1】巧克拉拉／哔哩哔哩vup综合讨论楼]/']

# hpaths = ['./S1PlainTextGeneral/虚拟主播区专楼/虚拟主播【H综】/','./S1PlainTextBackup/虚拟主播区专楼/2018062-01[再放送スレ].md']

# mpaths = ['./S1PlainTextGeneral/虚拟主播区专楼/虚拟主播【Mea楼】/','./S1PlainTextBackup/虚拟主播区专楼/2018830-01[【M14】神楽Mea(KaguraMea)讨论楼].md']

# vpaths = ['./S1PlainTextGeneral/虚拟主播区专楼/虚拟主播【V综】/','./S1PlainTextBackup/虚拟主播区专楼/1972669[【V14】虚拟YouTuber(vtuber)综合讨论楼]/']

def get2levelfile(dirpath,allpath):
    for pa in Path(dirpath).iterdir():
        allpath.append(pa)
# def getkwfile(flist, keyword):
#     res = []
#     for ff in flist:
#         if keyword in ff.split('\\')[-1]:   # 切分出文件名来再判断，可以缩短判断时间
#             res.append(ff)
#     return res

if __name__ == "__main__":
    pathdict = {}
    temppaths = []
    for key in rawpathdict.keys():
        count = 0
        pathdict[key] = {}
        for i in rawpathdict[key].keys():
            temppaths.clear()
            if i.isdigit():
                get2levelfile(rawpathdict[key][i],temppaths)
                for k in temppaths :
                    pathdict[key][str(count)] = k
                    count = count + 1
            else:
                pathdict[key][str(count)] = rawpathdict[key][i]
                count = count + 1
    for key in pathdict.keys():
        rawdata = []
        for filepath in pathdict[key].values():
            with open (filepath, 'r',encoding='UTF-8') as f:
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
                data['time'] = ''.join(re.findall(r"^.*?发表于\s(\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2})", post2))
                if(data['id']):
                    res.append(data)
            rawdata = rawdata + res
        mkdir('./S1B/')
        with open('./S1B/'+key+'-RawData.json', "w", encoding="utf-8") as f:
            f.write(json.dumps(rawdata,indent=2,ensure_ascii=False))


        # data = {}
        # for post in rawdata:
        #     postintime = int(time.mktime(time.strptime(post['time'],"%Y-%m-%d %H:%M")))
        #     if postintime%86400 :
        #         postintime = postintime - postintime%86400
        #     posttime = time.strftime("%Y-%m-%d", time.localtime(postintime))
        #     if posttime not in data.keys():
        #         data[posttime] = {}
        #         data[posttime]['num'] = 1
        #         data[posttime]['ids'] = {}
        #     else:
        #         data[posttime]['num'] = data[posttime]['num'] +1
        #         data[posttime]['ids'][post['id']] = 1

        # datadict = data
        # data = []
        # stime = []
        # reply = []
        # replyer = []
        # for keyd in sorted(datadict.keys()):
        #     c = keyd
        #     d = datadict[keyd]['num']
        #     e = len(datadict[keyd]['ids'].keys())
        #     stime.append(c)
        #     reply.append(d)
        #     replyer.append(e)
        # data.append(stime)
        # data.append(reply)
        # data.append(replyer)
        # mkdir('./S1B/')
        # with open('./S1B/'+key+'-Data.json', "w", encoding="utf-8") as f:
        #     f.write(json.dumps(data,indent=2,ensure_ascii=False))
