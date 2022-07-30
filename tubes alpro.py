from cmath import pi


def halo():
    print("++++++++++ Selamat datang ++++++++++")
    print("++++++++++++++++ Di ++++++++++++++++")
    print("++++++++++++ Pinjam Buku +++++++++++")
    print("[1] meminjam buku") 
    print("[2] mengembalikan buku")
    print("[3] menambah stok buku baru") 
    print("[4] menghapus stok buku")
    print("[5] Mengurutkan data peminjam sesuai nama")
    print('[6] Menutup Aplikasi')
    print("Note : setelah menambahkan buku mohon")
    print("       tutup aplikasi terlebih dahulu")
    pilihan1 = eval(input("Silahkan Masukan Pilihan : "))
    if pilihan1 == 1:
        pinjam()
    elif pilihan1 == 2:
        kembali()
    elif pilihan1 == 3:
        tambah()
    elif pilihan1 == 4:
        hapus()
    elif pilihan1 == 5:
        urut()
    elif pilihan1 == 6:
        quit()
    else :
        print("Pilihan salah, mohon masukan pilihan yang benar!")
        halo()

def pinjam():
        data_buku = open("list_buku.txt", "r")
        pisah = [line.rstrip("\n") for line in data_buku]
        print(pisah)
        print("Masukan nama peminjam : ", end="")
        data_buku.close()
        nama_pinjam=str(input()).title()
        print("Masukan NIM peminjam : ", end="")
        nim_pinjam=str(input())
        print("Masukan pilihan buku : ", end="")
        pilih = int(input())
        daftarbuku = [pilih]
        bukunya = []
        for index in daftarbuku:
            bukunya.append(pisah[index])
        print("Masukan tanggal peminjaman buku : ", end="")
        tanggal_pinjam=str(input()).title()
        print("Masukan tanggal pengembalian buku : ", end="")
        tanggal_balik=str(input()).title()
        print ("Apakah ingin mengubah data peminjaman buku?")
        print ("[1] Untuk meminjam buku lagi (Maksimal 2 Buku)")
        print ("[2] Jika ingin mengubah data peminjam")
        print ("[3] Jika ingin membatalkan peminjaman")
        print ('[4] Jika tidak ingin menambahkan buku yang ingin dipinjam')
        print ('[5] Jika Ingin mencari data peminjam yang baru di masukan')
        print ("Silahkan masukkan pilihan : ", end="")
        pilihan2 = str(input())
        if pilihan2 == "1":
            print("Masukan pilihan buku : ", end="")
            pilih2 = int(input())
            daftarbuku2 = [pilih2]
            bukunya2 = []
            for index2 in daftarbuku2:
                bukunya2.append(pisah[index2])
            h = open('peminjam.txt', 'a')
            h.write('\n')
            h.writelines(nama_pinjam)
            h.write(' ')
            h.writelines(nim_pinjam)
            h.write(' ')
            h.writelines(bukunya)
            h.write(' & ')
            h.writelines(bukunya2)
            h.write(' ')
            h.writelines(tanggal_balik)
            h.close
            print("="*66)
            print("="*66)
            print("="*66)
            print("============== Maksimal Peminjaman Hanya 2 Buku ==================")
            print("= anda sudah mengisi data yang dibutuhkan, mohon tunggu sebentar =")
            print("="*66)
            print("="*66)
            print("="*66)
            print("Peminjam dengan nama", nama_pinjam, "dengan nim", nim_pinjam,)
            print("meminjam buku dengan judul", bukunya,)
            print("dan", bukunya2, "akan dikembalikan pada", tanggal_balik)
            halo()
        elif pilihan2 == "2":
            print("Masukan jenis data yang ingin diubah")
            print("[1] Untuk mengubah nama peminjam")
            print("[2] Untuk mengubah nim peminjam")
            print("[3] Untuk mengubah tanggal pengembalian")
            print("Silahkan masukan pilihan anda : ", end="")
            update_data=int(input())
            if update_data == 1:
                print("Masukan nama baru : ")
                nama_pinjam=str(input()).title()
                print("==================================================================")
                print("==================================================================")
                print("==================================================================")
                print("======== update berhasil dilakukan, mohon tunggu sebentar ========")
                print("==================================================================")
                print("==================================================================")
                print("Peminjam dengan nama", nama_pinjam, "dengan nim", nim_pinjam, "meminjam buku")
                print("dengan judul", bukunya)
                print("akan dikembalikan pada", tanggal_balik)
                print("==================================================================")
                print("==================================================================")
                print("==================================================================")
                print("==================================================================")
                halo()
            elif update_data == 2:
                print("Masukan NIM baru : ", end="")
                nim_pinjam=str(input())
                print("==================================================================")
                print("==================================================================")
                print("==================================================================")
                print("======== update berhasil dilakukan, mohon tunggu sebentar ========")
                print("==================================================================")
                print("==================================================================")
                print("Peminjam dengan nama", nama_pinjam, "dengan nim", nim_pinjam, "meminjam buku")
                print("dengan judul", bukunya)
                print("akan dikembalikan pada", tanggal_balik)
                print("==================================================================")
                print("==================================================================")
                print("==================================================================")
                print("==================================================================")
                halo()
            elif update_data == 3:
                print("Masukan tanggal pengembalian baru : ", end="")
                tanggal_balik=str(input()).title()
                print("==================================================================")
                print("==================================================================")
                print("==================================================================")
                print("======== update berhasil dilakukan, mohon tunggu sebentar ========")
                print("==================================================================")
                print("==================================================================")
                print("Peminjam dengan nama", nama_pinjam, "dengan nim", nim_pinjam, "meminjam buku")
                print("dengan judul", bukunya)
                print("akan dikembalikan pada", tanggal_balik)
                print("==================================================================")
                print("==================================================================")
                print("==================================================================")
                print("==================================================================")
                halo()
            else:
                print("Pilihan salah! kembali ke menu utama")
                halo()

        elif pilihan2 == "3":
            print('Pilihan dibatalkan, kembali ke menu awal')
            halo()

        elif pilihan2 == "4":
            h = open('peminjam.txt', 'a')
            h.write('\n')
            h.writelines(nama_pinjam)
            h.write(' ')
            h.writelines(nim_pinjam)
            h.write(' ')
            h.writelines(bukunya)
            h.write(' ')
            h.writelines(tanggal_balik)
            h.close
            print("==================================================================")
            print("==================================================================")
            print("==================================================================")
            print("= anda sudah mengisi data yang dibutuhkan, mohon tunggu sebentar =")
            print("==================================================================")
            print("==================================================================")
            print("Peminjam dengan nama", nama_pinjam, "dengan nim", nim_pinjam, "meminjam buku")
            print("dengan judul", bukunya)
            print("akan dikembalikan pada", tanggal_balik)
            print("==================================================================")
            print("==================================================================")
            print("==================================================================")
            print("==================================================================")
            halo()
        elif pilihan2 == '5':
            h = open('peminjam.txt', 'a')
            h.write('\n')
            h.writelines(nama_pinjam)
            h.write(' ')
            h.writelines(nim_pinjam)
            h.write(' ')
            h.writelines(bukunya)
            h.write(' ')
            h.writelines(tanggal_balik)
            h.close
            searching = input('Masukan kata yang ingin dicari : ').title()
            if searching == nama_pinjam:
                print('Data yang anda cari sudah ketemu')
            elif searching == nim_pinjam:
                print('Data yang anda cari sudah ketemu')
            elif searching == tanggal_pinjam:
                print('Data yang anda cari sudah ketemu')
            elif searching == tanggal_balik:
                print('Data yang anda cari sudah ketemu')
            else:
                print('Data yang dimasukan salah!')
        else:
            print("Pilihan salah! Kembali ke menu utama")
            halo()
        

