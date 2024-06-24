x = int(input("What's x? "))
y = int(input("What's y? "))

if x>y:
    print("x is greater than y.")
elif x<y:
    print("x is less than y.")
else:
    print("x is equal to y.")

def grade(n):
    if n >= 90:
        print("A")
    elif n >= 80:
        print("B")
    elif n >= 70:
        print("C")
    else:
        print("D")

score = int(input("Score? "))
grade(score)