from bs4 import BeautifulSoup

# 主题：HTML 格式化（prettify/formatter）与编码（encode/decode/写文件）

raw_html = """
<html><head><meta charset="utf-8"><title>示例</title></head><body>
<p class='c'>中文 & symbols < & > & © and emoji 😀</p><div><span> A  B  </span></div></body></html>
"""

soup = BeautifulSoup(raw_html, "html.parser")

print("=== 1) prettify：美化缩进，便于阅读 ===")
pretty = soup.prettify()
print(pretty[:200], "...\n")  # 只展示前 200 个字符

print("=== 2) prettify + formatter：控制字符如何转义 ===")
# formatter="html"（默认）：会按 HTML 实体转义特殊字符
print("formatter=html → contains &lt;?", "&lt;" in soup.prettify(formatter="html"))

# formatter=None：尽量原样输出（不再把 < > 转成实体）。注意：这可能破坏 HTML 安全性，仅用于展示或受信内容。
print("formatter=None → contains < ?", "<" in soup.prettify(formatter=None))

# formatter="minimal"：较少转义（例如保留已是实体的部分）
print("formatter=minimal length:", len(soup.prettify(formatter="minimal")))
print()

print("=== 3) 文本与字符串化：get_text / str ===")
print("get_text() 合并纯文本:", soup.get_text(strip=True))
print("str(soup) 压缩成一行:", str(soup)[:120], "...\n")

print("=== 4) 编码：encode / decode ===")
# .encode 指定输出字节编码；formatter 也可用于控制转义
utf8_bytes = soup.encode("utf-8", formatter="html")
gbk_bytes = soup.encode("gbk", errors="ignore")  # 示例：非 UTF-8 编码（丢弃不支持字符）
print("utf-8 bytes size:", len(utf8_bytes))
print("gbk bytes size (errors=ignore):", len(gbk_bytes))

# 从字节解码回字符串
print("decode utf-8 preview:", utf8_bytes.decode("utf-8")[:100], "...\n")

print("=== 5) 写入文件：保持编码 ===")
with open("bs4_out_utf8.html", "wb") as f:
    f.write(utf8_bytes)
print("已写出: bs4_out_utf8.html (UTF-8)")

with open("bs4_out_gbk.html", "wb") as f:
    f.write(gbk_bytes)
print("已写出: bs4_out_gbk.html (GBK, 可能有丢失)")
print()

print("=== 6) original_encoding：解析时推断的原始编码 ===")
print("original_encoding:", soup.original_encoding)

print("=== 7) 片段级 prettify 与 select ===")
p = soup.select_one("p.c")
print(p.prettify())

#
