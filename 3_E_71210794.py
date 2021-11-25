print("=======Program Manipulasi String=======")
print("Pilihan Menu : ")
print ("1. Hitung kata ")
print ("2. Cek kata ")
print ("3. Ubah kata ")
x= input("Pilihan anda : ")

#1
def hitungKata():
    ke1= input(" Masukan sebuah kalimat/kata : ")
    kataitung= input("Masukan kata yang ingin dihitung : ")
    lowerkata1= ke1.lower()
    lowerkata2= kataitung.lower()
    if lowerkata2 in lowerkata1:
        o= lowerkata1.count(lowerkata2)
        print("Terdapat sebanyak",o,"kata",kataitung,"di dalam string")
#2
def cekkata():
    kata1= input("Masukan sebuah kalimat/kata : ")
    katacek= input("Masukan kata yang ingin di cek : ")
    if katacek in kata1:
        print("kata",katacek,"terdapat di dalam string")
        print("String diubah menjadi : ")
        x = kata1.replace(katacek,katacek.upper())
        print(x)
    
    else:
        print("Kata",katacek,"tidak terdapat di dalam string ")
        print("String diubah menjadi : ")
        print(kata1,katacek)
#3
def ubahKata():
    kata2= input("Masukan sebuah kalimat/kata : ")
    katacek2= input("Masukan kata yang ingin di ubah : ")
    kataganti= input("Masukan kata pengganti :")
    print("Anda akan mengubah kata",katacek2,"Menjadi",kataganti,"Sebanyak 1x")
    cek= input("Apakah anda ingin mengubah jumlah total penggantian kata ? (yes/no) : ")
    if cek=="no":
        print("String berhasil diubah menjadi : ")
        print(kata2.replace(katacek2,kataganti,1))

    elif cek== "yes":
        jumlahdiganti= int(input("Masukan jumlah total penggantian : "))
        print("String berhasil diubah menjadi : ")
        print(kata2.replace(katacek2,kataganti,jumlahdiganti))
if x == "1":
    hitungKata()

elif x == "2" :
    cekkata()

elif x == "3" : 
    ubahKata()

else:
    print("Pilihlah yang ada dimenu!")