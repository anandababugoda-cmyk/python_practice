
print("Welcome to Palindrome Checker!")

word = input("Computer: Enter a word: ")

print("Computer: Checking your word...")

reverse = word[::-1]

print("Computer: Original Word:", word)
print("Computer: Reverse Word:", reverse)

if word.lower() == reverse.lower():
    print("Computer: Great! It is a Palindrome.")
else:
    print("Computer: Sorry! It is not a Palindrome.")
