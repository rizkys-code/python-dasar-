jumlahpinjaman =5000
lamapinjaman =12
bungapinjaman =10000
biayaadmin =1000

jumlahangsuran = jumlahpinjaman *  bungapinjaman
jumlahbunga = 0.08 * jumlahpinjaman
total = jumlahangsuran + jumlahbunga

print("jumlah angsuran", jumlahangsuran)
print("lama pinjaman", lamapinjaman)
print("Total angsuran", total)
