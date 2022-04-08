s = input("Enter your string: ")
lenght = int(input("Enter lengh of string: "))
pal_str = ''
count = 0
for i in range(0, lenght):
    if s[i] == ' ':
        if pal_str == pal_str[::-1]:
            count += 1            
        pal_str = ''
    else:
        pal_str = pal_str + s[i]
else:
    if pal_str == pal_str[::-1]:
           count += 1
print("output : ", count)