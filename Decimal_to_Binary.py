n = int(input("Enter Decimal Number: "))
a = []
while n != 0:
    b_num = n % 2
    n = int(n / 2)
    a.append(b_num)
for i in range(len(a)-1, -1, -1):
    print(a[i], end=" ")