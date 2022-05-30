str = input("Enter your string: ")
count = 0
flag = 0
for i in str:
    for j in str:
        if i == j:
            count += 1
    else:
        if count == 1:
            print(f"First non-repeated characher is: '{i}'")
            flag = 1
        else:
            count = 0
    
    if flag == 1:
        break
else:
    print("Sorry, Each character is reapeated..!")