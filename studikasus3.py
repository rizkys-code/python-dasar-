tarif_per_jam = 1457
KWH_awal = 2500
KWH_akhir = 2960

KWH_terpakai = KWH_akhir - KWH_awal
total = KWH_terpakai * tarif_per_jam

print("KWH terpakai:", KWH_terpakai)
print("Total:", total)