class Orang():
    def __init__(self, firstName, middleName, lastName):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName

    def getFirstName(self):
        return self.firstName
    
    def getMiddleName(self):
        return self.middleName
    
    def getLastName(self):
        return self.lastName
    
class Alamat():
    def __init__(self, jalan, kota):
        self.jalan = jalan
        self.kota = kota

    def getJalan(self):
        return self.jalan
    
    def getKota(self):
        return self.kota

class Mahasiswa(Orang, Alamat):
    def __init__(self, firstName, middleName, lastName, nim, prodi, angkatan, jalan, kota):
        self.nim = nim
        self.prodi = prodi
        self.angkatan = angkatan
        self.jalan = jalan
        self.kota = kota

        #inherite
        Orang.__init__(self, firstName, middleName, lastName)
        Alamat.__init__(self, jalan, kota)

    def __str__(self):
        return f"{self.firstName} {self.middleName} {self.lastName} {self.nim} {self.prodi} {self.angkatan} {self.jalan} {self.kota}"
    
    def printData(self):
        print("\n"f"Nama     : {self.getFirstName()} {self.middleName} {self.lastName}")
        print(f"NIM      : {self.nim}")
        print(f"Prodi    : {self.prodi}")
        print(f"Angkatan : {self.angkatan}")
        print(f"Alamat   : {self.jalan}, {self.kota}")

            
mhs = Mahasiswa("Rifky", "Khoerul", "Muzaky", "2207013", "Sistem Informasi", "2022", "Jl. Raya Samarang", "Kabupaten Garut")
mhs.printData()
