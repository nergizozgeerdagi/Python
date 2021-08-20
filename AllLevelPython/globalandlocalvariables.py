x = 11
def fonksiyon():
    print(x)
print(fonksiyon())

a = 20
def fonk():
    a = 14
    print(a)
print(fonk())
print(a)

b = 34
def fonks():
    global b
    b = 17
    print(b)
print(fonks())
print(b)