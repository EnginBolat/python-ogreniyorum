print("Boy-Kilo İndeks Hesaplayıcı")

boy=float(input("Boyunuzu Giriniz: "))
kilo=int(input("Kilonuzu Giriniz: "))

indeks= kilo / boy**2

if indeks<18.5:
    print("Zayıf")
elif indeks >= 18.5 and indeks<25:
    print("Normal")
elif indeks >= 25 and indeks<30:
    print("Aşırı Kilolu")
else:
    print("Obez")