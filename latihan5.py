kendaraan =["B 2004 YGA", "Toyota Supra", "2998cc", "merah"]
print (kendaraan)

kendaraan.append("2,1 M")
kendaraan.append(4)
print (kendaraan)

kendaraan.insert(2, "Toyota")
kendaraan.insert(3, "Mobil")
print (kendaraan)


print("Pilih bangun datar:")
print("1. Persegi")
print("2. Lingkaran")
print("3. Segitiga")

pilihan = int(input("Masukkan pilihan (1/2/3): "))

match pilihan:
    case 1:
        sisi = float(input("Masukkan panjang sisi persegi: "))
        luas = sisi*sisi
    case 2:
        jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))
        luas = 3,14*jari_jari*jari_jari
    case 3:
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        luas = alas*tinggi/2
    case _:
        print("Pilihan tidak valid.")
        luas = None

if luas is not None:
    print(f"Luas bangun datar adalah: {luas}")