# 6- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    a-) Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    b-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    c-) Finalden 70 alındığında ortalamanın önemi olmasın.

vize1 = float(input('vize 1: '))
vize2 = float(input('vize 2: '))
final = float(input('final: '))

ortalama = (((vize1 + vize2) / 2) * 0.4) + (final * 0.6)
sonuc = ortalama>=50
sonuc = (ortalama >= 50) and (final>=50)
sonuc = (ortalama >= 50) or (final>=70)

#durum 1
if(ortalama>=50):
    print(f"öğrencini not ortalaması: {ortalama} ve sınıfı geçti")
else:
    print(f"öğrencini not ortalaması: {ortalama} ve kaldı.")

# durum 2
if (ortalama>=50):
    if(final>=50):
        print(f'öğrencinin not ortalaması: {ortalama} ve öğrenci geçti.')
    else:
        print(f'öğrencinin not ortalaması: {ortalama} ve öğrenci kaldı. Finalden en az 50 almalıdır.')
else:
    print(f'öğrencinin not ortalaması: {ortalama} ve öğrenci kaldı.')

# durum 3
if(ortalama>=50):
    print(f'öğrencinin not ortalaması: {ortalama} ve öğrenci geçti.')
else:
    if (final>=70):
        print(f'öğrencinin not ortalaması: {ortalama} ve öğrenci başarılı çünkü finalden 70 üstü aldı.')
    else:
        print(f'öğrencinin not ortalaması: {ortalama} ve öğrenci kaldı.')