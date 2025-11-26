import math
# Rumus volume Kubus
def kubus(rusuk):
    hasil = math.pow(rusuk, 3)
    return hasil

# Rumus volume Balok
def balok(p,l,t):
    hasil = p * l * t
    return hasil

# Rumus volume Prisma
def prisma(alas,tinggi_segitiga,tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi_segitiga
    hasil = luas_alas * tinggi_prisma
    return hasil

# Rumus volume Tabung
def tabung(jari_jari,tinggi):
    alas = 22/7 * math.pow(jari_jari,2)
    hasil = alas * tinggi
    return hasil
print(tabung(7,10))

# Rumus volume kerucut
def kerucut(r,t):
    hasil = 1/3 * 22/7 * pow(r,2) * t
    return hasil
print(kerucut(7,10))