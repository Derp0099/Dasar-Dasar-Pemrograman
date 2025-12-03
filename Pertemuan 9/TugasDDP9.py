# Tugas 4
def bilangan(angka):
    for i in range(1,angka):
        if i % 2 != 0:
            print(i, end=" ")
bilangan(20)
print()
# Tugas 3
print()
def nilai(n=0):
    if n <= 60:
        print(f'nilai {n} tidak lulus')
    elif n >60 and n <= 100:
        print(f'nilai {n} lulus')
    else :
        print(f'nilai {n} tidak diketahui')
nilai(80)
# Tugas 2
print()
def is_genap(n):
    return n % 2 == 0
print(is_genap(2))
# Tugas 1
def t(suhu_celcius):
    