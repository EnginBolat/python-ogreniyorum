print("""
Kullanici Giriş Programı
""")

system_admin_username="admin"
system_admin_password="admin"

get_username=input("Kullanıcı Adını Giriniz:")
get_password=input("Kullanıcı Şifresini Giriniz:")

if get_username == system_admin_username and get_password == system_admin_password:
    print("Hoşgeldin {}".format(get_username))
else:
    print("Hatalı Giriş Denemesi Lütfenn Tekrar Deneyiniz...")
