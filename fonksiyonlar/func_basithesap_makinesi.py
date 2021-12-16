def toplama(a,b):
    return a+b

def cikarma(a,b):
    return a-b

def carpma(a,b):
    return a*b

def bolme(a,b):
    return a/b

print("""

    1.Toplama
    2.Çıkarma
    3.Çarpma
    4.Bölme


""")



get_number1=float(input("1.Sayıyı Giriniz:"))
get_number2=float(input("2.Sayıyı Giriniz:"))
get_selection=int(input("Seçiminizi Giriniz:"))

if get_selection == 1:
    print(toplama(get_number1,get_number2))
elif get_selection == 2:
    print(cikarma(get_number1,get_number2))
elif get_selection == 3:
    print(carpma(get_number1,get_number2))
else:
    print(bolme(get_number1,get_number2))
