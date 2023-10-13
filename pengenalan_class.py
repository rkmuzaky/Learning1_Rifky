class X:
    x = 5

k = X()
print(k.x)

class X_lagi:
    x = 5

k = X_lagi()
k.x = 10
print(k.x)

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

saya = Mahasiswa("Iky", "2207013")
print("Nama saya adalah", saya.nama)
print("NIM saya adalah", saya.nim)

class Mahasiswa_lagi:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def __str__(self):
        return f"Nama saya adalah {self.nama}, dan NIM saya adalah {self.nim}"
    
saya = Mahasiswa_lagi("Iky", "2207103")
print(saya)

class Mhs:
    def __init__(self, nama, nim, umur):
        self.nama = nama
        self.nim = nim
        self.umur = umur

    def __str__(self):
        return f"Nama saya adalah {self.nama}, dan NIM saya adalah {self.nim}"
    
    def tahunLahir(self):
        return 2023 - self.umur
    
saya = Mhs("Iky", "2207013", 19)
print("Tahun lahir saya adalah", saya.tahunLahir())

class Mhs_lthn:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def __str__(self):
        return f"Nama saya adalah {self.nama}, dan NIM saya adalah {self.nim}"
       
saya = Mhs_lthn("Iky", "2207013")
print(f"{saya.nama} Mahasiswa angkatan 20{saya.nim[:2]}") #Iky Mahasiswa angkatan 2022





