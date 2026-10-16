import math

# Def Function McLaurin Sin
def mclaurin_sin(x, n):
    hasil = 0
    i = 0

    while i < n:
        suku = ((-1) ** i * x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        hasil = hasil + suku
        i = i + 1

    return hasil


# Def Function McLaurin Cos
def mclaurin_cos(x, n):
    hasil = 0
    i = 0

    while i < n:
        suku = ((-1) ** i * x ** (2 * i)) / math.factorial(2 * i)
        hasil = hasil + suku
        i = i + 1

    return hasil


# Program Utama
print("Program Sinus-Cosinus")
nama = input("Nama : Syva Sheptia Melani ")
nim = input("NIM  : 1306625094 ")

while True:
    sudut = float(input("Besar sudut (derajat) = "))

    x = math.radians(sudut)

    TV_sin = math.sin(x)
    TV_cos = math.cos(x)

    print()
    print("True value sin(x) =", format(TV_sin, ".6f"))
    print("True value cos(x) =", format(TV_cos, ".6f"))

    print()
    print("Jumlah | AV sin | ER sin (%) | AV cos | ER cos (%)")
    print("---------------------------------------------------")

    n = 1

    while True:
        AV_sin = mclaurin_sin(x, n)
        AV_cos = mclaurin_cos(x, n)

        ER_sin = abs((AV_sin - TV_sin) / TV_sin) * 100
        ER_cos = abs((AV_cos - TV_cos) / TV_cos) * 100

        print(n, "|", format(AV_sin, ".6f"), "|",
              format(ER_sin, ".6f") + "%", "|",
              format(AV_cos, ".6f"), "|",
              format(ER_cos, ".6f") + "%")

        if ER_sin < 5 and ER_cos < 5:
            break

        n = n + 1

    ulang = input("\nMau menghitung lagi (y/t)? ")

    if ulang == "t":
        break

print("Program selesai.")   

