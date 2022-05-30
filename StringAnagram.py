str1 = input("Enter first String: ")
str2 = input("Enter Second String: ")

if len(str1) == len(str2):
    for i in str1:
        if i not in str2:
            print("Strings are not Anagram..!")
            break
    else:
        for i in str2:
            if i not in str1:
                print("Strings are not Anagram..!")
                break
        else:
            print("Strings are anagram..")
else:
    print("Strings are not Anagram..!")