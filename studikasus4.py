gaji_pokok = int(input("masukan gaji pokok (dalam satuan rupiah):"))
uang_transport = int(input("masukan uang transport (dalam satuan rupiah): "))
jumlah_kehadiran = int(input("masukan jumlah kehadiran (dalam satuan hari): "))
pajak = int(input("masukan pajak anda (dalam satuan rupiah): "))

total_transport = uang_transport*jumlah_kehadiran
total_gaji = gaji_pokok+total_transport
total_pajak = 10/100 * total_gaji
gaji_bersih = gaji_pokok - total_pajak

print("Total gaji:", total_gaji)
print("Total pajak:", total_pajak)
print("Gaji Bersih:", gaji_bersih)