"""
    Uygulama 1: Bir öğrencinin aşağıdaki bilgileri için gerekli değişkenleri oluşturunuz.
    Öğrenci adı
    Öğrenci soyadı
    Öğrenci ad + soyad
    Öğrenci numarası
    Öğrenci cinsiyet
    Öğrenci tc kimlik
    Öğrenci doğum yılı
    Öğrenci adres bilgisi   
    Öğrenci yaşı 
"""

ogrenciAdi="Nergiz"
ogrenciSoyadi="Erdağı"
ogrenciAdSoyad=ogrenciAdi+" "+ogrenciSoyadi
print(ogrenciAdSoyad)

ogrenciNumarasi=192222
print(ogrenciNumarasi)

ogrenciCinsiyeti=True #Kadın
print("True:Kadın, False:Erkek")
print("Öğrencinin Cinsiyeti:" , ogrenciCinsiyeti)

ogrenciKimlikNo=99999999999
print(ogrenciKimlikNo)

ogrenciDogumYili=2002
print(ogrenciDogumYili)

ogrenciAdres="Ankara-Kızılay"
print(ogrenciAdres)

ogrenciYasi=2021-ogrenciDogumYili
print(ogrenciYasi)