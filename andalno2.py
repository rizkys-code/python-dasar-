mK1 = int(input())
mK2 = int(input())
mK3 = int(input())
jUMLAHLULUS = 0
if mK1 >= 60:
    jUMLAHLULUS = jUMLAHLULUS + 1
if mK2 >= 60:
    jUMLAHLULUS = jUMLAHLULUS + 1
if mK3 >= 60:
    jUMLAHLULUS = jUMLAHLULUS + 1
if  jUMLAHLULUS == 3:
    print("TIGA")
else:
    if jUMLAHLULUS == 2:
        print("DUA")
    else:
        if jUMLAHLULUS == 1:
            print("SATU")
        else:
            print("NOL")