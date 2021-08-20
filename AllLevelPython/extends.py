class calısanlar():
    
    def __init__(self,isim,maas,gorev):
        
        self.isim = isim
       
        self.maas = maas
        
        self.gorev = gorev

    def bilgiler(self):
        print("Bilgiler: \nİsim: {}\nMaaş: {}\nGörevi: {}".format(self.isim,self.maas,self.gorev))
        
    def zamyap(self,zammiktarı):
        self.maas += zammiktarı
        
    def gorevdegis(self,yenigorrev):
        
        self.gorev = yenigorrev
    
class yoneticiler(calısanlar):
    
    def __init__(self,isim,maas,gorev,oda):
        
        super().__init__(isim,maas,gorev)
        
        self.oda = oda
    
    def odadegis(self,yenioda):
        
        self.oda = yenioda
        
    def bilgiler(self):
        print("Bilgiler: \nİsim: {}\nMaaş: {}\nGörevi: {}\nOda Numarası: {}".format(self.isim,self.maas,self.gorev,self.oda))

murat = yoneticiler("Murat",5000,"Müdür",4)
murat.odadegis(6)
murat.gorevdegis("Müdür Yardımcısı")
murat.zamyap(250)
murat.bilgiler()