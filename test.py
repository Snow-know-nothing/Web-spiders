import urllib.request
# data = bytes( )
# response = urllib.response.urlopen("http://httpbin.org/post")##拓展：post 请求操作cookie 登录网站
# print(response.read().decode("utf-8"))

##伪装成一个浏览器，将请求对象封装
# url = "http://httpbin.org/post"
# headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
# }##模仿浏览器配置键值对
# data = bytes(urllib.parse.urlencode({'name':'flash'}),encoding="utf-8")
# req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

# url = "https://movie.douban.com/top250"
# headers={
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
# }##模仿浏览器配置键值对
# # data = bytes(urllib.parse.urlencode({'name':'flash'}),encoding="utf-8")
# req = urllib.request.Request(url=url,headers=headers) #此时方法是get
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

# from bs4 import BeautifulSoup
# type(bs.head)tag  标签及其内容
# navigablestring  标签里的字符串内容
# attrs

# bs = find_all

# t_list = bs.find_all(re.compile("a")) 
# search()#正则表达式搜索   
 

# import re
# findlink =  re.compile(r'sjh(.?)') 
# bs = 'sjhajkhailfhiolajilfolsjhfhfkhfik'
# t = findlink.findall(bs)
# print(t)

import xlwt
workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('sheet1')
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d*%d=%d"%(i+1,j+1,(i+1)*(j+1)))
workbook.save('student.xls')