import re
import urllib.request
import pdb
def getlink(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Mobile Safari/537.36')
    data = str(urllib.request.urlopen(req).read())
    pdb.set_trace()
    pattern = '(https:\/\/edu\.csdn\.net\/)'
    link = re.compile(pattern).findall(data)
    link = list(set(link))
    return link
url = "http://blog.csdn.net/"
# pdb.set_trace()
linklist = getlink(url)
for link in linklist:
    print(link)
