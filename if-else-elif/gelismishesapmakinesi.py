import math

print("""
*******************************************

    GELİŞMİŞ HESAP MAKİNESİ
    
    1.TOPLAMA
    2.ÇIKARMA
    3.ÇARPMA
    4.BÖLME
    5.KAREKÖK ALMA
    6.FAKTÖRİYEL HESAPLAMA
    7.ÜS ALMA

*******************************************
""")

while True:
        get_numer1=float(input("1. Sayı:"))
        get_numer2=float(input("2. Sayı:"))
        get_input = input("Seçiminizi Yapınız:")
        if get_input == "1":
            print("Sayıların Toplamı",get_numer1+get_numer2)
        elif get_input == "2":
            print("Sayıların Farkı", get_numer1 - get_numer2)
        elif get_input == "3":
            print("Sayıların Çarpımı", get_numer1 * get_numer2)
        elif get_input == "4":
            print("Sayıların Bölümü", get_numer1 / get_numer2)
        elif get_input == "5":
            print("{} sayısının karekökü:{}\n{} sayısının karekökü:{}".format(get_numer1,math.sqrt(get_numer1),get_numer2,math.sqrt(get_numer2)))
        elif get_input == "6":
            print("{} sayısının faktöriyeli:{}\n{} sayısının faktöriyeli:{}".format(get_numer1,math.factorial(get_numer1),get_numer2,math.factorial(get_numer2)))
        elif get_input == "7":
            print("{} sayısının üssü:{}\n{} sayısının üssü:{}".format(get_numer1,pow(get_numer1,2),get_numer2,pow(get_numer2,2)))










