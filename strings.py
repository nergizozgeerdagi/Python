ad='Nergiz'
yas='18'
numara='16'

mesaj='Benim adım ' + ad + ', yaşım ' + yas + ' ve numaram ' + numara
print(mesaj)
print(mesaj[2])
print(mesaj[9]) #boşluklar da sayılarak 0'dan saymaya başlanır.
print(mesaj[0]) #Her string dizisi 0'dan atamaya başlar, çıktı B olur.

karakterSayisi=len(mesaj) #Karakter sayısını len ile hesaplarız.
print(karakterSayisi)
print(mesaj[2:4]) #2. ile 4. karakter arasındaki 2 dahil olmak üzere olan kısmı yazdır.
print(mesaj[::-1]) #string'i terse çeviririz.