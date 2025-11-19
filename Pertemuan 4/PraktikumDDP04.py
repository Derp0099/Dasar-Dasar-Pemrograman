#Soal 1: Bilangan Genap atau Ganjil
#Buatlah program yang meminta pengguna untuk memasukkan sebuah bilangan bulat.
# Program harus menentukan apakah bilangan tersebut genap atau ganjil menggunakan if dan if else.

print("======Mencetak Bilangan Genap dan Ganjil=======")
bilangan = int(input("Masukkan Bilangan:"))

if bilangan % 2 == 0:
    print("Bilangan Genap")
else :
    print("Bilangan Ganjil")
    
#Soal 2: Nilai Ujian
#Buatlah program yang meminta pengguna untuk memasukkan nilai ujian.
# Jika nilai lebih besar atau sama dengan 75, cetak "Lulus".
# Jika tidak, cetak "Tidak Lulus". Gunakan if dan if else.

print("======Mencetak nilai========")
nilai = int(input("Masukkan Nilai:"))

if nilai >=75 :
    print("Lulus")    
else :
    print("Tidak Lulus 👎")
    
#Soal 3: Cek Usia dan Status
#Buatlah program yang meminta pengguna untuk memasukkan usia. 
#Program harus mencetak "Dewasa" jika usia lebih besar atau sama dengan 18,
#dan "Anak-anak" jika kurang dari 18.
#Tambahkan kondisi untuk mencetak "Remaja" jika usia antara 13 dan 17 menggunakan if and.

print('=======Cek Usia dan Status=======')
Usia = int(input('Masukkan Usia Anda:'))

if Usia >= 90 :
    print('Sepuhh')
elif Usia >= 18:
    print('Dewasa')
elif 13<Usia<17 :
    print('Remaja')
else :
    print('Anak-Anak')
    
#Soal 4: Cek Keanggotaan
#Buatlah program yang meminta pengguna untuk memasukkan status keanggotaan (misalnya "gold", "silver", atau "bronze").
#Jika statusnya "gold" atau "silver", cetak "Selamat! Anda mendapatkan diskon".Gunakan if or.

print('=======Status Kenaggotaan========')
stat = input("Masukkan Status Anda:")

if stat =="Gold"or stat =="Silver":
    print("Selamat! Anda Mendapatkan Diskon")
else:
    print("Anda Tidak Dapat Diskon")

#jika suhu >= 100 print air mendidih
#jika suhu <=0 print air beku
#jika tidak print air keadaan hangat atau cair

print('Keadaan Air')
suhu = int(input('Masukkan Suhu:'))

if suhu >= 100 :
    print('Air Mendidih')
elif suhu <= 0 :
    print('Air Membeku')
else :
    print('Air dalam keadaan hangat atau cair')
    
#Soal 5: Pembelian Diskon
#Buatlah program yang meminta pengguna untuk memasukkan jumlah pembelian.
#Jika jumlahnya lebih dari 100, beri diskon 10% menggunakan shorthand if.
#Cetak total harga setelah diskon jika ada, jika tidak, cetak total harga tanpa diskon.

JP = int(input('Masukkan Jumlah Pembelian:'))
TH = int(input("Masukkan total harga:"))
#JP=Jumlah Pembelian, TH=total harga

if JP > 100 :
    print("Anda dapat diskon 10%")
    print("Total Belanja anda", TH*0.9)
else :
    print('tidak dapat diskon')