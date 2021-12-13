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