def kembali():
        data_buku = open("list_buku.txt", "r")
        pisah = [line.rstrip("\n") for line in data_buku]
        print("List data buku yang dapat dipinjam : ")
        print(pisah)
        print("Masukan Nama peminjam : ", end="")
        nama = str(input()).title()
        print("Masukan NIM Peminjam : ", end="")
        nim = int(input())
        print("Masukan tangal peminjaman : ", end="")
        tanggal_pinjam = str(input()).title()
        print("Masukan tanggal pengembalian : ", end="")
        tanggal_balik = str(input()).title()
        print("Masukan pilihan buku yang ingin dikembalikan : ", end="")
        pilih = int(input())
        daftarbuku = [pilih]
        bukunya = []
        for index in daftarbuku:
            bukunya.append(pisah[index])
        print("Apakah ada buku yang ingin dikembalikan lagi?")
        print("[1] Jika buku yang dipinjam 2")
        print("[2] Jika buku yang dipinjam hanya 1")
        print("Silahkan masukan pilihan : ", end="")
        pilihan_balik = str(input())
        if pilihan_balik == "1":
            print("Masukan pilihan buku kedua yang ingin dikembalikan : ", end="")
            pilih2 = int(input())
            daftarbuku2 = [pilih2]
            bukunya2 = []
            for index2 in daftarbuku2:
                bukunya2.append(pisah[index2])
            print("[ ========================================================= ]")
            print("[ ========================================================= ]")
            print("[ Peminjam dengan nama", nama, "dan nim", nim, "]")
            print("[ telah mengembalikan buku", bukunya, "]")
            print("[ dan", bukunya2, "pada tanggal", tanggal_balik, "]")
            print("[ ========================================================= ]")
            print("[ ================= Kembali ke menu awal ================== ]")
            print("[ ========================================================= ]")
            halo()
        if pilihan_balik == "2":
            print("[ ========================================================= ]")
            print("[ ========================================================= ]")
            print("[ Peminjam dengan nama", nama, "dan nim", nim, "]")
            print("[ telah mengembalikan buku", bukunya, "]")
            print("[ pada tanggal", tanggal_balik, "]")
            print("[ ========================================================= ]")
            print("[ ================= Kembali ke menu awal ================== ]")
            print("[ ========================================================= ]")
            halo()        
            
