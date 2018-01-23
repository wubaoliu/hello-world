import urllib.request
import urllib.parse
'''
Get、Post、Put、Delete、Head、Option六种请求协议类型
'''
#GET
keywd = 'hello'
url = "http://www.baidu.com/s?wd="+keywd
#如果关键字是中文或者其他不能直接检索的符号的话，将用一下方法进行解码
# key = '刘武保'
# key_code = urllib.request.quote(key)
# url = (url + key_code)
req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()
fhandle = open('./5.html','wb')
fhandle.write(data)
fhandle.close()

#POST
url1 = "http://www.iqianyue.com/mypost/"
postdata = urllib.parse.urlencode({
    'name':'ceo@peterliu.com',
    'pass':'a123456'
}).encode('utf-8')
req1 = urllib.request.Request(url1,postdata)
req1.add_header('User-Agent','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36')
data1 = urllib.request.urlopen(req1).read()
fhandle1 = open('./6.html','wb')
fhandle1.write(data1)
fhandle1.close()
