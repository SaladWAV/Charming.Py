def main():

    def meow(times):
        for _ in range(times):
            print("Meow")

    n = int(input("How many meows? "))
    meow(n)

main()    