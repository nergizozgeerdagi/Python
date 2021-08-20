# 1- Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.

sayi = int(input('sayı: '))
if  (sayi > 50) and (sayi<=100):
    print(f"{sayi}, 50 ile 100 arasındadır.")
else:
    print(f"{sayi}, 50 ile 100 arasında değildir.")