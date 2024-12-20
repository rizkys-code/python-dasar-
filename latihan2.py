usia =int(input("Berapa usia anda:"))
izin_mengemudi =(input("Apakah anda sudah memiliki surat izin mengemudi:"))
pengalaman_mengemudi =int(input("Berapa tahun pengalaman anda mngemudi:"))

#proses
if (usia >= 20  and pengalaman_mengemudi >= 3) or usia >= 25 and izin_mengemudi=="sudah punya":
    print("Anda di terima")

else:
    print("Maaf anda tidak di terima")