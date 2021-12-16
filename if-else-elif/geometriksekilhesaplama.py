print("""
***********************************
Geometrik Şekil Hesaplama Programı

1.Dörtgen
2.Üçgen

***********************************
""")

secim= int(input("Seçiminizi Yapınız:"))

if secim==1:
    k1=int(input("1.Kenarı Giriniz"))
    k2=int(input("2.Kenarı Giriniz"))
    if k1**2==k2**2:
        print("Bu Şekil Bir Karedir Alanı:{}".format(k1**2))
    else:
        print("Bu Şekil Dikdörtgendir Alanı:{}".format(k1*k2))
else:
    k1 = int(input("1.Kenarı Giriniz"))
    k2 = int(input("2.Kenarı Giriniz"))
    k3 = int(input("3.Kenarı Giriniz"))

    if k1==k2 and k2==k3:
        print("Eşkenar Üçgen")
    elif k2!=k3 or k1!=k2 or k1!=k3:
        print("İkizkenar Üçgen")


