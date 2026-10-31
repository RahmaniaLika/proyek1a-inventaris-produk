
import time
from statistics import median

# =====================================
# 1. IMPLEMENTASI LINKED LIST
# =====================================

class Node:
    def __init__(self, id_produk):
        self.id_produk = id_produk
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Menambahkan data di akhir
    def tambah(self, id_produk):
        node_baru = Node(id_produk)

        if self.head is None:
            self.head = node_baru
            self.tail = node_baru
        else:
            self.tail.next = node_baru
            self.tail = node_baru

    # Mencari data
    def cari(self, id_produk):
        sekarang = self.head

        while sekarang is not None:
            if sekarang.id_produk == id_produk:
                return sekarang
            sekarang = sekarang.next

        return None

    # Menghapus data
    def hapus(self, id_produk):
        sekarang = self.head
        sebelumnya = None

        while sekarang is not None:
            if sekarang.id_produk == id_produk:
                if sebelumnya is None:
                    self.head = sekarang.next
                else:
                    sebelumnya.next = sekarang.next

                if sekarang == self.tail:
                    self.tail = sebelumnya

                return True

            sebelumnya = sekarang
            sekarang = sekarang.next

        return False


# =====================================
# 2. MEMBUAT DATA PENGUJIAN
# =====================================

JUMLAH_DATA = 10000
JUMLAH_ULANG = 1000

def buat_list():
    return [f"P{i}" for i in range(JUMLAH_DATA)]


def buat_dict():
    return {
        f"P{i}": f"Produk {i}"
        for i in range(JUMLAH_DATA)
    }


def buat_linked_list():
    data = LinkedList()

    for i in range(JUMLAH_DATA):
        data.tambah(f"P{i}")

    return data


# =====================================
# 3. FUNGSI PENGUKURAN WAKTU
# =====================================


def ukur_penambahan(fungsi_tambah, pembuat_data):
    hasil = []

    for _ in range(5):
        data = pembuat_data()

        mulai = time.perf_counter()

        fungsi_tambah(data)

        selesai = time.perf_counter()
        hasil.append(selesai - mulai)

    return median(hasil)


def ukur_pencarian(fungsi_buat, fungsi_cari):
    data = fungsi_buat()

    mulai = time.perf_counter()

    for _ in range(JUMLAH_ULANG):
        fungsi_cari(data, f"P{JUMLAH_DATA - 1}")

    selesai = time.perf_counter()

    return (selesai - mulai) / JUMLAH_ULANG


def ukur_penghapusan(fungsi_buat, fungsi_hapus):
    hasil = []
    target = f"P{JUMLAH_DATA // 2}"

    for _ in range(5):
        data = fungsi_buat()

        mulai = time.perf_counter()
        fungsi_hapus(data, target)
        selesai = time.perf_counter()

        hasil.append(selesai - mulai)

    return median(hasil)


# =====================================
# 4. FUNGSI OPERASI SETIAP STRUKTUR DATA
# =====================================

def tambah_list(data):
    for i in range(JUMLAH_DATA):
        data.append(f"P{i}")


def tambah_dict(data):
    for i in range(JUMLAH_DATA):
        data[f"P{i}"] = f"Produk {i}"


def tambah_linked(data):
    for i in range(JUMLAH_DATA):
        data.tambah(f"P{i}")


def cari_list(data, target):
    return target in data


def cari_dict(data, target):
    return target in data


def cari_linked(data, target):
    return data.cari(target)


def hapus_list(data, target):
    if target in data:
        data.remove(target)


def hapus_dict(data, target):
    data.pop(target, None)


def hapus_linked(data, target):
    data.hapus(target)


# =====================================
# 5. MENJALANKAN PENGUJIAN
# =====================================

print("========================================")
print(" PERBANDINGAN KOMPLEKSITAS STRUKTUR DATA")
print("========================================")
print("Jumlah data :", JUMLAH_DATA)
print("Pengulangan pencarian :", JUMLAH_ULANG)

# Pengujian penambahan

# Pengujian penambahan
tambah_dictionary = ukur_penambahan(tambah_dict, dict)
tambah_python_list = ukur_penambahan(tambah_list, list)
tambah_linked_list = ukur_penambahan(
    tambah_linked, LinkedList
)


# Pengujian pencarian
cari_dictionary = ukur_pencarian(buat_dict, cari_dict)
cari_python_list = ukur_pencarian(buat_list, cari_list)
cari_linked_list = ukur_pencarian(buat_linked_list, cari_linked)

# Pengujian penghapusan
hapus_dictionary = ukur_penghapusan(buat_dict, hapus_dict)
hapus_python_list = ukur_penghapusan(buat_list, hapus_list)
hapus_linked_list = ukur_penghapusan(
    buat_linked_list, hapus_linked
)

# =====================================
# 6. MENAMPILKAN HASIL
# =====================================

def tampilkan_judul(judul):
    print("\n---", judul, "---")

def tampilkan_hasil(nama, waktu):
    print(f"{nama:<18}: {waktu:.8f} detik")

tampilkan_judul("HASIL PENAMBAHAN 10.000 DATA")
tampilkan_hasil("Dictionary", tambah_dictionary)
tampilkan_hasil("Python List", tambah_python_list)
tampilkan_hasil("Linked List", tambah_linked_list)

tampilkan_judul("HASIL PENCARIAN (RATA-RATA)")
tampilkan_hasil("Dictionary", cari_dictionary)
tampilkan_hasil("Python List", cari_python_list)
tampilkan_hasil("Linked List", cari_linked_list)

tampilkan_judul("HASIL PENGHAPUSAN")
tampilkan_hasil("Dictionary", hapus_dictionary)
tampilkan_hasil("Python List", hapus_python_list)
tampilkan_hasil("Linked List", hapus_linked_list)

print("\n========================================")
print(" PENGUJIAN SELESAI")
print("========================================")
