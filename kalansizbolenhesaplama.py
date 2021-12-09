def kalansizbolenler(sayi):
    kalansizbolenler=[]
    for i in range(2,sayi):
        if sayi % i == 0:
            kalansizbolenler.append(i)
    return kalansizbolenler

while True:
    print("Programdan Çıkmak İçin Q Basınız...")
    sayi=input("Sayi Giriniz:")
    if sayi.lower() == "q":
        break
    else:
        sayi= int(sayi)

        print("Tam Bölenler:",kalansizbolenler(sayi))