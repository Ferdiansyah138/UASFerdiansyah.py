# Sistem Manajemen Produk di Gudang

class Produk:
    def __init__(self, kode, nama, jumlah, harga):
        self.kode = kode
        self.nama = nama
        self.jumlah = jumlah
        self.harga = harga

    def tampilkan_info(self):
        print(f"Kode Produk: {self.kode}")
        print(f"Nama Produk: {self.nama}")
        print(f"Jumlah Stok: {self.jumlah}")
        print(f"Harga: Rp{self.harga}")
        print("-" * 30)

class Gudang:
    def __init__(self):
        self.produk_list = {}

    def tambah_produk(self, produk):
        self.produk_list[produk.kode] = produk
        print(f"Produk {produk.nama} berhasil ditambahkan.")

    def hapus_produk(self, kode_produk):
        if kode_produk in self.produk_list:
            del self.produk_list[kode_produk]
            print(f"Produk dengan kode {kode_produk} berhasil dihapus.")
        else:
            print("Produk tidak ditemukan.")

    def update_stok(self, kode_produk, jumlah_baru):
        if kode_produk in self.produk_list:
            self.produk_list[kode_produk].jumlah = jumlah_baru
            print(f"Stok produk {self.produk_list[kode_produk].nama} berhasil diperbarui.")
        else:
            print("Produk tidak ditemukan.")

    def tampilkan_stok(self):
        if not self.produk_list:
            print("Gudang kosong!")
        else:
            for produk in self.produk_list.values():
                produk.tampilkan_info()

    def cari_produk(self, kode_produk):
        if kode_produk in self.produk_list:
            self.produk_list[kode_produk].tampilkan_info()
        else:
            print("Produk tidak ditemukan.")

def menu():
    print("\n=== Sistem Manajemen Produk Gudang ===")
    print("1. Tambah Produk")
    print("2. Hapus Produk")
    print("3. Update Stok Produk")
    print("4. Tampilkan Stok Produk")
    print("5. Cari Produk")
    print("6. Keluar")
    pilihan = input("Pilih menu (1-6): ")
    return pilihan

def main():
    gudang = Gudang()

    while True:
        pilihan = menu()

        if pilihan == "1":
            kode = input("Masukkan kode produk: ")
            nama = input("Masukkan nama produk: ")
            jumlah = int(input("Masukkan jumlah stok: "))
            harga = float(input("Masukkan harga produk: Rp"))
            produk = Produk(kode, nama, jumlah, harga)
            gudang.tambah_produk(produk)

        elif pilihan == "2":
            kode = input("Masukkan kode produk yang ingin dihapus: ")
            gudang.hapus_produk(kode)

        elif pilihan == "3":
            kode = input("Masukkan kode produk untuk update stok: ")
            jumlah_baru = int(input("Masukkan jumlah stok baru: "))
            gudang.update_stok(kode, jumlah_baru)

        elif pilihan == "4":
            gudang.tampilkan_stok()

        elif pilihan == "5":
            kode = input("Masukkan kode produk untuk dicari: ")
            gudang.cari_produk(kode)

        elif pilihan == "6":
            print("Terima kasih telah menggunakan sistem!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-6.")

if __name__ == "__main__":
    main()
