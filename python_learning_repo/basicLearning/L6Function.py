"""
函数
"""

# 求exp(x)的值
def fact(n):
    result = 1
    for i in range(1, n + 1):
        if i == 1:
            result = 1
        else:
            result *= i
    return result

def exp(x, n=1):
    result = 0
    for i in range(n + 1):
        result += (x ** i) / fact(i)
    return result
if __name__ == "__main__":
    print(exp(10, 5))