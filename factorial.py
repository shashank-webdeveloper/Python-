def factorial_loop(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial_loop(num)}")
