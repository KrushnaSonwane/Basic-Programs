n = int(input("Enter any number: "))
k = n
def palindrome(n):
        # flag = 0
        # if n < 0:           # Commented logic is for negative number 
        #     n = abs(n)
        #     flag = 1
        i = 1
        while n != 0:
            mod = n % 10
            if i == 1:
                total = mod
            n = int(n / 10)
            if i >= 2:
                total = (total * 10) + mod
            i += 1
        # if flag == 1:
        #     total = 0 - total 
        return total
x = palindrome(n)

while k != x:
        n = x + k
        k = n
        palindrome(n)
        x = palindrome(n)
print(f"{x}")
