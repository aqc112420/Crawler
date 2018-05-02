import re
import urllib.request
import requests
from bs4 import BeautifulSoup as BS
url = 'http://www.mzitu.com/26685'
header = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer':'http://www.mzitu.com'
               }
# header = {
#     "User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'
#
# }

html = requests.get(url,header)
# print(html.text)

soup = BS(html.text,'html.parser')

# all_a = soup.find('div',{"class":"postlist"}).find_all('a',target="_blank")
# for a in all_a:
#     title = a.get_text()
#     print(title)

pic_max = soup.find_all('span')[10].text
print(pic_max)

#找标题
title = soup.find('h2',{"class":"main-title"}).text

#输出每个图片页面的网址
for i in range(1,int(pic_max) + 1):
    href = url + '/' + str(i)
    html = requests.get(href,headers=header)
    mess = BS(html.text,'html.parser')

    #图片地址在img标签alt属性和标题一样的地方
    pic_url = mess.find('img',alt=title)
    html = requests.get(pic_url['src'],headers=header)

    #获取图片的名字方便命名
    file_name = pic_url['src'].split(r'/')[-1]

    #图片不是文本文件，以二进制的格式写入，所以是html.content
    f = open('D:/2/'+file_name,'wb')
    f.write(html.content)
    f.close()


