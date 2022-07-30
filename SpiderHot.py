import requests
import csv
from lxml import etree

url = 'https://nba.hupu.com/stats/players'
headers = {
# print(resp.text)
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44'
}
resp = requests.get(url,headers=headers)
resp.encoding = 'utf-8'

#此项目运用xpath解析方式进行爬虫
#解析
html = etree.HTML(resp.text)

# 将每个链接添加入链表当中
hrefs =["https://nba.hupu.com"+ html.xpath("/html/body/div[3]/div[4]/div/div/span[1]/a/@href")[0]]

hrefs.append("https://nba.hupu.com"+ html.xpath("/html/body/div[3]/div[4]/div/div/span[5]/a/@href")[0] )

hrefs.append("https://nba.hupu.com"+ html.xpath("/html/body/div[3]/div[4]/div/div/span[6]/a/@href")[0] )

# 对每个链接(子页面)循环，提取到需要的数据
#**************************************************************************
for href in hrefs:
    print(href)
    #重复：请求，响应，解析url的过程
    kidresp = requests.get(href)
    kidresp.encoding = 'utf-8'
    kidhtml = etree.HTML(kidresp.text)
    trs = kidhtml.xpath("/html/body/div[3]/div[4]/div/table/tbody/tr")

    #对每项内容想获取的数据位置不同，因此需要判断
    if(href == hrefs[0] ):
        f1 = open('score.csv', 'w', newline="", encoding='utf-8')
        csv_writer = csv.writer(f1)
        csv_writer.writerow([ trs[0].xpath("./td[1]/text()")[0],trs[0].xpath("./td[2]/text()")[0],
                              trs[0].xpath("./td[3]/text()")[0],trs[0].xpath("./td[4]/text()")[0],
                              trs[0].xpath("./td[6]/text()")[0],trs[0].xpath("./td[8]/text()")[0],
                              trs[0].xpath("./td[10]/text()")[0] ,trs[0].xpath("./td[12]/text()")[0] ])
        # print(trs[0].xpath("./td[1]/text()"),trs[0].xpath("./td[2]/text()"),trs[0].xpath("./td[4]/text()"),trs[0].xpath("./td[12]/text()") )
        i=0
        j=0
        for tr in trs[1:]:
            i=i+1

            id = tr.xpath("./td[1]/text()")[0]
            name = tr.xpath("./td[2]/a/text()")[0]
            team = tr.xpath("./td[3]/a/text()")[0]
            score = tr.xpath("./td[4]/text()")[0]
            hitPossibility = round( float(tr.xpath("./td[6]/text()")[0].split("%")[0])/100 ,3)
            threeHitPossibility = round( float(tr.xpath("./td[8]/text()")[0].split("%")[0])/100 ,3)
            twoHitPossibility = round( float(tr.xpath("./td[10]/text()")[0].split("%")[0])/100 ,3)
            time = tr.xpath("./td[12]/text()")[0]

            csv_writer.writerow([id, name,team, score,hitPossibility ,threeHitPossibility ,twoHitPossibility, time])


            if(i<5):

                kiddresp = requests.get(tr.xpath("./td[2]/a/@href")[0])
                print(kiddresp)
                kiddresp.encoding = 'utf-8'
                kiddhtml = etree.HTML(kiddresp.text)

                trss = kiddhtml.xpath("/html/body/div[3]/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/table[1]/tbody/tr   ")

                f22 = open('ScoreFouth.csv', 'a', newline="", encoding='utf-8')
                csv_writerr = csv.writer(f22)

                name = kiddhtml.xpath("/html/body/div[3]/div[3]/div[1]/div[1]")

                if(j == 0):
                    j=j+1
                    csv_writerr.writerow([ "球员",  trss[1].xpath("./td[15]/text()")[0], trss[1].xpath("./td[4]/text()")[0],
                                         trss[1].xpath("./td[6]/text()")[0], trss[1].xpath("./td[8]/text()")[0],
                                         trss[1].xpath("./td[9]/text()")[0], trss[1].xpath("./td[10]/text()")[0],
                                         trss[1].xpath("./td[11]/text()")[0], trss[1].xpath("./td[12]/text()")[0] ])

                csv_writerr.writerow([ name[0].xpath("./h2/text()")[0],  trss[2].xpath("./td[15]/text()")[0], round(float(trss[2].xpath("./td[4]/text()")[0].split("%")[0])/100,3),
                                      round(float(trss[2].xpath("./td[6]/text()")[0].split("%")[0])/100,3),  round(float(trss[2].xpath("./td[8]/text()")[0].split("%")[0])/100,3),
                                      trss[2].xpath("./td[9]/text()")[0], trss[2].xpath("./td[10]/text()")[0],
                                      trss[2].xpath("./td[11]/text()")[0], trss[2].xpath("./td[12]/text()")[0]])



                # id = tr.xpath("./td[1]/text()")[0]
                # name = tr.xpath("./td[2]/a/text()")[0]
                # team = tr.xpath("./td[3]/a/text()")[0]
                # score = tr.xpath("./td[15]/text()")[0]
                # hitPossibility = round(float(tr.xpath("./td[6]/text()")[0].split("%")[0]) / 100, 3)
                # threeHitPossibility = round(float(tr.xpath("./td[8]/text()")[0].split("%")[0]) / 100, 3)
                # twoHitPossibility = round(float(tr.xpath("./td[10]/text()")[0].split("%")[0]) / 100, 3)
                # time = tr.xpath("./td[12]/text()")[0]
                #
                # csv_writerr.writerow(
                #         [id, name, team, score, hitPossibility, threeHitPossibility, twoHitPossibility, time])


    # if (href == hrefs[1]):
    #     print(trs[0].xpath("./td[1]/text()"),trs[0].xpath("./td[2]/text()"),trs[0].xpath("./td[4]/text()"))
    #     for tr in trs[1:]:
    #         id = tr.xpath("./td[1]/text()")
    #         name = tr.xpath("./td[2]/a/text()")
    #         backboard = tr.xpath("./td[4]/text()")
    #         print(id,name, score)
    #
    # if (href == hrefs[2]):
    #     print(trs[0].xpath("./td[1]/text()"),trs[0].xpath("./td[2]/text()"),trs[0].xpath("./td[4]/text()"))
    #     for tr in trs[1:]:
    #         id = tr.xpath("./td[1]/text()")
    #         name = tr.xpath("./td[2]/a/text()")
    #         assist = tr.xpath("./td[4]/text()")
    #         print(id,name, assist)

