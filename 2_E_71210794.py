kata= input("Masukan kata : ")

def kataTengah(kata):
    x = len(kata)
    if x % 2 == 1:
        if x >=5:
            y = int((x - 1)/2)
            jawab = kata[y-1]+kata[y]+kata[y+1]
            #print("Huruf tengah pada kata",kata,"adalah", str(jawab))
            return jawab
        elif x<5:
            y = int((x - 1)/2)
            jawab = kata[y]
            #print("Huruf tengah pada kata",kata,"adalah", str(jawab))
            return jawab
    elif x%2 ==0:
        if x < 8:
            y= int(x/2)
            jawab= kata[y-1]+kata[y]
            #print("Huruf tengah pada kata",kata,"adalah", str(jawab))
            return jawab
        else:
            y=int(x/2)
            jawab=kata[y-2]+kata[y-1]+kata[y]+kata[y+1]
            #print("Huruf tengah pada kata",kata,"adalah", str(jawab))
            return jawab

print("Huruf tengah pada kata",kata,"adalah",kataTengah(kata))