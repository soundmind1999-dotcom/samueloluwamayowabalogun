text = input("Enter a string: ")

vowels = 0
consonants = 0

text = text.lower()

for ch in text:
    if 'a' <= ch <= 'z':
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            vowels += 1
        else:
            consonants += 1

print("The number of vowels is", vowels)
print("The number of consonants is", consonants)