def tambah():
        data_buku2 = open("list_buku.txt", "r+")
        print(data_buku2.readlines())
        data_buku2.close()
        print("Masukan judul buku baru : ", end="")
        judul_baru = str(input()).title()
        print("Masukan nomor seri buku : ", end="")
        seri_baru = str(input())
        f = open("list_buku.txt", "a")
        f.write("\n")
        f.writelines(str(judul_baru))
        f.write(" (")
        f.writelines(str(seri_baru))
        f.write(")")
        f.close
        print("Apakah ada buku lain yang ingin ditambahkan?")
        print("[1] Untuk menambahkan buku lagi")
        print("[2] Jika tidak ada yang ingin ditambahkan lagi")
        print("Silahkan masukan pilihan : ", end="")
        pilihan3 = str(input())
        if pilihan3 == "1":
            print("Masukan judul buku baru : ", end="")
            judul_baru2 = str(input()).title()
            print("Masukan nomor seri buku : ", end="")
            seri_baru2 = str(input())
            f = open("list_buku.txt", "a")
            f.write("\n")
            f.writelines(str(judul_baru2))
            f.write(" (")
            f.writelines(str(seri_baru2))
            f.write(")")
            f.close
        elif pilihan3 == "2":
            halo()

def hapus():
        data_buku = open("list_buku.txt", "r")
        pisah = [line.rstrip("\n") for line in data_buku]
        print(pisah)
        print("Masukan nama buku yang ingin dihapus : ", end="")
        buku_hapus = str(input()).title()
        inti=0
        for j in pisah:
            if buku_hapus == pisah[inti]:
                a = pisah.remove(buku_hapus)
                data_buku.close()
                with open("list_buku.txt", "w") as hapusbuku:
                    for index in pisah:
                        hapusbuku.write('%s\n' % index)
            inti+=1
        print("Apakah ada buku lagi yang ingin dikurangi ?")
        print("[1] Untuk menghapus buku lagi")
        print("[2] Jika tidak ada")
        print("Masukan pilihan : ", end="")
        pilihapus=str(input())
        if pilihapus == "1":
            data_buku = open("list_buku.txt", "r")
            pisah = [line.rstrip("\n") for line in data_buku]
            print(pisah)
            print("Perhatikan spasi dan jangan ada huruf dan angka yang kurang")
            print('contoh : belajar berkebun (2817318)')
            print("Masukan nama buku yang ingin dihapus : ", end="")
            buku_hapus = str(input()).title()
            inti=0
            for j in pisah:
                if buku_hapus == pisah[inti]:
                    a = pisah.remove(buku_hapus)
                    data_buku.close()
                    with open("list_buku.txt", "w") as hapusbuku:
                        for index in pisah:
                            hapusbuku.write('%s\n' % index)
                inti+=1
        print("[ ========================================================= ]")
        print("[ ================= Kembali ke menu awal ================== ]")
        print("[ ========================================================= ]")
        halo()

def urut():
    def sorting(filename):
        infile = open(filename)
        words = []
        for line in infile:
            temp = line.split('\n')
            for i in temp:
                words.append(i)
        infile.close()
        words.sort()
        print('data telah di urutkan')
        print(words)
    sorting("peminjam.txt")
    halo()
halo()
