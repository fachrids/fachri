bulan = int(input("Masukkan bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))

while bulan < 1 or bulan > 12:
    print("Bulan tidak valid!")
    bulan = int(input("Masukkan bulan (1-12): "))

# Menentukan tahun kabisat
kabisat = tahun % 400 == 0 or (tahun % 4 == 0 and tahun % 100 != 0)

print("Tahun kabisat:", kabisat)

if bulan == 2:
    if kabisat: 
        jumlah_hari = 29
    else:
        jumlah_hari = 28

elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
    jumlah_hari = 30

else:
    jumlah_hari = 31

print("Jumlah hari dalam bulan", bulan, "tahun", tahun, "adalah", jumlah_hari)
