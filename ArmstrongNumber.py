n =  int(input("\nEnter a number: "))
count = 0
temp_n = n
digit_list = []
while temp_n != 0:
    digit_list.append(temp_n % 10)
    temp_n = int(temp_n / 10)

for i in range(0, len(digit_list)):
    m = digit_list[i]
    for j in range(1, len(digit_list)):
        m = m * digit_list[i]
    else:
        temp_n = temp_n + m
if temp_n == n:
    print(f"{n} is Armstrong number..\n")
else:
    print(f"Sorry,\n{n} is not Armstrong number!\n")