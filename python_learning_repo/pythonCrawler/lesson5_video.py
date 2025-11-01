import requests
url = "https://www.ip138.com/"
head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
try:
    r=requests.get(url,headers=head,auth=())#kv可以随便改
    print(r.status_code)
    r.encoding=r.apparent_encoding
    r.raise_for_status()
    print(r.text)
except requests.exceptions.Timeout as e:
    print (f"timeout: {e}")
except requests.exceptions.HTTPError as e:
    print (f"http error: {e}")
except requests.exceptions.RequestException as e:
    print (f"request exception: {e}")
except Exception as e:
    print (f"other error: {e}")