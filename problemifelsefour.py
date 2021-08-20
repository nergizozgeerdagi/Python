# 4- Username ve parola bilgileri ile giriş kontrolü yapınız. 
_username = "nergiz.erdagi"
_password = "9898"
girilenUsername = input('username: ')
girilenPassword = input('parola: ')

if (girilenUsername.strip() == _username) and (girilenPassword.strip() == _password):
    print('girilen username ve parola doğru')
else:
    print('girilen bilgiler yanlış')