biayaparkir = 1000
jammasuk =  (input("inputkan jam masuk: "))
jamkeluar =(input("inputkan jam keluar: "))

hours_enter , minutes_enter = map(int,jammasuk.split(':'))
hours_exit , minutes_exit = map(int, jamkeluar.split(':'))

total_menit = (hours_exit * 60 + minutes_exit) - (hours_enter * 60 + minutes_enter )
lama_parkir = total_menit / 60 
total_tagihan = lama_parkir * biayaparkir




print("Total menit", total_menit)
print("Lama parkir", lama_parkir)
print("Total tagihan", total_tagihan)
