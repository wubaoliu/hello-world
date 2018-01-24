import urllib.request
import urllib.parse
import pdb
'''
需要用户名密码登陆的页面，只能在当前页面有效，当这个页面还有其他页面链接时，爬取其他页面的时候，用户名就会失效
这时就需要用到缓存了cookie和session
'''
url = 'https://i.taobao.com/my_taobao.htm?spm=875.7931836/B.a2226mz.7.9078e51qR1jcZ'
postdata = urllib.parse.urlencode({
    "username":"17682301541",
    "password":"LIU940115"
}).encode('utf-8')
pdb.set_trace()
req = urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36')
data = urllib.request.urlopen(req).read()
fhandle = open('./Tall.html','wb')
fhandle.write(data)
fhandle.close()