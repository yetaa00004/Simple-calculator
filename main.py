import math

num1 = float(input("Enter a number "))
User_Interaction = input("what do you want to do, + or - or * or / ? ")
num2 = float(input("Enter the other number "))

if User_Interaction == "+":
    print(num1 + num2)
elif User_Interaction == "-":
    print(num1 - num2)
elif User_Interaction == "*":
    print(num1 * num2)
elif User_Interaction == "/":
    print(num1 / num2)
else:
    print("Invalid Opertation!")