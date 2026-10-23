
import pandas as pd
from pathlib import Path


def hitung_grade(na):
    if na >= 86:
        return "A"
    elif na >= 81:
        return "A-"
    elif na >= 76:
        return "B+"
    elif na >= 71:
        return "B"
    elif na >= 66:
        return "B-"
    elif na >= 61:
        return "C+"
    elif na >= 56:
        return "C"
    else:
        return "TL"


def main():
    print("Program Grading")
    print("Nama : Syva Sheptia Melani")
    print("NRM  : 1306625094")
    print("\nLAPORAN GRADING MAHASISWA")

    # Membaca file Excel dari folder yang sama
    file_excel = Path(__file__).with_name("DataNilai2.xlsx")

    try:
        df = pd.read_excel(file_excel)
    except FileNotFoundError:
        print("\nFile DataNilai2.xlsx tidak ditemukan.")
        print("Pastikan file Excel berada di folder yang sama.")
        return
    except Exception as e:
        print(f"\nGagal membaca file Excel: {e}")
        return

    # Memastikan jumlah kolom sesuai kebutuhan
    if len(df.columns) < 5:
        print("Error: Excel harus memiliki minimal 5 kolom.")
        return

    # Mengambil kolom berdasarkan posisi pada Excel
    col_nama = df.columns[0]
    col_lain = df.columns[2]
    col_uts = df.columns[3]
    col_uas = df.columns[4]

    # Rekapitulasi grade
    rekap = {
        "A": 0,
        "A-": 0,
        "B+": 0,
        "B": 0,
        "B-": 0,
        "C+": 0,
        "C": 0,
        "TL": 0
    }

    print("-" * 65)
    print(
        f"{'No':<5}"
        f"{'Nama Mahasiswa':<30}"
        f"{'Nilai Akhir':<15}"
        f"{'Grade':<10}"
    )
    print("-" * 65)

    total_mahasiswa = len(df)
    i = 0

    while i < total_mahasiswa:
        row = df.iloc[i]

        try:
            nama_mhs = str(row[col_nama])
            n_lain = float(row[col_lain])
            n_uts = float(row[col_uts])
            n_uas = float(row[col_uas])

            # Menghitung nilai akhir
            nilai_akhir = (
                (0.30 * n_lain)
                + (0.35 * n_uts)
                + (0.35 * n_uas)
            )

            # Menentukan grade
            grade = hitung_grade(nilai_akhir)

            # Menambahkan jumlah grade
            rekap[grade] += 1

            print(
                f"{i + 1:<5}"
                f"{nama_mhs:<30}"
                f"{nilai_akhir:<15.2f}"
                f"{grade:<10}"
            )

        except (ValueError, TypeError):
            print(
                f"{i + 1:<5}"
                f"Data nilai tidak valid"
            )

        i += 1

    print("-" * 65)
    print("\nREKAPITULASI NILAI")
    print("-" * 30)

    for grade, jumlah in rekap.items():
        print(f"Grade {grade:<5} = {jumlah}")

    print(f"Total Mahasiswa = {total_mahasiswa}")
    print("\nProgram selesai.")


if __name__ == "__main__":
    main()


