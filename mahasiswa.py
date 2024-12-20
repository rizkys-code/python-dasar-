ipk = float(input("Masukan nilai rata rata kuimulatif anda:"))
pembayaran_uang =(input("apakah anda sudah membayar uang wisuda:"))
sertifikat = int(input ("masukan sertifkat yang sudah anda dapatkan "))

if ipk >= 3 and pembayaran_uang == "sudah bayar"  and sertifikat >=5:
   print("Boleh Mengikuti wisuda")

else:
   print("Tidak Boleh mengiktui wisuda")