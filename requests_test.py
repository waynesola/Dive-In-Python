import requests

url = 'https://sina.com.cn'

r = requests.get(url)
r.encoding = 'utf-8'
html = r.text
print(html)
