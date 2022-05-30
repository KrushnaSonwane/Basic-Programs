print("Enter your email: ", end="")
a = []
flag = 0
a = input()
for i in range(0, len(a)):
    if(a[i] == '@'):
        flag = flag + 1
    if(a[i] == '#' or a[i] == '$' or a[i] == '%' or a[i] == '^' or a[i] == '*' or a[i] == '(' or a[i] == ')' or a[i] == '!' or a[i] == '&' or a[i] == '-'):
        flag = 0

if(flag == 1):
    x = a.index('@')
    print("Domain name : ", end = "")
    for i in range(x+1, len(a)):
        print(a[i], end = "")
else:
    print("invalid email")
