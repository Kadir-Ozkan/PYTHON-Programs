#LetterCounter.py

text = input("Please enter a text to get the number of repetations of the characters: ")
for i in text:
    l = [text.count(i) for i in text]
counts = zip(text, l)
print(dict(counts))