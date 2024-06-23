#Methods:
name = input("Enter a username: ").strip().capitalize().title()
# Strip: removes spaces from left and right of an input.
# Capitalize: capitalises the first letter of the first word.
# Title: capitalises the first letter of all words.

#Split(): Splits a string into two smaller substrings leveraging the space in between.
first, last = name.split()
print(f"Hello, {first}")
