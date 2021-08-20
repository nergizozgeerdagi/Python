# 3- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.

sayi = int(input('sayı: '))
if (sayi > 0):
    if (sayi % 2 == 1):
        print('girilen sayı pozitif tek sayıdır.')
    else:
        print('sayı pozitif ancak tek değil.')
else:
    print('girilen sayı negatif.')