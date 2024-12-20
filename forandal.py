saldo = int(input("Masukan saldo anda:"))
bunga = float(input("Masukan bunga nya :"))


for bulan in range(10):
    bungaBulan = saldo * bunga
    saldo = saldo + bungaBulan
print(bungaBulan)
print(saldo,"Rp")
