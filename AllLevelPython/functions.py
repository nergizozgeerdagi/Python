def hosgeldin():
    print("Mekana hoşgeldiniz....")
print(hosgeldin())

def hosgeldin2(isim):
    print("Mekana hoşgeldin....",isim)
print(hosgeldin2("Ahmet"))

def topla(x,y):
    print("Toplamları:",x+y)
print(topla(7, 11))

def faktoriyel(sayı):
    a = 1
    if (sayı == 1):
        print("Sonuç: 1 ")
        
    elif (sayı == 0):
        print("Sonuç: 1")
        
    while (sayı > 1):
        a = a * sayı
        
        sayı -= 1
    print("Sonuç: ",a)   
print(faktoriyel(5))