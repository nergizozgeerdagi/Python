class ogretmen():
    
    def __init__(self,ad,soyad,telefon,maas,dersler):
        
        self.ad = ad
        self.soyad = soyad
        self.telefon = telefon
        self.maas = maas
        self.dersler = dersler
        
    def bilgiler(self):
        
        print("""
              Öğretmenin Adı : {}
              
              Öğretmenin Soyadı : {}
              
              Öğretmenin Telefonu : {}
              
              Öğretmenin Maaşı : {}
              
              Öğretmenin Girebildiği Dersler : {}
              
             
              """.format(self.ad,self.soyad,self.telefon,self.maas,self.dersler))
              
    def zamyap(self,zammiktarı):
        self.maas = self.maas + zammiktarı

Murat = ogretmen("Murat","Kaya",5410000000,4500,["Matematik","Fen Bilgisi","İngilizce"])
print(Murat.zamyap(750))
print(Murat.bilgiler())