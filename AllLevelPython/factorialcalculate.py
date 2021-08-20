print("Çıkmak için 'ç' ye basınız!")

while True:
    sayi = input("Sayıyı giriniz: ")
    if (sayi == "ç"):
        print("Program durduruldu!")
        break
    else:
        sayi = int(sayi)
        a = 1
        
        for i in range(2,sayi+1):
            a *= i
        print(a)