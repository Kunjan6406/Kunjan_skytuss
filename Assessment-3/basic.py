# =====================================================
# 1. Print your name, age, and city in one line
# =====================================================

name = input("Enter your name: kunjan")
age = input("Enter your age: Patel ")
city = input("Enter your city: Gandevi ")

print(name, age, city)

print("\n" + "=" * 50)


# =====================================================
# 2. Take user input for two numbers and print their sum
# =====================================================

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum =", num1 + num2)

print("\n" + "=" * 50)


# =====================================================
# 3. Convert temperature from Celsius to Fahrenheit
# Formula: (C × 9/5) + 32
# =====================================================

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit =", fahrenheit)

print("\n" + "=" * 50)


# =====================================================
# 4. Store your name in a variable and print it in uppercase
# =====================================================

name = input("Enter your name: ")

print("Uppercase Name =", name.upper())

print("\n" + "=" * 50)


# =====================================================
# 5. Ask the user for their birth year and calculate age
# =====================================================

birth_year = int(input("Enter your birth year: "))
current_year = 2025

age = current_year - birth_year

print("Your age is:", age)

print("\n" + "=" * 50)


# =====================================================
# 6. Swap the values of two variables
# =====================================================

a = input("Enter first value: ")
b = input("Enter second value: ")

print("Before Swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After Swapping:")
print("a =", a)
print("b =", b)

print("\n" + "=" * 50)


# =====================================================
# 7. Calculate the area of a rectangle
# Formula: Length × Width
# =====================================================

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area of Rectangle =", area)

print("\n" + "=" * 50)


# =====================================================
# 8. Check if a number is positive or negative
# =====================================================

num = float(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("The number is Zero")

print("\n" + "=" * 50)


# =====================================================
# 9. Ask for two numbers and print their average
# Formula: (num1 + num2) / 2
# =====================================================

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

average = (num1 + num2) / 2

print("Average =", average)

print("\n" + "=" * 50)