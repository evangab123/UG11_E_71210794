print("Menu Program Yang Tersedia")
print("1. pangkatkan angka")
print("2. akarkan bilangan")
x = input("Masukan pilihan yang diinginkan : ")

def pangkatAngka():
    y = float(input("Masukan angka ingin di Pangkatkan\nAngka : "))
    modif= input("ingin memodifikasi pangkat ?(yes/no)\n: ")
    if modif == "yes" :
        nilaipangkatbaru= float(input("Masukan nilai pangkat : "))
        rumus1 = y ** nilaipangkatbaru
        print("Hasil dari",str(y)+"^"+str(nilaipangkatbaru),"=",round(rumus1,2))
    elif modif =="no":
        rumus1= y ** 2
        print("Hasil dari",str(y)+"^2 = ",round(rumus1,2))
    else:
        print("ketik yes/no")
    return x

def akarBilangan():
    z= float(input("Masukan angka yang ingin di akar\nAngka : "))
    modif2= input("Ingin memodifikasi akar ?(yes/no)\n: ")
    if modif2 == "yes":
        nilaiakarbaru= int(input("Masukan nilai akar : "))
        rumus2=z**(1/ nilaiakarbaru)
        print("Hasil akar pangkat",nilaiakarbaru,"dari",z,"=",round(rumus2,2))
    elif modif2 =="no":
        rumus2=z**(1/2)
        print("Hasil akar pangkat 2 dari",z,"=",round(rumus2,2))
    else:
        print("ketik yes/no")
    return x
    
if x == "1":
    pangkatAngka()

elif x == "2":
    akarBilangan()