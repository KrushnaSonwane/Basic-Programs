roman_str = str(input("Enter you roman number: "))
int_num = 0
flag = 0
num = 0
for i in roman_str:
    if flag == 1:
        if i == 'X':
            num = num + 8
            flag = 0
        elif i == 'V':
            num = num + 3
            flag = 0
        else:
            num = num + 1
    elif i == 'X':
        int_num = int_num + 10
    elif i == 'V':
        int_num = int_num + 5
    elif i == 'I': 
        num = num + 1
        flag = 1
    else:
        print("Print enter valid roman..!")
        break
else:
    int_num = int_num + num
print(int_num)