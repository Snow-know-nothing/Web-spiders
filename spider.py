#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@Description:  ineternet spider   :
@Date     :2021/01/23 23:43:42
@Author      :Mao Rui
'''
from bs4 import BeautifulSoup
import sqlite3
import re
import urllib.request
import xlwt
def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1.爬取网页
    DataList = getData(baseurl)
    savepath = ".\\豆瓣电影.xls"
    Imagepath =".\\图片抓取\\电影"
    #保存数据
    saveData(DataList,savepath)
    saveImage(DataList,Imagepath)
    

findlink =  re.compile(r'<a href="(.*?)">')   #创建正则表达式的对象，表示规则
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)    #re.S让换行符包括在其中
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)



def getData(baseurl):
    datalist = []
    for i in range(0,10):           #想要爬几个页面 
        url = baseurl + str(i*25)  #调用获取页面的信息25次
        html = askURL(url)         #保存获取到的网页源码
    #2.逐一解析数据
        soup = BeautifulSoup(html,"html.parser")               #将网页信息转化为树结构
        for item in soup.find_all('div',class_="item"):      #查找符合要求的字符串，形成列表
            # print(item)        #测试查看到的item标签信息
            data = []   #保存每一步电影的信息
            item = str(item)

            link = re.findall(findlink,item)[0]     #re库通过正则表达式查找指定的字符串
            data.append(link)
           
            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)
            
            titles = re.findall(findTitle,item)
            if len(titles) == 2:
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/"," ")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(" ")
            
            rating = re.findall(findRating,item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")
            
            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)
            bd = re.sub('/'," ",bd)      #替换
            data.append(bd.strip())

            datalist.append(data)
    return datalist


#得到指定一个url的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
    }
    req = urllib.request.Request(url=url,headers=head) #此时方法是get
    html = ""
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html


def saveData(datalist,savepath):
    print('save...')
    workbook = xlwt.Workbook(encoding="utf-8",style_compression=0)
    worksheet = workbook.add_sheet('豆瓣电影top250',cell_overwrite_ok=True)
    col = ("详情链接","图片链接","影片中文名","影片又名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        worksheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,8):
            worksheet.write(i+1,j,data[j])
   
    workbook.save(savepath)

def saveImage(datalist,savepath):
    n = 0
    for data in datalist:
        n += 1
        try:
            request=urllib.request.Request(data[1])
            response =urllib.request.urlopen(request)
            imgData=response.read()#图片的二进制数据流
            pathfile =savepath+str(n)+".jpg" #路径+图片编号+原始图片后缀
            with open( pathfile,'wb') as f:
                f.write(imgData) #将图片的二进制数据流写入文件
                f.close()
                print('下载完成图片'+str(n))
        except:
            print('11')

if __name__ == "__main__":
    main()
    print("finish!")