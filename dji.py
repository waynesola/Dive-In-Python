'''
Created on 2017年1月13日
@author: Administrator
获取道琼斯工业股价平均指数（DJI）中的30家公司股价
'''

import urllib.request
import re

dStr = urllib.request.urlopen('https://hk.finance.yahoo.com/q/cp?s=%5EDJI').read()
getdStr = dStr.decode()  # 在python3中urllib.read()返回bytes对象而非str，语句功能是将dStr转换成str

m = re.findall('<tr><td class="yfnc_tabledata1"><b><a href=".*?">(.*?)</a></b></td>\
<td class="yfnc_tabledata1">(.*?)</td>.*?<b>(.*?)</b>.*?</tr>', getdStr)  # 含换行符'\'

if m:
    print(m)
    print('\n')
    print(len(m))
else:
    print('not match')
