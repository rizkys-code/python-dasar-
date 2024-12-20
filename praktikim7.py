listA = []

n = int(input("Masukan nilai N:"))
harga = 7650

for i in range(0,5):
    print("Satuan ke-{} : ", format(i+1), (i+1)*harga)
    elist = [i+1, (i+1) * harga]

    listA.append(elist)

print("Elemen harga bensin adalah: ", listA)