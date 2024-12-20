#input
kode_barang = input("masukan kode barang:")
nama_barang = input("masukan nama barang:")
harga_satuan = input("masukan harga satuan dalam bentuk rupiah:")
jumlah_beli = input("masukan jumlah beli:")

#proses 
total_harga = int(harga_satuan) * int(jumlah_beli)
pajak = (total_harga) * (0.1)
jumlah_bayar= (total_harga) + (pajak)

#output
print("\n")
print("================")
print("\ndata barang")
print("=================")
print("kode barang:",kode_barang)
print("nama baran:",nama_barang)
print("harga satuan:",harga_satuan)
print("jumlah beli:",jumlah_beli)
print("jumlah bayar:",pajak)
print("jumlah bayar: RP",jumlah_bayar)
