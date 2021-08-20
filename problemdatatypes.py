'''
    Bir aracın km cinsinden gittiği yol bilgisini mil olarak yazdırınız.
    mil = km / 1.609344
'''

print("Kaç km yol gittiniz?: ")
mesafeKm=input()
mesafeMil=float(mesafeKm)/1.609344

#Python round() fonksiyonu, x'in ondalık kısmını n kadar 
#yuvarlayarak döndürür. Bu fonksiyon parametre ile girilen
#reel sayıyı ondalıklı kısımdaki değere göre, bir üst veya bir alt 
#tam sayıya şayet ikinci parametrede girilirse belirtilen ondalık 
#sayısı kadar yuvarlamak için kullanılan bir fonksiyondur.
mesafeMil=round(mesafeMil , 2)
print(str(mesafeKm) + " km= " + str(mesafeMil) + " mil")
