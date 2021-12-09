print("""
**********************************************

    ATM MAKİNESİ ÖRNEĞİ
    
    1.BAKİYE SORGULAMA
    
    2.PARA YATIRMA
    
    3.PARA ÇEKME
    
    Programdan çıkmak için "q" tuşuna basınız...

**********************************************
""")


bakiye=1000
get_info=input("Seçiminizi Yapınız:")

while True:
    try:
        if get_info == "q":
            print("Bankamatikten Çıkılıyor")
            break
        elif get_info == "1":
            print("Mevcut Bakiyeniz: ", bakiye)
            break
        elif get_info == "2":
            try:
                parayatir = int(input("Yatırmak istediğiniz tutarı giriniz:"))
                bakiye += parayatir
                print("Mevcut Bakiyeniz: ", bakiye)
                break
            except:
                print("Lütfen sadece sayılardan oluşan bir metin giriniz...")
                continue
        else:
            try:
                paracek = int(input("Çekmek istediğiniz tutarı giriniz:"))
                bakiye -= paracek
                print("Mevcut Bakiyeniz: ", bakiye)
                break
            except:
                print("Lütfen sadece sayılardan oluşan bir metin giriniz...")
                continue
    except:
        print("Lütfen Sadece Belirtilen Numaralı işlemlerden birini yapınız...")
        continue