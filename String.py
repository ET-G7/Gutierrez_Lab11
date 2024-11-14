# 10 word inputs
wordList = []
for i in range (1,11):
        word = str(input(f"Type in a word ({i}/10): "))
        wordList.append(word)

wordLengthDisplay = int(input("Enter the minimum word length: "))

for word in wordList:
    if len(word) >= wordLengthDisplay:
        print(word)
    
    