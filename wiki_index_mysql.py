'''
使用BeautifulSoup4获取维基百科主页的所有词条
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re

# part 1:
resp = urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf-8')  # 最好使用utf-8编码显示
soup = bs(resp, 'html.parser')
listUrls = soup.findAll('a', href=re.compile('^/wiki/'))
for url in listUrls:
    if not re.search("\.jpg|JPG$", url['href']):
        print(url.get_text(), ">>>", "https://en.wikipedia.org" + url['href'])

print('Done!')
