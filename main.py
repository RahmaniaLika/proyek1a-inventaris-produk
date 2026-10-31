
class InventarisProduk:
    def __init__(self):
        # Dictionary untuk menyimpan data produk
        self.data_produk = {}

    # 1. Menambahkan produk
    def tambah_produk(self, id_produk, nama, harga, stok):
        if id_produk in self.data_produk:
            print("ID produk sudah terdaftar!")
            return

        self.data_produk[id_produk] = {
            "nama": nama,
            "harga": harga,
            "stok": stok
        }

        print("Produk berhasil ditambahkan!")

    # 2. Mencari produk berdasarkan ID
    def cari_produk(self, id_produk):
        if id_produk in self.data_produk:
            print("\nProduk ditemukan!")
            print("ID Produk :", id_produk)
            print("Nama      :", self.data_produk[id_produk]["nama"])
            print("Harga     : Rp", self.data_produk[id_produk]["harga"])
            print("Stok      :", self.data_produk[id_produk]["stok"])
        else:
            print("Produk tidak ditemukan!")

    # 3. Menghapus produk
    def hapus_produk(self, id_produk):
        if id_produk in self.data_produk:
            del self.data_produk[id_produk]
            print("Produk berhasil dihapus!")
        else:
            print("Produk tidak ditemukan!")

    # 4. Menampilkan semua produk
    def tampilkan_produk(self):
        if not self.data_produk:
            print("Belum ada data produk.")
            return

        print("\n===== DAFTAR PRODUK =====")

        for id_produk, produk in self.data_produk.items():
            print("-------------------------")
            print("ID Produk :", id_produk)
            print("Nama      :", produk["nama"])
            print("Harga     : Rp", produk["harga"])
            print("Stok      :", produk["stok"])


# Program utama (CLI)
inventaris = InventarisProduk()

# Data awal untuk contoh pengujian
inventaris.tambah_produk("P001", "Laptop ASUS", 8500000, 10)
inventaris.tambah_produk("P002", "Mouse Logitech", 150000, 25)
inventaris.tambah_produk("P003", "Keyboard Mechanical", 450000, 15)

while True:
    print("\n================================")
    print(" SISTEM MANAJEMEN INVENTARIS")
    print("================================")
    print("1. Tambah Produk")
    print("2. Cari Produk")
    print("3. Hapus Produk")
    print("4. Tampilkan Semua Produk")
    print("5. Keluar")
    print("================================")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        print("\n--- TAMBAH PRODUK ---")
        id_produk = input("Masukkan ID Produk: ")
        nama = input("Masukkan Nama Produk: ")

        try:
            harga = int(input("Masukkan Harga Produk: "))
            stok = int(input("Masukkan Stok Produk: "))

            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif!")
            else:
                inventaris.tambah_produk(
                    id_produk, nama, harga, stok
                )
        except ValueError:
            print("Harga dan stok harus berupa angka!")

    elif pilihan == "2":
        print("\n--- CARI PRODUK ---")
        id_produk = input("Masukkan ID Produk: ")
        inventaris.cari_produk(id_produk)

    elif pilihan == "3":
        print("\n--- HAPUS PRODUK ---")
        id_produk = input("Masukkan ID Produk: ")
        inventaris.hapus_produk(id_produk)

    elif pilihan == "4":
        inventaris.tampilkan_produk()

    elif pilihan == "5":
        print("Terima kasih. Program selesai.")
        break

    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
