print("--------------------------------")
print("|      WELCOME TO MY           |")
print("|          CODES               |")
print("|     MAHENDRA CAHYANTO        |")
print("--------------------------------")

Menu = int(input("Masukan Pilihan (1-4) : "))

if Menu == 1:
    AngkaPertama = int(input("Masukan Bilangan 1 : "))
    AngkaKedua = int(input("Masukan Bilangan 2 : "))

    HasilPenjumlahan = AngkaPertama + AngkaKedua

    print("Angka Pertama : ", AngkaPertama)
    print("Angka Kedua   : ", AngkaKedua)

    print("Hasil Penjumlahan : ", HasilPenjumlahan)
elif Menu == 2:
    AngkaPertama = int(input("Masukan Bilangan 1 : "))
    AngkaKedua = int(input("Masukan Bilangan 2 : "))

    HasilPengurangan = AngkaPertama - AngkaKedua

    print("Angka Pertama : ", AngkaPertama)
    print("Angka Kedua   : ", AngkaKedua)

    print("Hasil Pengurangan : ", HasilPengurangan)
elif Menu == 3:
    AngkaPertama = int(input("Masukan Bilangan 1 : "))
    AngkaKedua = int(input("Masukan Bilangan 2 : "))

    HasilPerkalian = AngkaPertama * AngkaKedua

    print("Angka Pertama : ", AngkaPertama)
    print("Angka Kedua   : ", AngkaKedua)

    print("Hasil Perkalian : ", HasilPerkalian)
elif Menu == 4:
    AngkaPertama = int(input("Masukan Bilangan 1 : "))
    AngkaKedua = int(input("Masukan Bilangan 2 : "))

    HasilPembagian = AngkaPertama / AngkaKedua

    print("Angka Pertama : ", AngkaPertama)
    print("Angka Kedua   : ", AngkaKedua)

    print("Hasil Pembagian : ", HasilPembagian)
else:
    print("Error")