website = "https://www.nergizinyazilari.blogspot.com"
siirAdi = "Bir Melodi"

# 1- 'siirAdi' karakter dizisinde kaç karakter bulunmaktadır ?
sonuc = len(website)
sonuc = len(siirAdi)

# 2- 'website' içinden www karakterlerini alın.
sonuc = website[7:10]

# 3- 'website' içinden com karakterlerini alın.
karakterSayisi = len(website)
sonuc = website[karakterSayisi-3:karakterSayisi]

# 4- 'siirAdi' içinden ilk 15 ve son 15 karakterlerini alın.
sonuc = siirAdi[0:15]
sonuc = siirAdi[:15]
sonuc = siirAdi[-15:]

# 5- 'siirAdi' ifadesindeki karakterleri tersten yazdırın.
sonuc = siirAdi[::-1]
#print(sonuc)

# 6- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]
print(s)

# 7- 'abc' ifadesini yan yana 3 defa yazdırın.

print('abc ' * 3)

name, surname, age, job = 'Nergiz' , 'Erdağı' , 18 , 'öğrenci' 

# 8- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Nergiz Erdağı, Yaşım 18 ve mesleğim öğrenci.' 

sonuc = "Benim adım " + name + " " + surname + ",Yaşım " + str(age) + " ve mesleğim " + job + "."
sonuc = "Benim adım {0} {1},Yaşım {2} ve mesleğim {3}".format(name,surname,age,job)
sonuc = f"Benim adım {name} {surname},Yaşım {age} ve mesleğim {job}."

print(sonuc)