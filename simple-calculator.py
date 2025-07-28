# Simple Calculator Program

# Welcome message
print("Simple Calculator")
print("Enter two numbers and an operation (+, -, *, /)")

# Get all inputs at once
number1 = float(input("First number: "))
number2 = float(input("Second number: "))
operation = input("Operation (+, -, *, /): ")

# Calculate result
if operation == '+':
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '*':
    result = number1 * number2
elif operation == '/':
    if number2 == 0:
        print("Error! Can't divide by zero!")
        exit()  # Stop the program if dividing by zero
    result = number1 / number2
else:
    print("Error! Invalid operation!")
    exit()  # Stop the program if invalid operation

# Show the calculation
print(f"\nCalculation: {number1} {operation} {number2} = {result}")
