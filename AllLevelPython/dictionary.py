sözlük = {"elma":"apple","bir":"one","iki":"two"}

print(type(sözlük))
print(sözlük)

sözlük1 = dict()
print(sözlük1)

sözlük2 = {"elma":"apple","bir":"one","iki":"two"}
print(sözlük2["elma"])

sözlük3 = {"elma":"apple","bir":"one","iki":"two"}
sözlük3["bir"] = 1
print(sözlük3)

sözlük4 = {"a":[10,15,20]}
print(sözlük4)
print(sözlük4["a"])

sözlük5 = {"b":[[1,2],[3,4],[5,6]]}        
print(sözlük5)
print(sözlük5["b"][1][1])
sözlük5["b"][1][1] = 9
print(sözlük5)
sözlük5["b"][1][1] -= 1 
print(sözlük5)

sözlük6 = {"a":[10,15,20]}
print(sözlük6.keys())
print(sözlük6.values())
print(sözlük6.items())