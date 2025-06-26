# Simple Calculator
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
#Choose operation for calculation
print("+ for Addition")
print("- for Subtraction")
print("* for multiplication")
print("/ for division")
operation = input("Enter operation:")
if operation == '+':
    print("Result:",a+b)
elif operation =='-':
    print("Result:",a-b)
elif operation =='*':
    print("Result:",a*b)
elif operation =='/':
    print("Result:",a/b)
else:
    print("Invalid Operation")
