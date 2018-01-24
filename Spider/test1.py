import urllib.request
#第一种方法
print(urllib.request.quote('http:%3A//www.sina.com'))
# file = urllib.request.urlopen("http%3A//github.com")
# # print(file.info(),file.getcode(),file.geturl())
# data = file.read()
# fhandl = open("./1.html","wb")
# fhandl.write(data)
# fhandl.close()
# dataline = file.readline()
# # print(dataline)
#
# #第二种方法，使用urlib.request中的urlretrieve()函数直接将目标地址的内容写入到文件中
# filename= urllib.request.urlretrieve("http://www.baidu.com",filename="./2.html")
# urllib.request.urlcleanup()#清楚urlretrieve执行过程中产生的缓存

