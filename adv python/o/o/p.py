import re

# Accept input from user
word = input("Enter a word: ")

# Pattern: 3-letter words like cat, cot, cut, mat, met, mud
pattern = r'^[cm][aeiou]t|mud$'

# Check using regex
if re.fullmatch(pattern, word):
    print("Valid word")
else:
    print("Invalid word")
