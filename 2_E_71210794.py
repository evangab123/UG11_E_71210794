kata= input("Masukan kata : ")
x = len(kata)

def kataTengah():
    if x % 2 == 1:
        if x >=5:
            y = int((x - 1)/2)
            jawab = kata[y-1]+kata[y]+kata[y+1]
            print("Huruf tengah pada kata",kata,"adalah", str(jawab))
        elif x<5:
            y = int((x - 1)/2)
            jawab = kata[y]
            print("Huruf tengah pada kata",kata,"adalah", str(jawab))

    elif x%2 ==0:
        if x < 8:
            y= int(x/2)
            jawab= kata[y-1]+kata[y]
            print("Huruf tengah pada kata",kata,"adalah", str(jawab))
        else:
            y=int(x/2)
            jawab=kata[y-2]+kata[y-1]+kata[y]+kata[y+1]
            print("Huruf tengah pada kata",kata,"adalah", str(jawab))

kataTengah()