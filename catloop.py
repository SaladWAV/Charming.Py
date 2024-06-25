while True:
    cat = int(input("How many meows? "))
    if cat > 0:
        break
# This loop is simply so to prevent the user giving 0/negative input to the question.
# It will keep asking the question until the input is positive.

for _ in range(cat):
    print("meow")
# Then using a for loop we'll print the number of meows in the range of the input.