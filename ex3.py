#Guess a random number
#Author:ZhengZhongxing
import random
number=random.randint(10,20)
print(number)

found=False

while not found:
   x=input("Enter a number between 10 and 20:")
   if int(x)==number:
      found=True
      print("Congratulations!")
   else:
      print("Please try again.")

