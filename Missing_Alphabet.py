name = input("Enter any name: ")
chr = input("Enter characher: ")
for i in range(0, len(name)):
    if name[i] == chr:
        continue
    else:
        print(name[i], end="")