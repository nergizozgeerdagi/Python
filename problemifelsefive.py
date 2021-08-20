# 5- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

if (x>y) and (x>z):
    print("x en büyük sayı: ")
elif (y>x) and (y>z):
    print("y en büyük sayı: ")
elif (z>x) and (z>y):
    print("z en büyük sayı: ")
