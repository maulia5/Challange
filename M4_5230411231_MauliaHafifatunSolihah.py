class Debitur:
    def __init__(self, nama, ktp, limit):
        self.nama = nama
        self.ktp = ktp
        self.limit = limit

class Pinjaman:
    def __init__(self, nama, jml_pinjaman, bunga, bulan):
        self.nama = nama
        self.jml_pinjaman= jml_pinjaman
        self.bunga = bunga
        self.bulan = bulan
        self.angsuran_bulanan = self.hitung_bulanan()

    def hitung_bulanan(self):
        angsuran_pokok = self.jml_pinjaman / self.bulan
        angsuran_bulanan = angsuran_pokok * (1 + self.bunga)
        return angsuran_bulanan
    
daftar_debitur = []
daftar_pinjaman = []

def tampil_debitur():
    if len(daftar_debitur) == 0:
        print("Belum ada debitur yang terdaftar.")
        return
    
    for debitur in daftar_debitur:
        print(f"Nama: {debitur.nama}, KTP: {debitur.ktp}, Limit: {debitur.limit}")

def tambah_debitur():
    nama = input("Masukkan Nama Debitur: ")
    ktp = input("Masukkan KTP Debitur: ")

    for debitur in daftar_debitur:
        if debitur.ktp == ktp:
            print("KTP yang dimasukkan sudah ada.")
            return

    limit = float(input("Masukkan Limit Pinjaman: "))
    debitur_baru = Debitur(nama, ktp, limit)
    daftar_debitur.append(debitur_baru)
    print(f"Debitur dengan nama {nama} berhasil ditambahkan.")
        
def cari_debitur():
    nama = input("Masukkan nama debitur yang anda cari: ")

    for debitur in daftar_debitur:
        if debitur.nama == nama:
            print(f"Nama: {debitur.nama}, dengan KTP: {debitur.ktp}, memiliki Limit Pinjaman: {debitur.limit}")
            return debitur
        
        for debitur in daftar_debitur:
            if debitur.nama == nama:
                print(f"Nama: {debitur.nama}, dengan KTP: {debitur.ktp}, memiliki Limit Pinjaman: {debitur.limit}")
                return debitur
        
        print("Debitur tidak ditemukan.")
        return None

def tambah_pinjaman():
    nama = input("Masukkan Nama Debitur: ")
    debitur = None

    for i in daftar_debitur:
        if i.nama == nama:
            debitur = i
            break

    if debitur is None:
        print("Nama Debitur tidak ada")
        return
    
    jml_pinjaman = float(input("Masukkan jumlah pinjaman yang diinginkan: "))
    bunga = float(input("Masukkan bunga: "))
    bulan = int(input("Masukkan jangka waktu yang ditentukan dalam bulan: "))

    total_pinjaman_saat_ini = sum(pinjaman.jml_pinjaman for pinjaman in daftar_pinjaman if pinjaman.debitur == debitur)
    if total_pinjaman_saat_ini + jml_pinjaman > debitur.limit:
        print("Jumlah pinjaman yang diajukan melebihi limit debitur.")
        return
    
    pinjam_baru = Pinjaman(nama, jml_pinjaman, bunga, bulan)
    daftar_pinjaman.append(pinjam_baru)
    print(f"Pinjaman atas nama {nama}, berhasil ditambahkan.")

def tampil_pinjaman():
    if len(daftar_pinjaman) == 0:
        print("Belum ada pinjaman yang terdaftar.")
        return
    
    for pinjaman in daftar_pinjaman:
        print(f"Nama: {pinjaman.nama}, Jumlah Pinjaman: {pinjaman.jml_pinjaman}, Bunga: {pinjaman.bunga}, Bulan: {pinjaman.bulan}, Angsuran Bulanan: {pinjaman.angsuran_bulanan}")

def tampilanmenu():
    while True:
        print("="*10 +"Aplikasi Admin Pinjol"+ "="*10)
        print("1. Kelola Debitur")
        print("2. Pinjaman")
        print("3. Keluar")
        pilih  = input("Masukkan pilihan 1/2/3:")

        if pilih == '1':
            while True:
                print("="*10 +"Kelola Debitur"+ "="*10)
                print("1. Tampilkan Semua Debitur")
                print("2. Cari Debitur")
                print("3. Tambah Debitur")
                print("4. Keluar")
                pilih  = input("Masukkan pilihan 1/2/3/4:")
            
                if pilih == '1':
                    print("="*10 + "Tampil Debitur" + "="*10)
                    tampil_debitur()

                elif pilih == '2':
                    print(" >>>>> Cari Debitur")
                    cari_debitur()

                elif pilih == '3':
                    print("="*10 + "Tambah Debitur" + "="*10)
                    tambah_debitur()

                else:
                    break
                
        elif pilih == '2':
            while True:
                print("="*10 + "Kelola Pinjaman" + "="*10)
                print("1. Tambah Pinjaman")
                print("2. Tampilkan Pinjaman")
                print("3. Keluar")
                pilih  = input("Masukkan pilihan 1/2/3: ")

                if pilih == '1':
                    print("="*10 + "Tambah Pinjaman" + "="*10)
                    tambah_pinjaman()

                elif pilih == '2':
                    print("="*10 + "Tampilkan Pinjaman" + "="*10)
                    tampil_pinjaman()

                else:
                    break

        elif pilih == '3':
           print("Terima kasih telah memakai program ini")
           break

        else:
            print("\n")


tampilanmenu()

                    