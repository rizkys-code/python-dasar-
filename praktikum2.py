presensi = int(input("masukan jumlah absen dalam:"))
nilai_tugas = int(input("masukan nilai tugas:"))
nilai_uts = int(input("masukan nilai UTS:"))
nilai_uas = int(input("masukan nilai uas:"))

Nilai_akhir = (0.1*presensi) + (0.2*nilai_tugas) + (0.3*nilai_uts) + (0.4*nilai_uas)

print("presensi:",presensi)
print("nilai tugas:",nilai_tugas)
print("nilai uts:",nilai_uts)
print("nilai uas:", nilai_uas)
print("nilai akhir:", Nilai_akhir) 