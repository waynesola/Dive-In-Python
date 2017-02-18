'''
使用BeautifulSoup4获取维基百科主页的所有词条，并保存在MySQL数据库。
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re
import pymysql.cursors


resp = urlopen('https://en.wikipedia.org/wiki/Main_Page').read().decode('utf-8')  # 最好使用utf-8编码显示
soup = bs(resp, 'html.parser')
listUrls = soup.findAll('a', href=re.compile('^/wiki/'))

for url in listUrls:
    if not re.search("\.jpg|JPG$", url['href']):
        print(url.get_text(), ">>>", "https://en.wikipedia.org" + url['href'])

        # 获取数据库链接
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='88888888',
                                     # db亦作database，即Schema名
                                     db='wiki_url',
                                     charset='utf8mb4')

        try:
            # 获取会话指针
            with connection.cursor() as cursor:
                # 创建SQL语句
                sql = "insert into `urls` (`urlname`, `urlhref`) values (%s, %s)"
                # 执行SQL语句
                cursor.execute(sql, (url.get_text(), "https://en.wikipedia.org" + url['href']))
                # 提交
                connection.commit()
        finally:
            connection.close()
