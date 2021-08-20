a = ["a","b","c"]
print("d" in a)
print("b"in a)

liste = [1,2,3,4,5]
for b in liste:
    print(b)

çarpım = 1
liste2 = [1,2,3,4,5]
for i in liste2:
    çarpım = çarpım * i
    print(çarpım)

toplam = 0
liste3 = [1,2,3,4,5,6,7,8,9,10]
for j in liste3:
    toplam = toplam + j
    print(toplam)

liste4 = [44,84,77,33,21,65,2,5]
for i in liste4:
    if i % 2 == 1:
        print(i)

a = "ahmet"
for i in a:
    print(i)

liste5 = [1,2,3]
for i in liste5:
    print(i*2)

demet = (1,2,3,4,5)
for a in demet:
    print(a)

liste6 = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in liste6:
    print("a:{} b:{} c:{}".format(a,b,c))

liste7 = [(1,2,3),(4,5,6),(7,8,9)]

for a,b,c in liste7:
    print(a,b,c)