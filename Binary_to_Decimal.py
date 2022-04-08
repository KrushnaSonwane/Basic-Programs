from dbm import dumb


n = int(input("Enter Binary number: "))
a = []
i = 0
d_num = 1
flag = 0
result = 0
while n != 0:
    num = n % 10
    n = int(n / 10)
    if num >= 2:
        flag = 1
    if num == 1 and i == 0:
        result = 1
    if i > 0:
        d_num = d_num * 2
        if num == 1:
            result = result + d_num
    i += 1
if flag == 1:
    print("Please enter valid binary number..!!")
else:print(result)