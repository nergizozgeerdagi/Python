try:
    

    a = int(input("Lütfen 1. Sayıyı Giriniz: "))

    b = int(input("Lütfen 2. Sayıyı Giriniz: "))    


    print(a/b)
    
except ValueError:
    print("Lütfen int değer giriniz")
    
except ZeroDivisionError:
    print("Sayılar 0'a Bölünemez")
    
    
try:
    

    a = int(input("Lütfen 1. Sayıyı Giriniz: "))

    b = int(input("Lütfen 2. Sayıyı Giriniz: "))    


    print(a/b)
    
except (ValueError,ZeroDivisionError):
    print("Hata")
    
    
try:
    

    a = int(input("Lütfen 1. Sayıyı Giriniz: "))

    b = int(input("Lütfen 2. Sayıyı Giriniz: "))    


    print(a/b)
    
except:
    print("Hata")
    

try:
    

    a = int(input("Lütfen 1. Sayıyı Giriniz: "))

    b = int(input("Lütfen 2. Sayıyı Giriniz: "))    


    print(a/b)
    
except:
    print("Hata")
    
finally:
    print("Burası Çalıştı")
    
    
def hosgeldin2(isim):
    if (type(isim) != str):
        raise ValueError("Sadece Str değer Gönderebilirsiniz")
    else:
      
        print("Mekana hoşgeldin....",isim)

print(hosgeldin2(55))