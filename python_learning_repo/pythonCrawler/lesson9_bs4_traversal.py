from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <ul id="nav">
      <li class="item"><a href="/home">Home</a></li>
      <li class="item"><a href="/about">About</a></li>
      <li class="item"><a href="/contact">Contact</a></li>
    </ul>
    <div id="content">
      <h1>Title</h1>
      <p class="lead">Intro <b>bold</b> text.</p>
      <p>Paragraph <span>with <i>inline</i></span></p>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# 定位基准节点
nav = soup.find("ul", id="nav")
about_li = nav.find_all("li")[1]
content_div = soup.find("div", id="content")

print("=== 向下遍历: children / descendants ===")
print("children (直接子节点标签，不含更深层):", [c.name for c in nav.find_all(recursive=False)])
print("descendants (所有后代标签):", [d.name for d in nav.descendants if getattr(d, "name", None)])
print()

print("=== 向上遍历: parent / parents ===")
print("parent (上一层标签):", about_li.parent.name)
print("parents (所有祖先，取前3个):", [p.name for p in list(about_li.parents)[:3]])
print()

print("=== 兄弟节点: next_sibling / previous_sibling ===")
# 注意: 直接使用 next_sibling 可能得到换行符，使用 find_next_sibling 可跳过空白
print("raw next_sibling is tag?", getattr(about_li.next_sibling, "name", type(about_li.next_sibling)))
print("next element sibling tag:", about_li.find_next_sibling().a.get_text())
print("previous element sibling tag:", about_li.find_previous_sibling().a.get_text())
print()

print("=== 文档顺序遍历: next_elements / previous_elements ===")
# 取 about_li 的下一个元素们中的前5个，显示其类型/名字或文本摘要
next_elems = []
for e in about_li.next_elements:
    label = e.name if getattr(e, "name", None) else str(e).strip()
    if label:
        next_elems.append(label[:20])
    if len(next_elems) >= 5:
        break
print("next_elements(5):", next_elems)

prev_elems = []
for e in about_li.previous_elements:
    label = e.name if getattr(e, "name", None) else str(e).strip()
    if label:
        prev_elems.append(label[:20])
    if len(prev_elems) >= 5:
        break
print("previous_elements(5):", prev_elems)
print()

print("=== 查找 API: find / find_all / find_next_* / find_previous_* ===")
print("find(tag):", content_div.find("p").get_text())
print("find_all(tag, class):", [p.get_text() for p in content_div.find_all("p", class_="lead")])
print("find_next(tag) from <h1>:", content_div.h1.find_next("p").get_text())
print("find_previous(tag) from 第二个 <p>:", content_div.find_all("p")[1].find_previous("h1").get_text())
print("find_next_sibling(tag) on <li> About →", about_li.find_next_sibling("li").a.get_text())
print("find_previous_sibling(tag) on <li> About →", about_li.find_previous_sibling("li").a.get_text())

#
