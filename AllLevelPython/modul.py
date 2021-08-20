"""
faktoriyel fonksiyonu Faktoriyel hesaplar.
hos geldin fonksiyonu selamlama yapar
"""

def faktoriyel(sayı):
    a = 1
    
    if (sayı == 1 or sayı == 0):
        
        return 1
    while (sayı > 1):
        a = a* sayı
        sayı = sayı - 1  
    return a
    
def hosgeldin():
    print("Hoş Geldin")