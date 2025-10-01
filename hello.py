def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


number = int(input("Enter Any Number: "))
print(f"Factorial of {number} is: {factorial(number)}")