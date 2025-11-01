'''
python基础问题
'''

# 华氏度和摄氏度转换
# fahrenheit = eval(input("Please input a temperature in Fahrenheit: "))
# celsius = (fahrenheit -32)/1.8
# print("{:.2f} degrees Celsius is equal to {:.2f} degrees Fahrenheit.".format(celsius,fahrenheit))

# 计算一个三位数的各位数字
x=eval(input("Please input a number with 3 digits: "))
a=x//100
b=(x%100)//10
c=x%10
print("The hundreds digit is {}, the tens digit is {}, and the units digit is {}.".format(a, b, c))

