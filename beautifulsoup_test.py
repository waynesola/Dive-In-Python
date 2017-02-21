from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# 下面的html5lib是解析器。可以选择第三方库"lxml"，或标准库"html.parser"

# 指定文本
soup = BeautifulSoup(html_doc, "html5lib")
# 指定本地html
# soup = BeautifulSoup(open(r"C:\Users\Administrator\Desktop\html_doc.html"), "html5lib")
# 指定网址
# soup = BeautifulSoup("www.baidu.com", "html5lib")


# prettify() 方法将Beautiful Soup的文档树格式化后以Unicode编码输出,每个XML/HTML标签都独占一行
print(soup.prettify())

# BeautifulSoup 对象和它的tag节点都可以调用 prettify() 方法
print(soup.a.prettify())

# tag 对象
tag = soup.title
print(tag)

# name 属性
print(tag.name)

# 用attrs点取属性，返回字典。
print(soup.a.attrs)

# 获取标签
print(soup.title.string)
print(type(soup.title.string))

# 替换标签里的字符串
tag.string.replace_with("A Short Story")
print(tag)

# 获取父标签
print(soup.title.parent.name)

# 获取第一个a标签
print(soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>


# 获取soup的第一个a标签的class属性
print(soup.a["class"])


# 查找第一个title标签，直接返回结果
print(soup.find('title'))


# 查找第一个title标签，返回一个元素的列表
soup.find_all('title', limit=1)


# find_all( name , attrs , recursive , text , **kwargs )方法
# 查找所有a标签
print(soup.find_all('a'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]


# 使用正则表达式查找所有以b开头的标签
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

# 使用正则表达式查找所有名字中包含”t”的标签:
for tag in soup.find_all(re.compile("t")):
    print(tag.name)

# 查找所有a,b标签
soup.find_all(["a", "b"])

# 查找所有属性值为title的p标签
soup.find_all("p", "title")
# [<p class="title"><b>The Dormouse's story</b></p>]


# 查找id为lin3的标签
print(soup.find(id="link3"))
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


# 查找所有标签的text含sisters的字符串，返回字符串列表
print(soup.find_all(text=re.compile("e")))
# u'Once upon a time there were three little sisters; and their names were\n'


# 查找所有class属性为sister的a标签
print(soup.find_all("a", attrs={"class": "sister"}))


