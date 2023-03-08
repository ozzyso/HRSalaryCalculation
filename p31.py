class Personel():
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad

    def info(self):
        print(f"Personel Ad Soyad: {self.ad} {self.soyad}")


class Calisan(Personel):
    def __init__(self,maas,ad,soyad):
        self.maas = maas
        Personel.__init__(self,ad,soyad)

    def info(self):
        print(f"Personel Ad Soyad: {self.ad} {self.soyad}, Maaş: {self.maas}")

    def zamYap(self,limit):   #5000 tl altı maaşa 10% zam yap, üstüne 5% zam
        self.limit = limit
        if self.maas <= limit:
            self.maas = (self.maas*10/100) + self.maas
        else:
            self.maas = (self.maas*5/100) + self.maas
        print(f"{self.ad} {self.soyad} için onaylanan yeni maaş: {self.maas}")

yeni_personel = Personel("Mustafa", "Sandal")
yeni_personel.info()

yeni_calisan = Calisan(5000,"Ali","Yılmaz")
yeni_calisan.info()

yeni_calisan.zamYap(4900)

calisan2 = Calisan(4500,"Veli","Çevik")
calisan2.info()
calisan2.zamYap()


#---------------------------------------------------------------------------------------------------------------------------

#hocanın kodu


class Personel():
    
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad
    
    def bilgileriGoster(self):
        print(f"Personel adısoyadı; {self.ad} {self.soyad}")


class Calisan(Personel):
    
    def __init__(self,maas,ad,soyad):
        self.maas = maas
        Personel.__init__(self,ad,soyad)

    def bigileriGoster(self):
        print(f"Çalışan adısoyadı; {self.ad} {self.soyad}, maaşı:{self.maas} ")
    
    def zamYap(self,limit):
        self.limit = limit
        if self.maas <= limit :
            self.maas = (self.maas * 10 / 100) + self.maas
        else:
            self.maas = (self.maas * 5 / 100) + self.maas
        print(f"{self.ad} {self.soyad} için onaylanan yeni maaş: {self.maas}")


yeni_personel = Personel("Mustafa","Öztürk")
yeni_personel.bilgileriGoster()

yeni_calisan = Calisan(5000,"Ali","Öztürk")
yeni_calisan.bigileriGoster()
yeni_calisan.zamYap(4900)

calisan2 = Calisan(4500,"Veli","Çevik")
calisan2.bigileriGoster()




