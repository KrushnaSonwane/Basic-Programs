sentence = input("Enter your sentence: ")
# print(sent[4:1:-1])  hsu
words = []
count = 0
for i in range(0, len(sentence)):
    if sentence[i] == " ":
        words.append(sentence[count:i:])
        count = i+1
else:
    words.append(sentence[count::])

for i in words:
    print(i[::-1], end=" ")