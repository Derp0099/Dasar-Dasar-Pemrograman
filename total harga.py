
JP = int(input('Masukkan Jumlah Pembelian:'))
TH = int(input("Masukkan total harga:"))
#JP=Jumlah Pembelian, TH=total harga

if JP > 100 :
    print("Anda dapat diskon 10%")
    print("Total Belanja anda", TH*0.9)
else :
    print('tidak dapat diskon')