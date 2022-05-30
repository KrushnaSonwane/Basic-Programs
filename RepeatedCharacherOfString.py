string = input("Enter your string: ")
dup = []
print("Repeated charachers of String(s) is/are: ",end="")
for i in string:
    if i not in dup:
        dup.append(i)
    else:
        print(i, end="")
