class telefon():
    marka = "Samsung"
    model = "Note10"
    renk = "Siyah"
    batarya = 4000
    sarj = 80

telefon1 = telefon()
telefon2 = telefon()
print(telefon1)
print(telefon2)
print(telefon2.renk)
print(telefon2.renk)
print(telefon.renk)


class bilgisayar():
    
    def __init__(self,marka,model,renk,batarya,sarj):
        self.marka = marka
        self.model = model
        self.renk = renk
        self.batarya = batarya
        self.sarj = sarj
        
bilgisayar1 = bilgisayar("Dell","İnspiron", "Siyah", 8000, 120)
bilgisayar2 = bilgisayar("Hp","Pavillon","Beyaz",6000,100)
print(bilgisayar1.marka)
print(bilgisayar2.marka)


class bilgisayar():
    
    def __init__(self,marka = "Asus",model = "Bilinmiyor",renk = "Mor",batarya = 9000,sarj = 130):
        self.marka = marka
        self.model = model
        self.renk = renk
        self.batarya = batarya
        self.sarj = sarj
        
bilgisayar1 = bilgisayar(renk = "Kırmızı")

 
print(bilgisayar1.marka)
print(bilgisayar1.model)
print(bilgisayar1.renk)
print(bilgisayar1.batarya)
print(bilgisayar1.sarj)