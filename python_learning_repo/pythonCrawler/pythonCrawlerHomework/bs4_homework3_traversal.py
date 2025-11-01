"""
作业三：BeautifulSoup 文档结构遍历

【题目说明】
参考 lesson9_bs4_traversal.py，完成下列任务：

html = '''
<html><body>
  <ul id="nav">
    <li class="item"><a href="/">首页</a></li>
    <li class="item"><a href="/about">关于</a></li>
    <li class="item"><a href="/contact">联系</a></li>
  </ul>
  <div id="main">
    <h2>标题</h2>
    <p class="desc">Here is <b>desc</b></p>
    <p>正文段落<span>内嵌<span>二级</span></span></p>
  </div>
</body></html>
'''

1. 找到 class 为 item 的第二个 <li> 标签（即“关于”）
2. 输出其父节点的标签名。
3. 输出其下一个兄弟节点（next_sibling）和上一个兄弟节点（previous_sibling）中 <a> 的内容。
4. 遍历 main <div> 内所有 <span>，打印它们的层级文本。
5. 列举第二个 <li> 所有祖先标签名。

【填写区】
# ===== 代码区 start =====
from bs4 import BeautifulSoup

# 在此补全你的代码
soup = BeautifulSoup(html, "lxml")
target_tag = soup.find.next_sibling("li", class_="item")
print(target_tag.parent.name)
print(target_tag.next_sibling.a.text)
print(target_tag.previous_sibling.a.text)
for span_tag in soup.find("div", id="main").find_all("span"):
  print(span_tag.get_text())
print([p.name for p in target_tag.parents if p is not None])
# ===== 代码区 end =====
"""
