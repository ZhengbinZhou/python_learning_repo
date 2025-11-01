import requests
import os
url = "https://bkimg.cdn.bcebos.com/pic/3c6d55fbb2fb43166d22d257a1f2512309f7905275dd"
path = "C://Users//Eddie//OneDrive//Pictures//Screenshots.jpg"
try:
    if os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")