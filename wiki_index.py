'''
使用BeautifulSoup4获取维基百科主页的所有词条
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re

# part 1:获取测试，请求URL并把结果用UTF-8编码
# resp = urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf-8')  # 最好使用utf-8编码显示
# soup = bs(resp, 'html.parser')
# print(soup)

# part 2:获取所有/wiki/开头的a标签的href属性
# resp = urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf-8')  # 最好使用utf-8编码显示
# soup = bs(resp, 'html.parser')
# listUrls = soup.findAll('a', href=re.compile('^/wiki/'))
# print(listUrls)

# part 3:简化输出1
# resp = urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf-8')  # 最好使用utf-8编码显示
# soup = bs(resp, 'html.parser')
# listUrls = soup.findAll('a', href=re.compile('^/wiki/'))
# for url in listUrls:
#     print(url['href'])#输出每个列表项的href属性

# part 4:简化输出2，过滤图片链接
# resp = urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf-8')  # 最好使用utf-8编码显示
# soup = bs(resp, 'html.parser')
# listUrls = soup.findAll('a', href=re.compile('^/wiki/'))
# for url in listUrls:
#     if not re.search("\.jpg|JPG$", url['href']):
#         print(url['href'])


# part 5:将链接补全
resp = urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf-8')  # 最好使用utf-8编码显示
soup = bs(resp, 'html.parser')
listUrls = soup.findAll('a', href=re.compile('^/wiki/'))
for url in listUrls:
    if not re.search("\.jpg|JPG$", url['href']):
        print(url.get_text(), ">>>", "https://en.wikipedia.org" + url['href'])
