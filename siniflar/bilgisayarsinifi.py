#Bilgisayar
class Bilgisayar:
    def __init__(self,anakart = "Bilgi Yok",islemci= "Bilgi Yok",ram= "Bilgi Yok",ssd= "Bilgi Yok",hdd= "Bilgi Yok",ekran_karti= "Bilgi Yok",guc_kaynagi= "Bilgi Yok"):
        self.anakart = anakart
        self.islemci = islemci
        self.ram = ram
        self.ssd = ssd
        self.hdd = hdd
        self.ekran_karti = ekran_karti
        self.guc_kaynagi = guc_kaynagi

    def __str__(self):
        return "Anakart: {}\nİşlemci: {}\nRam: {}\nSSD: {}\nHDD: {}\nEkran Kartı: {}\nGüç Kaynağı {}".format(self.anakart,self.islemci,self.ram,self.ssd,self.hdd,self.ekran_karti,self.guc_kaynagi)

    def __delete__(self, instance):
        return print("Siliniyor...")

    def anakart(self,model):
        self.anakart= model
    def islemci(self,model):
        self.islemci=model
    def ram(self,boyut):
        self.ram=boyut
    def ssd(self,boyut):
        self.ssd=boyut
    def hdd(self,boyut):
        self.hdd=boyut
    def ekran_karti(self,model):
        self.ekran_karti=model
    def guc_kaynagi(self,watt):
        self.guc_kaynagi=watt

bilgisayar = Bilgisayar("G31M-ES2L","Core 2 Duo","4GB","240GB","1TB","GT 9500","350W")
print(bilgisayar)
