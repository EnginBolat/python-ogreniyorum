import random

print("""
    *******************************
    
    1 ile 40 arasında sayıyı tahmin edin.
    
    *******************************
""")

rastgele_sayi=random.randint(1,40)
print(rastgele_sayi)
tahmin_hakki=7
while True:
    tahmin = int(input("Tahmininiz:"))
    if (tahmin < rastgele_sayi):
        print("Küçük")
        tahmin_hakki -=1
    elif (tahmin > rastgele_sayi):
        print("Büyük")
        tahmin_hakki -=1
    else:
        print("Tebrikler Doğru Tahmin!")
    if tahmin_hakki == 0:
        print("Tahmin Hakkınız Bitti...")
        break




