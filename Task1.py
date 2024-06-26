# Write a Python program that prints the string "Hello Python" to the console.
print("Hello Python")

# Write a Python program that performs addition, subtraction, multiplication, and division of two numbers input by the user.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
if num2 != 0:
    division = num1 / num2
else:
    division = "Division by zero is not allowed"
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# Write a Python program to generate and print a random number between a specified range.
import random
start = int(input("Enter the start number: "))
end = int(input("Enter the end number : "))
random_number = random.randint(start, end)
print("Random number:", random_number)

# Write a Python program to display the calendar of a given month and year.
import calendar
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
print(calendar.month(year, month))

# Write a Python program to check if a given year is a leap year.
year = int(input("Enter the year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# Write a Python program to print all prime numbers within a specified range.
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
print("Prime numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

# Write a Python program to find the factorial of a number input by the user.
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "is", factorial)

# Write a Python program to print the Fibonacci sequence up to a specified number of terms.
terms = int(input("Enter the number of terms: "))
n1, n2 = 0, 1
count = 0
if terms <= 0:
    print("Please enter a positive integer")
elif terms == 1:
    print("Fibonacci sequence upto", terms, "terms:")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


# Write a Python program to find all Armstrong numbers within a specified range.
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
print("Armstrong numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)

# Write a Python program to print the reverse of a string input by the user.
string = input("Enter a string: ")
reverse_string = string[::-1]
print("Reverse of the string:", reverse_string)

# Write a Python program to calculate and print the sum of the first ten natural numbers.
sum = 0
for i in range(1, 11):
    sum += i
print("Sum of the first ten natural numbers:", sum)
