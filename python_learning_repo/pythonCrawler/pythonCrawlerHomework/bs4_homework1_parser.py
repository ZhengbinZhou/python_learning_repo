"""
作业一：BeautifulSoup 解析器比较与使用

【题目说明】
结合你在 lesson7_bs4&4parser.py 学到的内容，完成下列任务：
1. 以字符串 html = '<div><p>Test<a>link' 为例，分别用 html.parser、lxml、html5lib 解析，
   输出每种解析器下 <a> 标签的内容（不要求写 try/except）。
2. 用你自己的话简述三种解析器的优缺点。

【填写区】
# ===== 代码区 start =====

# 1. 解析器比较
from bs4 import BeautifulSoup
html = '<div><p>Test<a>link'
# 用三种解析器处理，并输出 <a> 内容。请补全下方代码：
#
soup_html = BeautifulSoup(html, "html.parser")
soup_lxml = BeautifulSoup(html, "lxml")
soup_html5lib = BeautifulSoup(html, "html5lib")

print(soup_html.a.text)
print(soup_lxml.a.text)
print(soup_html5lib.a.text)

# 2. 简述三种解析器优缺点（用注释写出即可）
#
# html.parser:自带，速度中等，零依赖
# lxml:快且稳，需要安装 lxml
# html5lib:容错最强，最接近浏览器 DOM，较慢

# ===== 代码区 end =====
"""
