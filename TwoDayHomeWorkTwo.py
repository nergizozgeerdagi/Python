#Ders notu hesaplayan kod
dersAdi =input("Not ortalamasını istediğiniz dersin adını giriniz: ")
vizeNotu = float(input("Vize notunuz: "))
finalNotu = float(input("Final notunuz: "))
vizeNotu = vizeNotu*0.3
finalNotu = finalNotu*0.7
ortalama=vizeNotu+finalNotu
print(dersAdi , "Dersi Not Ortalamanız: " , ortalama)