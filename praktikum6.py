#Belanja.py

#input data
kode_barang = (input("Masukan kode barang:"))
nama_barang = (input("Masukan nama barang:"))
harga_satuan = (input("Masukan harga satuan:"))
jumlah_beli = (input("Masukan jumlah beli:"))

#proses
total_harga = int(harga_satuan) * int(jumlah_beli)

if total_harga >= 200000:
    potongan = 0.03 * total_harga
else: 
    potongan = 0

total_bayar = total_harga - potongan

#output
print("\nData barang")
print("Total bayar",total_bayar)
