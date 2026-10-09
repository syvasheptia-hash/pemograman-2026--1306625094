#identitas
print("Program Mencari Faktor Bilangan")
print("Nama : (syva sheptia melani)")
print("NIM  : (1306625094)")
print("Kelas: (Fisika C)")
print()

#program untuk mencari faktor bilangan
while True:
    hasil =[]
    n = int(input("Masukkan bilangan < 100 (selesai= 0) ="))
    if n == 0:
        break
    for i in range(1, n+1):
        if n % i == 0:
            hasil.append(i)
    print('Bilangan', 1, 'faktornya=', hasil)

print("SELESAI")

    