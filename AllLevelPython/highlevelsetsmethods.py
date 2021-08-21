a = {"a","b","c"}
print(type(a))

b = set()
print(type(b))

c = {1,2,3,1,1,1,2,2,7,8,9,9,9}
print(c)

d = {"Bugün hava güzel"}
print(d)

f = set("Python programlama dili")
print(f)

g = {"ocak","şubat","mart"}
print(g)

x = {"Ahmet","Mehmet","Ali"}
print(x)

for i in x:
    print(i)
liste = list(x)
print(type(x))

x = {4,8,12}
x.add(16)
x.add(4)
x.add(12)
print(x)

a = {5,10,44,5,67,24,99,40}
b = {2,10,44,67,11,34,77}
#print(b.difference(a))
a.difference_update(b)
print(a)

a = {5,10,44,5,67,24,99,40}
a.discard(99)
print(a)

a = {5,10,44,5,67,24,99,40}
b = {2,10,44,67,11,34,77}
a.intersection(b)
print(a)
print(b)