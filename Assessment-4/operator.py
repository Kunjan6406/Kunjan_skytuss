# Python Program for All 10 Questions

# 1. Calculate the remainder of two numbers
print("1. Calculate the remainder of two numbers")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Remainder =", num1 % num2)

print("\n----------------------------")

# 2. Check if a number is even or odd
print("2. Check if a number is even or odd")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

print("\n----------------------------")

# 3. Compare two numbers and print the larger one
print("3. Compare two numbers")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("Larger number is:", num1)
elif num2 > num1:
    print("Larger number is:", num2)
else:
    print("Both numbers are equal.")

print("\n----------------------------")

# 4. Calculate the square and cube of a number
print("4. Square and Cube of a number")
num = int(input("Enter a number: "))
print("Square =", num ** 2)
print("Cube =", num ** 3)

print("\n----------------------------")

# 5. Check if two entered numbers are equal
print("5. Check if two numbers are equal")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 == num2:
    print("Numbers are equal.")
else:
    print("Numbers are not equal.")

print("\n----------------------------")

# 6. Print True if both numbers are positive, else False
print("6. Check if both numbers are positive")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1 > 0 and num2 > 0)

print("\n----------------------------")

# 7. Convert float to integer
print("7. Convert float to integer")
num = float(input("Enter a float number: "))
print("Integer value =", int(num))

print("\n----------------------------")

# 8. Take a number as a string, convert to int, and multiply by 10
print("8. String to Integer and Multiply by 10")
num = input("Enter a number: ")
print("Result =", int(num) * 10)

print("\n----------------------------")

# 9. Use and & or operators to check multiple conditions
print("9. Check multiple conditions using and/or")
age = int(input("Enter age: "))
salary = int(input("Enter salary: "))

if (age >= 18 and salary >= 20000) or age >= 60:
    print("Condition is True")
else:
    print("Condition is False")

print("\n----------------------------")

# 10. Divide two numbers and print quotient and remainder
print("10. Quotient and Remainder")
num1 = int(input("Enter dividend: "))
num2 = int(input("Enter divisor: "))
print("Quotient =", num1 // num2)
print("Remainder =", num1 % num2)