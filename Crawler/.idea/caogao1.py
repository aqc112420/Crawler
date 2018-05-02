#https://mp.weixin.qq.com/s/oO46GdmGeDdYGvW3B75qsg 教程链接
import requests
import codecs
import re
from bs4 import BeautifulSoup as BS
import lxml
import csv
urls = []
for i in list(range(1,11)):
    urls.append("https://rate.tmall.com/list_detail_rate."
                "htm?itemId=539696221085&spuId=705882082&sellerId=1675299352&order=3&currentPage={}".format(i))

nickname = []
ratedate = []
color = []
size = []
ratecontent = []
for url in urls:
    content = requests.get(url).text
    nickname.extend(re.findall('"displayUserNick":"(.*?)"',content))
    color.extend(re.findall(re.compile('颜色分类:(.*?);'),content))
    size.extend(re.findall(re.compile("尺码:(.*?),"),content))
    ratecontent.extend(re.findall(re.compile('"rateContent":"(.*?)","rateDate"'),content))
    ratedate.extend(re.findall(re.compile('"rateDate":"(.*?)","reply"'),content))
# print(nickname, color, ratecontent)
print(len(size),len(nickname),len(color),len(ratecontent),len(ratedate))


file = open("D:/南极人评价.csv","w")
# file.write(','.join("nickname","ratedate","color","size","ratecontent")+'\n')
# writer = csv.writer(file)
# writer.writerow(["nickname","ratedate","color","size","ratecontent"])
for i in list(range(len(size))):
    file.write(','.join((nickname[i],ratedate[i],color[i],size[i],ratecontent[i]))+"\n")
file.close()
