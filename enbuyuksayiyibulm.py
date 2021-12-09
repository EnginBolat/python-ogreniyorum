
a=float(input("1. Sayıyı Giriniz:"))
b=float(input("2. Sayıyı Giriniz:"))
c=float(input("3. Sayıyı Giriniz:"))

if a<b and b<c:
    print("En Büyük Sayi: {}".format(c))
elif c<b and b<a:
    print("En Büyük Sayi: {}".format(a))
else:
    print("En Büyük Sayi: {}".format(b))