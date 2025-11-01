'''
熟悉python开发环境
使用turtle库绘制正方形和正六边形
'''


# a=eval(input("Please input a number: "))
# b=eval(input("Please input another number: "))
# s=a+b
# print("{} + {} = {}".format(a,b,s))

import turtle as t
t.pensize(2)
t.setup(650,350,200,200)
for i in range(4):
    t.fd(150)
    t.left(90)

for i in range(6):
    t.fd(150)
    t.left(60)
t.done()