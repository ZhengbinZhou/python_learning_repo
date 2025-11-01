"""
作业四：HTML 美化与编码

【题目说明】
参考 lesson10_bs4_prettify.py，完成下列任务：
1. 对下方 html 字符串进行美化（prettify），打印出缩进后的内容（前 100 个字符即可）。
2. 提取纯文本内容，用 get_text 输出（去除所有 HTML 标签）。
3. 将格式化后的 HTML 以 UTF-8 字节写入 output_homework_utf8.html，并将纯文本写入 output_homework.txt。
4. 试用 encode/decode API，将原 HTML 字节内容解码回字符串并简单核对前缀。



【填写区】

"""
# ===== 代码区 start =====
from bs4 import BeautifulSoup

html = '''
<html><head><title>作业4</title></head><body>Hi <span>hello<b>world</b></span> &copy;</body></html>
'''
# 请在此完成全部任务
# 1. 使用 html.parser 或 lxml 均可
soup = BeautifulSoup(html, "html.parser")

# 1) 美化（prettify），只打印前 100 字符
pretty = soup.prettify()
print("--- 1) 美化前100字符 ---\n", pretty[:100], "...\n")

# 2) 提取纯文本内容
plain_text = soup.get_text(strip=True)
print("--- 2) 纯文本 ---\n", plain_text, "\n")

# 3) 格式化后的 HTML 写入 UTF-8，纯文本写入 txt
with open("output_homework_utf8.html", "wb") as f:
    f.write(pretty.encode("utf-8"))
with open("output_homework.txt", "w", encoding="utf-8") as f:
    f.write(plain_text)
print("已写出: output_homework_utf8.html, output_homework.txt\n")

# 4) encode/decode API 测试
html_bytes = html.encode("utf-8")
decoded = html_bytes.decode("utf-8")
print("--- 4) encode/decode ---")
print("原html前缀:", html[:30])
print("解码html前缀:", decoded[:30])
print("一致?", html[:30] == decoded[:30])
# ===== 代码区 end =====

