"""
1. Write a Python program that asks the user for two numbers and prints:

Sum
Difference
Product
Quotient

2. Ask the user for their age, and print:

"You are eligible to vote" if age >= 18

Otherwise "You are not eligible to vote"
"""
num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 % num2)


print(40 * "*")
print("Task 2")
print(40 * "*")

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("Not eligible")




