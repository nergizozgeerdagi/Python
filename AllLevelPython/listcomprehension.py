liste = ["a","b","c"]
liste1 = []
for i in liste:
    liste1.append(i)
print(liste1)

liste2 = ["a","b","c"]
liste3 = [i for i in liste2]
print(liste3)

liste4 = [(1,2,3),(4,5,6),(7,8,9)]
liste5 = [i+j+k for i,j,k in liste4]
print(liste5)

liste6 = [[1,2],[3,4,5,6,7],[8,9,10]]
liste7 = [a for i in liste6 for a in i]
print(liste7)