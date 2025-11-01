# 这个程序演示了如何使用BeautifulSoup库来解析HTML内容。
# 一个简单的Demo，获取一个网页的HTML内容并使用BeautifulSoup进行解析，然后以格式化的方式输出HTML结构。
import requests

r = requests.get('http://python123.io/ws/demo.html')
demo = r.text
from bs4 import BeautifulSoup

soup = BeautifulSoup(demo, 'html.parser')  # 使用html.parser解析器
print(soup.prettify())