# Program Konversi Suhu Celcius - Reamur - Fahrenheit

# Haeder dan Input Indentitas
print("Program Konversi Suhu\n")
print("Nama:syva sheptia melani")
print("NIM:1306625094")
print("Fisika C")
print()

#Input Parameter Suhu
suhu_awal = float(input("Suhu Awal ="))
suhu_akhir= float (input("Suhu Akhir ="))
selang = float(input("Selang ="))
print()

# Header Tabel
print("Tabel Konversi Suhu")
print(f"{'No.':<4} | {'Celcius':<10} | {'Reamur':<10} | {'Fahrenheit':<10}")
print("-"*45)

#Inisialisasi Variabel Perhitungan
c = suhu_awal
no = 1

#Perulangan while untuk perhitungan & cetak format tabel
while c <= suhu_akhir:
    r = 0.8* c
    f = (1.8 * c) + 32
  
    #cetak baris tabel dengan format rapi
    print(f"{no:<4}|{c:<10.2f}|{r:<10.2f}|{f:<10.2f}")
   
    c += selang
    no += 1
