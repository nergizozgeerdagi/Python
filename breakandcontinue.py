isim = "Nergiz Erdağı"

for harf in isim:
    if(harf=="i"):
        break
    print(harf)


i=0
while(i<5):
    i=i+1
    if(i==3):
        break
    print(i)
print("Döngü sonu!!")


#1-100 arası çift sayılar toplamı programı

toplam=0
n=0
while(n<=100):
    n+=1
    if(n%2==1):
        continue
    toplam+=n
print(f"Toplam: {toplam}")