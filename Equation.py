#create three variables to store user input

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a third number: "))

#find the Quadratic Equation roots

root1 = 0
root2 = 0

d = (b**2) - (4*a*c)

root1 = (-b + d**0.5) / (2*a)
root2 = (-b - d**0.5) / (2*a)
print(f"The roots of the equation are: {root1} and {root2}")
