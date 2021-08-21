liste = [1,2,3,4,5]
liste.append(6)
print(liste)

liste1 = [1,2,3,4,5]
liste2 = [i for i in liste1]
print(liste2)

liste3 = [1,2,3,4,5]
liste4 = [6,7,8]
liste3.extend(liste4)
print(liste3)
print(liste4)

liste5 = [70,85,67,42]
liste5.pop(2)
print(liste5)

liste6 = [1,2,4,5,6,7,8,9]
liste6.insert(2,3)
print(liste6)

liste7 = ["Ahmet","Mehmet","Civan","Şevval"]
liste7.remove("Ahmet")
liste7.remove("Mehmet")
liste7.remove("Civan")
liste7.remove("Şevval")
print(liste7)

liste8 = [10,20,30,40,50,50,50,40,30,30,40,30,40]
print(liste8.index(30,3))

liste9 = [1,1,1,1,2,2,2,2,3,4,5,5,5,5]
print(liste.count(5))

liste10 = [10,12,1,2,3,4,5]
liste10.sort()
print(liste10)

liste10.sort(reverse = True)
print(liste10)