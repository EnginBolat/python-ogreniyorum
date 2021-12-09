print("""
**********************************
Gelişmiş Kullanici Giris Programı
**********************************
""")

system_username="admin"
system_password="admin"
girishakki=3

while True:
    getusername=input("Kullanıcı Adınızı Giriniz:")
    getpassword=input("Parolanızı Giriniz:")

    if getusername == system_username and getpassword == system_password:
        print("Hoşgeldiniz")
        break
    elif getusername == system_username and getpassword != system_password:
        print("Parolanız Yanlış")
        girishakki -= 1
    elif getusername != system_username and getpassword == system_password:
        print("Kullanıcı Adınız Yanlış")
        girishakki -= 1
    else:
        print("Kullanıcı Adı ve Şifreniz Yanlış")
        girishakki -= 1
    if girishakki==0:
        print("Giriş Hakkınız Tükendi...")
        break
