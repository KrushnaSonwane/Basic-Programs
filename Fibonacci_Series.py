n = int(input("Enter any number: "))
num1 = 0
num2 = 1
num3 = 0
for i in range(0, n):
    num3 = num1 + num2
    print(f"{num1} + {num2} = {num3}")
    num1 = num2
    num2 = num3