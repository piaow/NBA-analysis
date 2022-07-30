import requests
import csv
from lxml import etree

url = 'https://nba.hupu.com/players/russellwestbrook-3016.html'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44'
}
resp = requests.get(url,headers=headers)
resp.encoding = 'utf-8'
# print(resp.text)

html = etree.HTML(resp.text)
trs = html.xpath("/html/body/div[3]/div[3]/div[1]/div[3]/div[3]/div/div/div[1]/table[2]/tbody/tr")
f1 = open('Kurantttt.csv', 'w', newline="", encoding='utf-8')
csv_writer = csv.writer(f1)

csv_writer.writerow([   trs[0].xpath("./td[1]/text()")[0],
                        trs[0].xpath("./td[18]/text()")[0], trs[0].xpath("./td[7]/text()")[0],
                        trs[0].xpath("./td[9]/text()")[0],trs[0].xpath("./td[11]/text()")[0],
                        trs[0].xpath("./td[12]/text()")[0], trs[0].xpath("./td[13]/text()")[0],
                        trs[0].xpath("./td[14]/text()")[0], trs[0].xpath("./td[15]/text()")[0]])

for i in range(1,15):
    csv_writer.writerow( [   trs[i].xpath("./td[1]/text()")[0],
                             trs[i].xpath("./td[18]/text()")[0],round( float(trs[i].xpath("./td[7]/text()")[0].split("%")[0])/100 ,3),
                              round( float(trs[i].xpath("./td[9]/text()")[0].split("%")[0])/100 ,3),
                              round( float(trs[i].xpath("./td[11]/text()")[0].split("%")[0])/100 ,3),
                              trs[i].xpath("./td[12]/text()")[0],trs[i].xpath("./td[13]/text()")[0],
                              trs[i].xpath("./td[14]/text()")[0] ,trs[i].xpath("./td[15]/text()")[0]])