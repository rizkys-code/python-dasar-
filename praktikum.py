#input
kode_barang = input("masukan kode barang:")
nama_barang = input("masukan nama barang:")
harga_satuan = input("masukan harga satuan:")
jumlah_beli = input("masukan mjumlah beli:")

#proses
total_harga = int(harga_satuan)* int(jumlah_beli)
pajak  = (total_harga) * (0.1)
bayar = (total_harga) + (pajak)



#output
print("\n")
print("==============")
print("\ndata barang ")
print("===============")
print("kode barang:",kode_barang)
print("nama barang:",nama_barang)
print("harga satuan:",harga_satuan)
print("jumlah beli:",jumlah_beli)
print("total harga:RP",total_harga)
print("hasil potongan pajak: RP",pajak)
print("total bayar:RP",bayar)



