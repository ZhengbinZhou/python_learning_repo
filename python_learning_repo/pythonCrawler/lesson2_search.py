import requests
url = "https://so.com/s"
kv={'q':'python'}#baidu 是 wd, so.com 是 q
try:
    r=requests.get(url,params=kv)#kv可以随便改
    print(r.status_code)
    r.encoding=r.apparent_encoding
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")
