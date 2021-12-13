#Araba Class
"""class Araba():

    def __init__(self,model = "Bilgi Yok", renk = "Bilgi Yok",beygir_gucu=70,silindir=4):
        print("İnit Geldi")
        self.model= model
        self.renk = renk
        self.beygir_gucu = beygir_gucu
        self.silindir= silindir

input_car = Araba()
input_car.model = input("Araba Modelini Giriniz:")
input_car.renk = input("Araba Rengini Giriniz:")
input_car.beygir_gucu = int(input("Araba Beygirini Giriniz:"))
input_car.silindir = int(input("Araba Silindirini Giriniz:"))
print(input_car.model,input_car.renk,input_car.silindir,input_car.beygir_gucu)"""

#Yazılımcı Class
"""class Yazilimci():

    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.diller = diller
        
    def bilgilerigoster(self):
        print('''
        Yazılımcı objesinin özellikleri     
        İsim : {}     
        Soyisim : {}      
        Numara : {}       
        Maaş : {}        
        Diller : {}  
        '''.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))
        
    def zamyap(self,zammiktari):
        print("Zam Yapiliyor")
        self.maas += zammiktari
        
    def dilekle(self,yeni_dil):
         print("Dil Ekleniyor")
         self.diller = self.diller + yeni_dil
         
yazilimci = Yazilimci("Engin","Bolat",1231231,5000,"Python,C#,")
yazilimci.dilekle("Go")
yazilimci.zamyap(3400)
yazilimci.bilgilerigoster()"""

#Kalıtım

"""class Calisan:
    def __init__(self,isim,maas,departman):
        self.isim = isim
        self.maas = maas
        self.departman = departman
    def bilgilerigoster(self):
            print("Çalışanların Bilgileri")
            print("Ad : {}\nMaaş:{}\nDepartman:{}".format(self.isim,self.maas,self.departman))
    def departman_degistir(self,yeni_departman):
        self.departman = yeni_departman

class Yonetici(Calisan):
    def zam_yap(self,zam_miktari):
        self.maas += zam_miktari


yonetici = Yonetici("Ali",3600,"Pazarlama")
yonetici.zam_yap(4000)
yonetici.bilgilerigoster()
############################################
isci = Calisan("Engin",4500,"IT")
isci.departman_degistir("Haberleşme")
isci.bilgilerigoster()"""

#Overriding

"""class Calisan:
    def __init__(self,isim,maas,departman):
        self.isim = isim
        self.maas = maas
        self.departman = departman
    def bilgilerigoster(self):
            print("Çalışanların Bilgileri")
            print("Ad : {}\nMaaş:{}\nDepartman:{}".format(self.isim,self.maas,self.departman))
    def departman_degistir(self,yeni_departman):
        self.departman = yeni_departman

class Yonetici(Calisan):

    def __init__(self,isim,maas,departman,kisi_sayisi):
        self.isim = isim
        self.maas = maas
        self.departman = departman
        self.kisi_sayisi = kisi_sayisi

    def bilgilerigoster(self):
            print("Yönetici Bilgileri")
            print("Ad : {}\nMaaş:{}\nDepartman:{}\nSorumlu Kişi Sayısı:{}".format(self.isim,self.maas,self.departman,self.kisi_sayisi))

    def zam_yap(self,zam_miktari):
        self.maas += zam_miktari

yonetici = Yonetici("Ali",3600,"Pazarlama",4500)
yonetici.zam_yap(300)
yonetici.bilgilerigoster()"""

#SuperKeyword

"""class Calisan:
    def __init__(self,isim,maas,departman):
        print("Calisan init")
        self.isim = isim
        self.maas = maas
        self.departman = departman
    def bilgilerigoster(self):
            print("Çalışanların Bilgileri")
            print("Ad : {}\nMaaş:{}\nDepartman:{}".format(self.isim,self.maas,self.departman))
    def departman_degistir(self,yeni_departman):
        self.departman = yeni_departman

class Yonetici(Calisan):

    def __init__(self,isim,maas,departman,kisi_sayisi):
        super().__init__(isim,maas,departman)
        print("Yonetici init")
        self.kisi_sayisi = kisi_sayisi

    def bilgilerigoster(self):
            print("Yönetici Bilgileri")
            print("Ad : {}\nMaaş:{}\nDepartman:{}\nSorumlu Kişi Sayısı:{}".format(self.isim,self.maas,self.departman,self.kisi_sayisi))

    def zam_yap(self,zam_miktari):
        self.maas += zam_miktari

yonetici = Yonetici("Ali",3600,"Pazarlama",4500)
yonetici.zam_yap(300)
yonetici.bilgilerigoster()"""


class Kitap():

    def __init__(self,isim,yazar,sayfa_sayisi,tur):
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur

    def __str__(self):
        return "Ad : {}\nYazar:{}\nSayfa Sayısı:{}\nTür:{}".format(self.isim,self.yazar,self.sayfa_sayisi,self.tur)

    def __len__(self):
        return self.sayfa_sayisi

    def __del__(self):
        print("Kitap Objesi Siliniyor...")

kitap= Kitap("İstanbul Hatrası","Ahmet Ümit",561,"Polisiye")
print(kitap)
print(len(kitap))

