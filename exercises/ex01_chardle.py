"""EX01 - Chardle - A cute step toward Wordle!"""

__author__ = "730325236"

word: str = input("Enter a 5-character word: ")

if len(word) != int(5):
    exit(print("Error: Word must contain 5 characters"))

letter: str = input("Enter a single character: ")

if len(letter) != int(1):
    exit(print("Error: Character must be a single character."))

num: int = 0

print("Searching for " + letter + " in " + word)

if word[0] == letter:
    print(letter + " found at index 0")
    num = num + 1
if word[1] == letter:
    print(letter + " found at index 1")
    num = num + 1
if word[2] == letter:
    print(letter + " found at index 2")
    num = num + 1
if word[3] == letter:
    print(letter + " found at index 3")
    num = num + 1
if word[4] == letter:
    print(letter + " found at index 4")
    num = num + 1

if num == 0:
    print("No instances of " + letter + " found in " + word)
else:
    if num == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(num) + " instances of " + letter + " found in " + word)
    
    