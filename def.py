def main():
    def hello(to):
        print("hello, ", to)    
    name = input("What's your name? ")
    hello(name)
    
    def squared(n):
        print(n * n)
    
    square = int(input("Give me another one, i'll square it for you. "))
    squared(square)

main()    