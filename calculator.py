x = float(input("X? "))
y = float(input("Y? "))
operation = input("Operation? ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
elif operation == "%":
    print(x % y)
elif operation == "//":
    print(x // y)
else:
    print("Error! please enter a valid operator.")

