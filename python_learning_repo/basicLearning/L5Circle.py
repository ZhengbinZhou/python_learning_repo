"""
循环结构
"""
#编写程序,利用for循环实现输入正整数,求1到该数的和
# n = eval (input("Please input a positive integer: "))
# sum = 0
# for i in range(n):
#     sum +=i
# print(sum)

# 猜数游戏,0-100之间的数
import random
count = 5
number= random.randint(0, 100)
guess = int(input("Please input a positive integer: "))
while guess !=number and count != 0:
    count -= 1
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    guess = int(input("Please input a positive integer: "))
if count!=0:
    print("Congratulations! You guessed the number {}.".format(number))
else:
    print("Sorry, you have no more chances. The number was {}.".format(number))