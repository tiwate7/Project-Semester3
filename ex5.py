#Calculate factorial of a number by while loop
#Author:ZhengZhongxing
n=int(input("Enter a number:"))
def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(factorial(n))
