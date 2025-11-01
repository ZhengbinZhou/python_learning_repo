from bs4 import BeautifulSoup, FeatureNotFound

# 简要对比：
# - html.parser：自带，速度中等，零依赖
# - lxml（HTML）：快且稳，需要安装 lxml
# - lxml-xml（XML）：严格 XML 解析，用于 XML/RSS/SVG
# - html5lib：容错最强，最接近浏览器 DOM，较慢

html = "<div><p>Hi<a>link"

parsers = [
    "html.parser",
    "lxml",
    "lxml-xml",
    "html5lib",
]

need_pkg = {"lxml": "lxml", "lxml-xml": "lxml", "html5lib": "html5lib"}

for parser in parsers:
    try:
        soup = BeautifulSoup(html, parser)
        a = soup.find("a")
        # 打印：解析器名、是否找到 <a>、截断后的 <a> 标签
        print(parser, bool(a), (str(a)[:60] if a else ""))
    except FeatureNotFound:
        pkg = need_pkg.get(parser)
        if pkg:
            print(f"{parser} 未安装，请先安装：pip install {pkg}")
        else:
            print(f"{parser} 不可用")
#BeautifulSoup4的解析器