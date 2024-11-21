class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.spp_dibayar = False
        self.nilai_mata_kuliah = {}

    def bayar_spp(self):
        self.spp_dibayar = True
        print(f"{self.nama} telah membayar SPP.")

    def ambil_mata_kuliah(self, nama_mata_kuliah):
        if self.spp_dibayar:
            print(f"{self.nama} telah mengambil mata kuliah {nama_mata_kuliah}.")
            self.nilai_mata_kuliah[nama_mata_kuliah] = None
        else:
            print(f"{self.nama} harus membayar SPP terlebih dahulu.")

    def set_nilai(self, nama_mata_kuliah, nilai):
        if nama_mata_kuliah in self.nilai_mata_kuliah:
            self.nilai_mata_kuliah[nama_mata_kuliah] = nilai
            print(f"Nilai {nilai} untuk {nama_mata_kuliah} telah diset.")
        else:
            print(f"{self.nama} belum mengambil mata kuliah {nama_mata_kuliah}.")

    def hitung_nilai_akhir(self):
        total_nilai = 0
        jumlah_mata_kuliah = len(self.nilai_mata_kuliah)

        for nilai in self.nilai_mata_kuliah.values():
            if nilai is not None:
                total_nilai += nilai

        if jumlah_mata_kuliah > 0:
            nilai_akhir = total_nilai / jumlah_mata_kuliah
            print(f"Nilai akhir {self.nama} adalah {nilai_akhir:.2f}.")
        else:
            print(f"{self.nama} belum mengambil mata kuliah.")

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek mahasiswa
    mahasiswa1 = Mahasiswa("Luthfi Anazzalea", "L200220052")

    # Proses pembayaran SPP
    mahasiswa1.bayar_spp()

    # Mengambil mata kuliah
    mahasiswa1.ambil_mata_kuliah("Pemrograman Dasar")
    mahasiswa1.ambil_mata_kuliah("Algoritma dan Struktur Data")

    # Mengatur nilai mata kuliah
    mahasiswa1.set_nilai("Pemrograman Dasar", 85)
    mahasiswa1.set_nilai("Algoritma dan Struktur Data", 90)

    # Menghitung nilai akhir
    mahasiswa1.hitung_nilai_akhir()