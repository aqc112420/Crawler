import re
from bs4 import BeautifulSoup as BS
from bs4 import NavigableString as NS

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>"""

soup = BS(html_doc,'html.parser')
# for sibling in soup.a.next_siblings:
#     print(sibling)
# # tag = soup.find_all("a",{"class":"sister"})
# # for i in tag:
# #     print(i["href"])
# # tag = soup.body.p
# # for child in tag.descendants:
# #     print(child)
# print(len(list(soup.descendants)))

# sibing_soup = BS("<a><b>text1</b><c>text2</c></b></a>")
# print(sibing_soup.c.previous_sibling)


def not_lacie(href):
    return href and not re.compile("lacie").search(href)


def surrounded_by_strings(tag):
    return (isinstance(tag.next_elment,NS) and isinstance(tag.previous_element,NS))


def has_6_characters(css_class):
    return css_class is not None and len(css_class) == 6


print(soup.find("a"))
print(soup.find_all("a"))


# import re
# import lxml
# from bs4 import BeautifulSoup as BS
# import urllib.request as urlre
# import requests
# url = "http://www.kugou.com/song/lujpe1d.html?frombaidu?frombaidu#hash=85180C68F9388721D3D9199440AD493B&album_id=0"
#
# page = urlre.urlopen(url)
# html = page.read()
# soup = BS(html,'html.parser')
# print(soup.prettify())
# tag = soup.find("div",{"class":"displayNone"})
# print(tag.string)
