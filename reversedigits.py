x = int(input("What's x? "))
sum = 0
while (x>0):
    z = x%10
    sum = sum * 10 + z
    x = x//10
print(sum)