class Bangun_Ruang():
    def __init__(self, nama, luas):
        self.nama = nama
        self.luas = luas

    def getLuas(self):
        return self.nama
    
    def getNama(self):
        return self.luas
    
class Persegi(Bangun_Ruang):
    def __init__(self, nama, sisi, luas):
        self.sisi = sisi

        #inherit all attributes from Orang Class

        super().__init__(luas, nama)

    def __str__(self):
        return "\n"f"{self.nama} {self.sisi} {self.luas}"
    
    def printData(self):
        print("\n"f"Aku Adalah {self.getNama()}")
        print(f"luas persegi dengan sisi {self.sisi} adalah {self.getLuas()}")

persegi1 = Persegi ("Persegi", "4", "16")
persegi1.printData()

class Lingkaran(Bangun_Ruang):
    def __init__(self, nama, jari_jari, luas):
        self.jari_jari = jari_jari

        #inherit all attributes from Orang Class

        super().__init__(luas, nama)

    def __str__(self):
        return "\n"f"{self.nama} {self.jari_jari} {self.luas}"
    
    def printData(self):
        print("\n"f"Aku Adalah {self.getNama()}")
        print(f"luas lingkaran dengan jari - jari {self.jari_jari} adalah {self.getLuas()}")

lingkaran1 = Lingkaran ("Lingkaran", "7", "153.93804002589985")
lingkaran1.printData()
        