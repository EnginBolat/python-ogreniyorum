# Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın.
"""liste = ["345","asda","324a","14","kemal"]

for eleman in liste:
    try:
        eleman = int(eleman)
        print(eleman)
    except ValueError:
        print(eleman+" sadece rakamlardan oluşmuyor")"""


# Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın.Bu fonksiyon, eğer sayı çift ise return ile bu değeri dönsün. Ancak sayı tek sayı ise fonksiyon
# raise ile ValueError hatası fırlatsın. Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın ve liste üzerinde gezinerek ekrana sadece çift sayıları
# bastırın.


def ciftmi(sayi):
    try:
        if int(eleman) % 2 == 0:
            print("{} sayısı çift sayıdır".format(eleman))
    except:
        raise ValueError


liste = [34, 2, 1, 3, 33, 100, 61, 1800]

for eleman in liste:
    ciftmi(eleman)
