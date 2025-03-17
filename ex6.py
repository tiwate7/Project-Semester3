#Calculate factorial of a number by for loop
#Author:ZhengZhongxing
n=int(input("Enter a number:"))
def factorial(n):
    result = 1
    for i in range(2,n+1):
        result*=i  
    return result

print(factorial(n))

