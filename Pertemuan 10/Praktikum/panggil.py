import bangunruang as br, bangundatar as bd
# Panggil Bangun Ruang
print('---- BANGUN RUANG -----')
print(f'Volume Kubus dengan rusuk 3 adalah {br.kubus(3)}')
print(f'Volume Balok adalah {br.balok(4,5,2)}')
print(f'Volume Prisma Segitiga adalah {br.prisma(3,3,3)}')
print(f'Volume Tabung adalah {br.tabung(7,10)}')
print(f'Volume Kerucut adalah {br.kerucut(7,10)}')
# Panggil Bangun datar
print('---- BANGUN DATAR ----')
print(f'Luas persegi adalah {bd.persegi(5)}')
print(f'Luas persegi panjang adalah {bd.lpp(5,2)}')
print(f'Luas segitiga adalah {bd.segitiga(10,10)}')
print(f'Luas lingkaran adalah {bd.lingkaran(7)}')
print(f'Luas jajargenjang adalah {bd.jg(5,2)}')