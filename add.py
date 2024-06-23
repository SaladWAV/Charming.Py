# simple addition calculator.
# 'int' can be replaced with 'float' for decimal point values.
x = int(input("Value of X? "))
y = int(input("Value of Y? "))
print(x + y)

# round(x + y, 2) to round the output to the specfic place after the decimal point.

# adds commas to big numbers with ":," inside the f-string brackets.
print(f"{x + y:,}")

# Alternative of round function, specify the no. of digits to print using an f-string.
print(f"{x + y:.2f}")