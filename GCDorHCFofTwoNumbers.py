print("Enter any two numbers: ")
a = int(input())
b = int(input())
x = a
y = b

while True:
    if a > b:
        if a % b == 0:
            print(f"GCD of {x} and {y} is {b}")
            break
        else:
            a = a - b

    elif b > a:
        if b % a == 0:
            print(f"GCD of {x} and {y} is {a}")
            break
        else:
            b = b - a

    else:
        print(f"GCD of {x} and {y} is {a}")
        break