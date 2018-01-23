'''
有些网页具有反爬取设置，我们需要模拟成浏览器去访问这些网站
第一种方法使用bulid_opener()修改报头
'''
import urllib.request
url = "http://www.zhifu.com"
file = urllib.request.urlopen(url)
data = file.read()
fhandl = open("./4.html","wb")
fhandl.write(data)
fhandl.close()
print(file.getcode())