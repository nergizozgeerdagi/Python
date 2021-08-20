print(""" Atm'ye Hoş Geldiniz! Tuşlamalar:
      
      Para Çekmek için : 1
      
      Para Yatırmak için : 2
      
      Bakiye Sorgulamak İçin : 3
      
      Kart iadesi için : "99"
      
      """)
      
bakiye = 75

while True:
    islem = input("Yapmak istediğiniz işlemi seçiniz: ")
    
    if islem == "1":
        miktar = int(input("Çekmek istediğiniz Miktar? : "))
        if miktar > bakiye:
            print("Bakiye Yetersiz Menüye Yönlendiriliyorsunuz!")
            continue
        bakiye -= miktar
    elif islem ==  "2":
        miktar1 = int(input("Yatırmak istediğiniz Miktarı Giriniz: "))
        bakiye += miktar1
    elif islem == "3":
        print("Bakiyeniz: ",bakiye)
    elif islem == "99":
        print("Kartınız İade Ediliyor.")
        break
    else:
        print("Geçersiz İşlem!")