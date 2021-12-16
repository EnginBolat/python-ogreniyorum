print("""
    *******************************
    
    Basit Hesap Makinesi
    
    1.Toplama
    2.Çıkarma
    3.Çarpma
    4.Bölme
    
    ********************************
""")

try:
    a = float(input("1. Sayıyı Giriniz:"))
    b = float(input("2. Sayıyı Giriniz:"))
    secenek = int(input("İşleminizi Giriniz:"))

    if secenek==1:
        print("{} ve {} sayısının toplamı {}".format(a,b,a+b))
    elif secenek==2:
        print("{} ve {} sayısının farkı {}".format(a,b,a-b))
    elif secenek==3:
        print("{} ve {} sayısının çarpımı {}".format(a,b,a*b))
    elif secenek==4:
        print("{} ve {} sayısının bölümü {}".format(a,b,a/b))
    else:
        print("Geçersiz İşlem")
except:
    print("Yanlış Formatta Deger Giriniz Lütfen Tekrar Deneyiniz")
