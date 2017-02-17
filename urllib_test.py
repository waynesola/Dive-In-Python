

# part 1:
#from urllib import request
# resp = request.urlopen("http://www.baidu.com")
# print('resp:')
# print(resp)
# print('decode:')
# print(resp.read().decode('utf-8'))


# part 2:
#from urllib import request
# req = request.Request("http://www.baidu.com")
# req.add_header('User-Agent',
#                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
# resp = request.urlopen(req)
# print('decode:')
# print(resp.read().decode("utf-8"))


# part 3:使用urllib发送post请求
from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

#发送头信息，预防网站禁止爬虫机制
req = Request('http://www.thsrc.com.tw/tw/TimeTable/SearchResult')
req.add_header('Origin', 'http://www.thsrc.com.tw')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537')

#数据参数列表
postData = parse.urlencode([
    ('StartStation', '977abb69-413a-4ccf-a109-0272c24fd490'),
    ('EndStation', '9c5ac6ca-ec89-48f8-aab0-41b738cb1814'),
    ('SearchDate', '2017/02/12'),
    ('SearchTime', '19:00'),
    ('SearchWay', 'DepartureInMandarin')
])

resp = urlopen(req, data=postData.encode('utf-8'))

print(resp.read().decode('utf-8'))
