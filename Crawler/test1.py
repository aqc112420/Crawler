from urllib.request import urlopen
import urllib.parse
from urllib.error import HTTPError
from bs4 import BeautifulSoup as BS
import re
import datetime
import random
# html = request.urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bsObj = BS(html)
# # nameList = bsObj.findAll("span",{'class':'green'})
# allText = bsObj.findAll(id='text')
#
# # for name in nameList:
# #     print(name.get_text())
# print(allText[0].get_text())
# # print(bsObj.nonExistentTag)



# url = "http://restapi.amap.com/v3/staticmap?location=101.86039,25.71999&traffic=1&zoom=10&scale=2&size=400*400&makers=mid&labels=7,2,0,16,0xFFFFFF,0x008000:101.86039,25.71999&key=fb9a94655c1ee8b49602d878ca47ebce"
# html = urlopen(url)
# bsObj = BS(html.read())
# for child in bsObj.find("table",{"id":"giftList"}).descendants:
#     print(child)
#
# for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_sibling:
#     print(sibling)
# print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_siblings)

# images = bsObj.findAll("img")
# print(bsObj.body.img)
# random.seed(datetime.datetime.now())
# def getLinks(articleUrl):
#     html = urlopen("http://en.wikipedia.org"+articleUrl)
#     bsObj = BS(html)
#     return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
#
# links = getLinks("/wiki/Kevin_Bacon")
# while len(links) > 0:
#     newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
#     print(newArticle)
#     links = getLinks(newArticle)
#
#

#数据收集
# pages = set()
# def getLinks(articleUrl):
#     global pages
#     html = urlopen("http://en.wikipedia.org"+articleUrl)
#     bsObj = BS(html)
#     try:
#         print(bsObj.h1.get_text())
#         print(bsObj.find(id="mw-content-text").findAll("p")[0])
#         print(bsObj.find(id="ca-edit").find("span").find("a").attrs["href"])
#     except AttributeError:
#         print("页面缺少一些属性，不过不用担心")
#
#     for link in bsObj.findAll("a",href=re.compile("^(/wiki/)")):
#         if "href" in link.attrs:
#             if link.attrs["href"] not in pages:
#                 #遇到了新页面
#                 newPage = link.attrs['href']
#                 print("----------\n"+newPage)
#                 pages.add(newPage)
#                 getLinks(newPage)
#
# getLinks("")


from bs4 import BeautifulSoup as BS
from urllib.request import  urlretrieve
from urllib.request import  urlopen

def download(_url,name):
    if _url == None:
        pass

    result = urlopen(_url)
    if result.getcode != 200:
        pass
    else:
        data = result.read()
        with open(name,"wb") as f:
            f.write(data)
            f.close()


url = "https://zhuanlan.zhihu.com/p/35696287"
res = urlopen(url)
respond = res.read()
count = 0
soup = BS(respond)
list1 = []

for link in soup.find_all("img"):
    addr = link.get("data-original")
    list1.append(addr)

s = set(list1)
for addr1 in s:
    if (addr1 != None):
        pathName = "F:/pic/" + str(count+1) + ".jpg"
        download(addr1,pathName)
        count = count + 1
        print("downloading:{}".format(count))


#Demo
# import urllib.request
# import re
#
# def getHtml(url):
#     page = urllib.request.urlopen(url)
#     html = page.read()
#     return html
#
# def getImg(html):
#     reg = 'src="(.+?\.jpg)" alt='
#     imgre = re.compile(reg)
#     html = html.decode('utf-8')
#     imglist = re.findall(imgre, html)
#     x = 0
#     for imgurl in imglist:
#         urllib.request.urlretrieve(imgurl, '%s.jpg' % x)
#         x+=1
#     return imglist
#
# html = getHtml("http://pic.yxdown.com/list/0_0_1.html")
#
# print( getImg(html))
