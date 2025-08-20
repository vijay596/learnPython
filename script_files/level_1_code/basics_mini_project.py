# -----------------------------
# Python Basics Mini Project
# -----------------------------

# Welcome message
print("Welcome to the Python Basics Program!")

# User Info Section
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

print(f"My name is {name}, I am {age} years old, and I live in {city}.")
print(type(name))
print(type(age))
print(type(city))

print("\n", 40 * "*")
print("Task 1: Arithmetic Operations")
print(40 * "*")

# Arithmetic Operations Section
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)       # Division
print("Floor Quotient:", num1 // num2) # Floor Division
print("Remainder:", num1 % num2)       # Modulus
print("Power:", num1 ** num2)          # Exponent

print("\n", 40 * "*")
print("Task 2: Eligibility Check")
print(40 * "*")

# Eligibility Check Section
if age >= 18 and age < 60:
    print("You are eligible to work.")
elif age >= 60:
    print("You are a senior citizen.")
else:
    print("You are not eligible to work.")

# Final Message
print("\nThank you for using the program!")
