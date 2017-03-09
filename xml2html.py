import lxml
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("all.xml"), "xml")
all = soup.find_all('item')
markup = BeautifulSoup("<meta charset=\"UTF-8\">", "html5lib")
for a in all:
    title = a.title.get_text()
    publish = a.publish.get_text()
    text = a.text.get_text()
    link = a.link.get_text()

    original_tag = soup.link

    new_tag = soup.new_tag("a", href=link)
    original_tag.append(new_tag)
