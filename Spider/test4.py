import urllib.request

'''
使用同一个IP去对同一个网站进行长久的爬取，到后期可能会被屏蔽，所以这样的情况
需要对我们自己的IP进行伪装，也就是代理服务器
'''
def use_proxy(proxy_addr,url):
    proxy = urllib.request.ProxyHandler({'http':proxy_addr})
    opender = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opender)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data

proxy_addr = "127.0.0.1:3306"
data = use_proxy(proxy_addr,"http://www.baidu.com")
print(len(data))