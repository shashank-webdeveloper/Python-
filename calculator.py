num1 = int(input("Enter the value1: "))
num2 = int(input("Enter the value2: "))

operator = input("Enter the operator: ")

if (operator=="+"):
    print(f"The Sum of two numbers is: {num1+num2} ")

elif (operator=="-"):
    print(f"The Subtraction of two numbers is: {num1-num2} ")

elif (operator=="*"):
    print(f"The Multiplication of two numbers is: {num1*num2}")

elif (operator=="/"):
    print(f"The Division of two numbers is: {num1/num2}")

else:
    print("Invalid Operator!")
