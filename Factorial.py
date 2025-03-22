print("Factorial of number")
def factorial(num):
    if num==1:
        return 1 # Base case: factorial of 0 and 1 is 1
    return num* factorial(num - 1) # Recursive case


number = int(input("Enter number: "))
print("Factirial of", number, "is", factorial(number))