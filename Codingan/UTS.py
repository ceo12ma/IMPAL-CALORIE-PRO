import math

def hitung_luas_lingkaran(jari_jari):
    # Menghitung luas lingkaran menggunakan rumus Pi * r^2
    return math.pi * (jari_jari ** 2)

def hitung_luas_persegi_panjang(panjang, lebar):
    # Menghitung luas persegi panjang menggunakan rumus panjang * lebar
    return panjang * lebar

def hitung_luas_permukaan_tabung(jari_jari, tinggi):
    # Menghitung luas permukaan tabung menggunakan rumus 2 * Pi * r * (r + tinggi)
    return 2 * math.pi * jari_jari * (jari_jari + tinggi)

def tampilkan_menu():
    # Menampilkan menu utama
    print("====================================")
    print("       MODUL MATEMATIKA SMP        ")
    print("====================================")
    print("Pilihlah opsi perhitungan:")
    print("1. Hitung Luas Lingkaran")
    print("2. Hitung Luas Persegi Panjang")
    print("3. Hitung Luas Permukaan Tabung")
    print("4. Keluar")
    print("====================================")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")
        
        if pilihan == '1':
            # Menghitung Luas Lingkaran
            jari_jari = float(input("Masukkan jari-jari lingkaran: "))
            luas = hitung_luas_lingkaran(jari_jari)
            print(f"Luas Lingkaran = {luas:.2f}")
        
        elif pilihan == '2':
            # Menghitung Luas Persegi Panjang
            panjang = float(input("Masukkan panjang: "))
            lebar = float(input("Masukkan lebar: "))
            luas = hitung_luas_persegi_panjang(panjang, lebar)
            print(f"Luas Persegi Panjang = {luas:.2f}")
        
        elif pilihan == '3':
            # Menghitung Luas Permukaan Tabung
            jari_jari = float(input("Masukkan jari-jari tabung: "))
            tinggi = float(input("Masukkan tinggi tabung: "))
            luas = hitung_luas_permukaan_tabung(jari_jari, tinggi)
            print(f"Luas Permukaan Tabung = {luas:.2f}")
        
        elif pilihan == '4':
            # Keluar dari program
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__":
    main()
