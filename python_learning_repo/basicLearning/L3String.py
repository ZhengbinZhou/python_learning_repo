'''
字符串类型
'''

s="This is a programme"
print(s[0])  # 输出第一个字符
print(s[2])  # 输出第三个字符
print(s[-1])  # 输出最后一个字符
print(s[:3])  # 输出前三个字符
print(s[-3:])  # 输出倒数三个字符
print(s[2:8:2])  # 输出从第3个字符开始到第八个字符，每隔一个字符取一个
print(s)
print(s[:-1])  # 输出除最后一个字符外的所有字符
print(s.find("a"))
print(s.count("a"))
print(s.replace(" ",","))
print(s.upper())
print(s+" is a good programme")  # 字符串拼接
print(s>"this is a book")  # 字符串比较
print(s*3)  # 字符串重复三次
print(s.find("i"))
print(s.split(" "))


