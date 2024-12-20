presensi =float(input("Massukan nilai presesnsi:"))
tugas =float(input("Massukan nilai tugas:"))
uts =float(input("Massukan nilai uts:"))
uas =float(input("Massukan nilai uas:"))

#proses
nilai_akhir= 0.1*presensi + 0.2*tugas + 0.3*uts + 0.4*uas

#if
if nilai_akhir >= 85 and nilai_akhir <= 100:
    print("Grade A:")
if nilai_akhir >= 80 and nilai_akhir <= 84:
    print("Grade A-")
if nilai_akhir >= 75 and nilai_akhir <= 79:
   print("Grade B+")
if nilai_akhir >= 70 and nilai_akhir <= 74:
    print("Grade B")
if nilai_akhir >= 60 and nilai_akhir <= 69:
    print("Grade C")
if nilai_akhir >= 0 and nilai_akhir <= 59:
    print("Grade D")

    
#output
print("Nilai akhir", nilai_akhir)
