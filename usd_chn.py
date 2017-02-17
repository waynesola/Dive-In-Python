'''
Created on 2017年1月13日
@author: Administrator
获取离岸人民币兑美元汇率
'''
import urllib.request
import re

dStr = urllib.request.urlopen('http://finance.yahoo.com/quote/USDCNH=X?ltr=1').read()
getdStr = dStr.decode()  # 在python3中urllib.read()返回bytes对象而非str，语句功能是将dStr转换成str

regularMarketPrice = re.findall('"currency":"CNH","regularMarketPrice":{"raw":(.*?),', getdStr)
regularMarketPreviousClose = re.findall('"regularMarketPreviousClose":{"raw":(.*?),"fmt":".*?"},"currencySymbol":"CNH"',
                                        getdStr)
regularMarketChange = re.findall(
    '"averageDailyVolume10Day":{},"longName":null,"regularMarketChange":{"raw":(.*?),"fmt":".*?"}', getdStr)

if regularMarketPrice:
    print('regularMarketPrice:')
    print(regularMarketPrice)
else:
    print('not match')

if regularMarketPreviousClose:
    print('regularMarketPreviousClose:')
    print(regularMarketPreviousClose)
else:
    print('not match')

if regularMarketChange:
    print('regularMarketChange:')
    print(regularMarketChange)
else:
    print('not match')
