#Tugas 1
NamaKendaraan = "Odyssey"
JenisKendaraan = "Mobil"
ccKendaraan = 2356
WarnaKendaraan = "Silver"
RodaKendaraan = "Roda 4"

data_kendaraan = [
    NamaKendaraan, JenisKendaraan, ccKendaraan, WarnaKendaraan, RodaKendaraan
]

HargaKendaraan = 380000000
TipeKendaraan = "Prestige"
print(data_kendaraan)

data_kendaraan.append(HargaKendaraan)
data_kendaraan.append(TipeKendaraan)
print(data_kendaraan)

MerkKendaraan = "Honda"
data_kendaraan.insert(2,MerkKendaraan)
print(data_kendaraan)

#Tugas 2
rumus = int(input("""     
Rumus Bangun Datar                          
1: persegi
2: lingkaran
3: segitiga
Masukkan Pilihan:
"""))

match rumus:
    case 1:
        #S: Sisi
        S = int(input("masukkan sisi="))
        hasil = S * S
        print("hasil=",hasil)
    case 2:
        #R: jari jari
        R = int(input("masukkan jari jari="))
        hasil = 22/7 * R * R
        print("hasil=",hasil)
    case 3:
        #A: alas
        #T: tinggi
        A = int(input("masukkan alas="))
        T = int(input("masukkan tinggi="))
        hasil = A * T / 2
        print("hasil=",hasil)
    case _ :
        print("Salah Memasukkan Pilihan")