listA = []

n = int(input("Ukuran list: "))
jum = 0

for i in range(0,n):
    print("input nilai u/ indeks ke: ",i)
    list_item = int(input())
    jum = jum + list_item

    listA .append (list_item)


print("Data list:", listA)
print("Jumlah:", jum)