# Can also open file like above
with open("C:\\Users\\HP\\Desktop\\Python Programs\\sampl.txt") as f:
    f.write('it also work')

# # 'r' to read file
f = open("C:\\Users\\HP\\Desktop\\Python Programs\\sampl.txt", 'r')
dat = f.read()
print(dat)
f.close()

# #  'w' to wite in file and data will be overridden
f = open("C:\\Users\\HP\\Desktop\\Python Programs\\sampl.txt", 'w')
dat = f.write("Hello, i am krushna")
f.close()

# # 'a' to append the data at the end, it will not overridden
f = open("C:\\Users\\HP\\Desktop\\Python Programs\\sampl.txt", 'a')
dat = f.write("\ni am a good boy xD")
f.close()

# 'r+' to read and write in file, data in the file will not be deleted
with open("C:\\Users\\HP\\Desktop\\Python Programs\\sampl.txt", 'r+') as f:
    print(f.read())
    f.write("I am last line\n")
    # not reding data
    # f.write("I am last line\n")
    # print(f.read())
    f.close()

# 'w+' to write and read data, it will override existing data
with open("C:\\Users\\HP\\Desktop\\Python Programs\\sampl.txt", 'w+') as f:
    f.write("I am line\n")

# 'a+' to append and read from the file, it will not override existing data
f = open("C:\\Users\\HP\\Desktop\\Python Programs\\sampl.txt", 'a+')
f.write("I am line\n")
f.close()