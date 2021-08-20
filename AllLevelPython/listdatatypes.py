nergiz = []
print(type(nergiz))

liste = list()
print(type(liste))

liste1 = [4,8,75,"Nergiz",14.6]
print(type(liste1))
print(liste1)

liste2 = ["Herkese Merhaba"]
print(len(liste2))
print(liste2)

liste3 = list("Merhaba")
print(liste3)
print(len(liste3))

liste4 = [1,2,3,4,5,6,7,8,9]
print(len(liste4))
print(liste4[3])
print(liste4[-1])
print(liste4[len(liste4)-1])

liste5 = [1,2,3,8,65,78]
liste5[1] = [1001]
print(liste5)
liste5[1:3] = [10,15]
print(liste5)
print(liste5[::2])
print(liste5[::-1])

liste6 = [1,2,3]
liste7 = [6,4,5]
liste8 = liste6+liste7
print(liste8)
print(liste6*2)
liste6 = liste6*2
print(liste6)
liste6[2] = 7
print(liste6)