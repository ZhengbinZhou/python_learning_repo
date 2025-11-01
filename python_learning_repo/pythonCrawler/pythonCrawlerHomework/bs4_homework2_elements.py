"""
作业二：标签元素查找与属性练习

【题目说明】
结合你在 lesson8_bs4_elements.py 学到的内容，完成下列任务：
1. 给定如下 HTML，查找所有 class 为 "pic" 的 <img> 标签，并输出 src 属性。
2. 查找所有带 href 的 <a> 标签，并输出文本内容及 href 值。
3. 用 CSS 选择器找到 id 是 "main" 的 <div> 下所有 <span> 元素文本。

html = '''
<html><body>
  <div id="main">
    <span>One</span>
    <span>Two</span>
    <img src="img1.png" class="pic"/>
    <a href="http://a.com">A</a>
    <a>Plain</a>
    <img src="img2.jpg" class="icon"/>
    <img src="cat.jpg" class="pic"/>
    <span>Three</span>
  </div>
  <a href="http://b.com">B</a>
</body></html>
'''

【填写区】
# ===== 代码区 start =====
from bs4 import BeautifulSoup

# 1. 找出所有 class="pic" 的 <img> 标签，输出它们的 src
#img_tags = BeautifulSoup(html, "lxml").find_all("img", class_="pic")
# for img_tag in img_tags:
#     print(img_tag["src"])
#
# 2. 查找所有带 href 的 <a> 标签，输出其文本和 href 
# a_tags = BeautifulSoup(html, "lxml").find_all("a", href=True)
# for a_tag in a_tags:
#     print(a_tag.text, a_tag["href"])
#
# 3. id=main 的 <div> 下所有 <span> 元素文本（用 CSS selector）
# select 方法用于通过 CSS 选择器选中满足条件的标签。例如，下面的代码查找 id="main" 的 <div> 下所有 <span> 标签：
# span_tags = BeautifulSoup(html, "lxml").select("#main span")
# for span_tag in span_tags:
#     print(span_tag.text)
#
# ===== 代码区 end =====
"""
