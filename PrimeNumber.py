n = int(input("Enter any number: "))
if n % 2 == 0:
    print(f"{n} is not a prime number")
else:
    for i in range(2, int((n/2) + 1)):
        if n % i == 0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is prime number")
        