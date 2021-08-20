def besletopla(a = 10):
    print(a+5)
print(besletopla())

def besletopla(a = 10):
    print(a+5)
print(besletopla(7))

def topla(a,b):
    return a+b
print(topla(4, 2,))


def topla(*a):
    toplam = 0
    for i in a:
        toplam = toplam + i
    print(toplam)
print(topla(4,4,5,8))