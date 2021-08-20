'''
    Daire Alanı   : πr²
    Daire Çevresi : 2πr    
    ** Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. 
    (π: 3.14)
'''

pi = 3.14
r = float(input("yarı çap: ")) #r=yarıçap
alan = pi*(r**2) #Daire Alanı : πr²
cevre = 2*pi*r #Daire Çevresi : 2πr 

result = "alan: " + str(alan) + " çevre: " + str(cevre)
print(result)

