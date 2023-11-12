class Karyawan:
    def __init__(self, nama):
        self.nama = nama
        self.gaji_pokok = 4000000
        self.uang_harian = 30000
        self.absen = False

    def htg_gaji(self):
        if not self.absen:
            return self.gaji_pokok + self.uang_harian
        else:
            return self.gaji_pokok

    def tampilkan_info(self):
        print(f"\nNama\t\t\t: {self.nama}")
        print(f"Gaji Pokok\t\t: {self.gaji_pokok}")
        print(f"Uang Harian\t\t: {self.uang_harian}")
        print(f"Absen\t\t\t: {'Tidak' if not self.absen else 'Ya'}")
        print(f"Total Gaji\t\t: {self.htg_gaji()}")

class Manajer(Karyawan):
    def __init__(self, nama):
        super().__init__(nama)
        self.tunjangan_profesi = 1500000
        self.uang_transport_harian = 30000

    def htg_gaji(self):
        if not self.absen:
            return (
                self.gaji_pokok
                + self.uang_harian
                + self.tunjangan_profesi
                + self.uang_transport_harian
            )
        else:
            return self.gaji_pokok + self.tunjangan_profesi

    def tampilkan_info(self):
        print("Informasi Manajer :")
        super().tampilkan_info() #ngambil data 'print' dari tampilkan_info
        print(f"Tunjangan Profesi\t: {self.tunjangan_profesi}")
        print(f"Uang Transport Harian\t: {self.uang_transport_harian}")


class Admin(Karyawan):
    def __init__(self, nama, jam_lembur=0):
        super().__init__(nama)
        self.tarif_lembur = 40000
        self.jam_lembur = jam_lembur

    def hitung_gaji(self):
        if not self.absen:
            return self.gaji_pokok + self.uang_harian + (self.tarif_lembur * self.jam_lembur)
        else:
            return self.gaji_pokok

    def tampilkan_info(self):
        print("\nInformasi Admin\t:")
        super().tampilkan_info()
        print(f"Tarif Lembur\t\t: {self.tarif_lembur}")
        print(f"Jam Lembur\t\t: {self.jam_lembur}")


class Pemasaran(Karyawan):
    def __init__(self, nama):
        super().__init__(nama)
        self.uang_transport_harian = 50000

    def htg_gaji(self):
        return self.gaji_pokok + self.uang_transport_harian

    def tampilkan_info(self):
        print("\nInformasi Pemasaran :")
        super().tampilkan_info()
        print(f"Uang Transport Harian\t: {self.uang_transport_harian}")


# Metode utama
if __name__ == "__main__":
    manajer1 = Manajer("Rifky")
    admin1 = Admin("Salwa", jam_lembur=2)
    pemasaran1 = Pemasaran("Adam")

    # Simulasi absen untuk Admin
    admin1.absen = True

    # Tampilkan informasi
    manajer1.tampilkan_info()
    admin1.tampilkan_info()
    pemasaran1.tampilkan_info()