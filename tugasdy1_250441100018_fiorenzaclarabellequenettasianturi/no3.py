jarak = float(input("Masukkan jarak tempuh (dalam km): "))
konsumsi_bbm_per_liter = float(input("Masukkan konsumsi BBM per liter (km/liter): "))
kapasitas_tangki = float(input("Masukkan kapasitas tangki (dalam liter): "))
harga_bbm_per_liter = float(input("Masukkan harga BBM per liter (Rp): "))

# menghitung total bbm yang dibutuhkan
total_bbm_dibutuhkan = jarak / konsumsi_bbm_per_liter

# cek apakah ada diskon 
if total_bbm_dibutuhkan > 3:
    harga_bbm_diskom = harga_bbm_per_liter - 500
else:
    harga_bbm_diskom = harga_bbm_per_liter

# menghitung total biaya
total_biaya = total_bbm_dibutuhkan * harga_bbm_diskom

# hitung berapa kali isi ulang
import math
jumlah_isi_ulang = math.ceil(total_bbm_dibutuhkan / kapasitas_tangki)

print ( "total bensin yang di butuhkan : liter", total_bbm_dibutuhkan)
print ("harga bensin per liter setelah diskon : Rp", harga_bbm_diskom)
print ("total biaya yang harus di keluarkan : Rp", total_biaya)
print ("jumlah isi ulang : ", jumlah_isi_ulang, "kali")