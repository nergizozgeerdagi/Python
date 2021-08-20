sayilar = [2,3,11,20]

# for=>collection
#1-100=>koşul-ifade

i=1
while i<=100:
    if(i%2==0):
        print("Çift sayı: " , i)
    else:
        print("Tek sayı: " , i)
    i=i+1

username=""
while not username:
    username = input("Lütfen kullanıcı adınızı giriniz!: ")

print("Girdiğiniz kullanıcı adı: " , username)