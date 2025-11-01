from bs4 import BeautifulSoup
from bs4.element import NavigableString, Comment, Doctype

html = """<!DOCTYPE html>
<!-- page head comment -->
<html>
  <head><title>Demo</title></head>
  <body>
    <div id="box" class="c1 c2" data-x="42">
      Hello <span>world</span>!
      <!-- inline comment -->
    </div>
  </body>
</html>
"""

# 1) BeautifulSoup：整棵文档树的根对象
soup = BeautifulSoup(html, "lxml")
print("[BeautifulSoup] type:", type(soup))
print("[BeautifulSoup] children count:", len(list(soup.children))) #len function return the length of the list
print("[BeautifulSoup] first 50 chars:", str(soup)[:50]) #str function return the string of the soup
print()

# 2) Tag：HTML/XML 标签节点（可有属性/子节点）
div_tag = soup.find("div", id="box") #find function return the tag of the div tag for example <div id="box" class="c1 c2" data-x="42">, etc.
print("[Tag] type:", type(div_tag))
print("[Tag] name:", div_tag.name)
print("[Tag] attrs dict:", div_tag.attrs) #attrs function return the attributes of the tag for example id, class, data-x, etc.
print("[Tag] get class list:", div_tag.get("class")) #get function return the class of the tag for example c1, c2, etc.
print("[Tag] select span text:", div_tag.span.get_text()) #get_text function return the text of the span tag for example world, etc.
print()

# 3) NavigableString：标签内的文本节点（纯文本）
text_nodes = [n for n in div_tag.children if isinstance(n, NavigableString)]
print("[NavigableString] count in <div>:", len(text_nodes))
for i, node in enumerate(text_nodes, 1):
    print(f"  #{i}", repr(node.strip()))
print()

# 4) Comment：HTML 注释节点（NavigableString 的子类）
comments = soup.find_all(string=lambda x: isinstance(x, Comment))
print("[Comment] count:", len(comments))
for i, c in enumerate(comments, 1):
    print(f"  #{i}", repr(c))
print()

# 5) Doctype：文档类型声明（根节点的直接子节点之一）
doctype_nodes = [n for n in soup.contents if isinstance(n, Doctype)]
print("[Doctype] count:", len(doctype_nodes))
for i, d in enumerate(doctype_nodes, 1):
    print(f"  #{i}", repr(d))

'''
fing function is used to find the tag of the html document for example <div id="box" class="c1 c2" data-x="42">, etc.
find_all function is used to find all the tags of the html document for example <div id="box" class="c1 c2" data-x="42">, etc.
'''

