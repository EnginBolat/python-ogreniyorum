"""try:
    a = int("2asdasdas3")
    print("Program Burada")
except:
    print("Bir Hata oluştu!")
print("Program Bitti")

print("***************************************")

try:
    a = int("23")
    print("Program Burada")
except:
    print("Bir Hata oluştu!")
print("Program Bitti")

print("***************************************")

try:
    a = int("23")
    print("Program Burada")
except ValueError:
    print("Bir Hata oluştu!")
print("Program Bitti")

print("***************************************")

while True:
    try:
        a = int(input("1.Sayı:"))
        b = int(input("2.Sayı:"))
        print(a / b)
        break
    except ValueError:
        print("Lütfen inputu doğru girin.")
    except ZeroDivisionError:
        print("Bir sayı 0'a bölünemez.")
    print("Program Bitti")

while True:
    try:
        a = int(input("1.Sayı:"))
        b = int(input("2.Sayı:"))
        print(a / b)
        break
    except (ValueError,ZeroDivisionError):
        print("Value Error veya ZeroDivisionError Hatası")
    finally:
        print("Finally Bloğu")"""

def terscevir(s):
    if type(s) != str:
        raise ValueError ("Lütfen String Değer Giriniz")
    else:
        return s[::-1]
print(terscevir(12))
