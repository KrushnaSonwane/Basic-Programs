n = int(input("Enter a number: "))
reverse_num = 0
count = 1
while n != 0:
    mod = n % 10
    n = int(n / 10)
    if count == 1:
        reverse_num = mod
    else:
        reverse_num = (reverse_num * 10) + mod 
    count += 1
print(reverse_num)