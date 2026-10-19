
def normalisasi_nama(nama):
    return " ".join(nama.strip().split()).title()


def buat_inisial(nama):
    kata = normalisasi_nama(nama).split()
    return "".join(k[0] for k in kata)


def normalisasi_kode(kode):
    kata = kode.strip().upper().split()
    return "-".join(kata)


nama = input("Nama mahasiswa: ")
kode = input("Kode kelas: ")

nama_bersih = normalisasi_nama(nama)
kode_bersih = normalisasi_kode(kode)
inisial = buat_inisial(nama)
jumlah_kata = len(nama_bersih.split())

print("\n--- Hasil Normalisasi Data Mahasiswa ---")
print("Nama bersih :", nama_bersih)
print("Kode kelas  :", kode_bersih)
print("Jumlah kata :", jumlah_kata)
print("Inisial     :", inisial)
