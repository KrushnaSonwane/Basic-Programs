l=[1,2,3,4,5,6]
l.append(9)
print(l)
l.extend([10,11,12])
print(l)
print(['krushna']*2)
l.insert(1,11)
print(l)
l[1:4]=[7,8]
print(l)
l.pop(2)
print(l)
print(len(l))
print(max(l))
print(min(l))
print(l.index(7))
print(l.count(11))
l[0:3]=[1,1,1]
print(l)
print(l.count(1))
print(l.sort())
del l[0:3]
print(l)
l.reverse()
print(l)
l.sort()
print(l)
ll=['k','r','i','s','h']
print(ll)
print("i" in ll)
print("z" not in ll )



#list in for loop

for i in('cricket','holliball','batmintan'):
    print("i like to play ",i)
