#Judge tichet price by age
#Author:ZhengZhongxing
age = input("Enter your age: ")

if int(age) <= 19:
   print("You qualify for student discounts.")
elif 20 <= int(age) <= 54:
   print("You qualify for no age discounts.")
else:
   print("You can receive senior discounts.")
