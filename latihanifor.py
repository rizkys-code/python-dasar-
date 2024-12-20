usia1= int(input("masukan usia anda:"))
izin_orangtua =(input("Apakah anda mendapat izin dari orang tua anda?"))

if usia1 >= 18 or usia1 >= 16 and izin_orangtua== "sudah":


    print("Anda di perbolekan membeli tiket konser")
else: 
    print("Maaf anda tidak di perbolehkan membeli tiket konser")