content = True
i = 1
with open("C:\\Users\\HP\\Desktop\\Python Programs\\sampl.txt") as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line number {i}")
        i += 1 

# To delete using python
import os
data = 'C:\\Users\\HP\\Desktop\\Python Programs\\sampl.txt'
os.remove(data)