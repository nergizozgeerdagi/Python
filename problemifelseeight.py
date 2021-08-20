# 8- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. 
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır. 

isim = input('isim: ')
yas = int(input('yaş: '))
egitim = input('eğitim: ')

if (yas >= 18):
    if (egitim == 'lise' or egitim == 'üniversite'):
        print('ehliyet alabilirsiniz.')
    else:
        print(f'{isim} ehliyet alamazsınız çünkü eğitim durumu yetersiz.')
else:
    print(f'{isim} ehliyet alamazsınız çünkü yaşınız tutmuyor.')