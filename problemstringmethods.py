website = "https://www.nergizinyazilari.blogspot.com"
siirAdi = "Mumdaki Gece"

# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
sonuc = ' Hello World '.strip()
sonuc = ' Hello World '.lstrip()
sonuc = ' Hello World '.rstrip()

sonuc = website.lstrip('/:pthw.')

# 2- 'www.nergizinyazilari.blogspot.com' içindeki nergizinyazilari bilgisi haricindeki her karakteri silin.
sonuc = "www.nergizinyazilari.blogspot.com".strip('w.moc')

# 3- 'siirAdi' karakter dizisinin tüm karakterlerini küçük harf yapın.
sonuc = siirAdi.lower()

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
sonuc = website.count('a')
sonuc = website.count('www')
sonuc = website.count('www',9,15)

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
sonuc = website.startswith('www')
sonuc = website.endswith('com')

# 6- 'website' içinde '.com' ifadesi var mı?
sonuc = website.find('.com')
sonuc = website.find('com',0,10)
sonuc = siirAdi.find('Gece')
sonuc = siirAdi.rfind('Gece')

# sonuc = siirAdi.index('Gece')
# sonuc = siirAdi.rindex('Gece')
# sonuc = siirAdi.index('Mumdaki')

# 7- 'siirAdi' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
sonuc = "abc1".isalpha()
sonuc = "123".isdigit()

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
sonuc = 'Contents'.center(50,'*')
sonuc = 'Contents'.ljust(50,'*')
sonuc = 'Contents'.rjust(50,'*')

# 9- 'siirAdi' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
sonuc = siirAdi.replace(' ','-')

# 10-'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
sonuc = 'Hello World'.replace('World','There')

# 11-'siirAdi' karakter dizisini boşluk karakterlerinden ayırın.
siirAdi = siirAdi.lower().replace(':','')
sonuc = siirAdi.split()

print(sonuc)