import urllib.request
import urllib.error
'''
在爬虫的过程中，最容易出现的异常就是与URL相关了，使用URLError处理是最合适的
'''
try:
    urllib.request.urlopen('http://blog.csdn.net')
except urllib.error.URLError as e:
    print(e.code)
    print(e.reason)