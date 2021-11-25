import random

print("=======Program Test Aritmatika Dasar=======")
print("Pilihan level yang tersedia : ")
print("1. Easy ")
print("2. Medium ")
print("3. Hard ")

def generate(tingkatan):
    tingkatan=input("Masukan tingkatan yang ingin anda coba : ",)

    if tingkatan == "1":
        a = random.randint(20,50)
        b = random.randint(20,50)
        operasi = ['+','-','/','*']
        x = random.choice(operasi)
        pertanyaan = str(a)+str(x)+str(b) 
        print("Berapakah hasil dari",pertanyaan,"?")
        jawaban= float(input("Masukan Jawaban Anda : "))
        if jawaban == round(eval(pertanyaan),3):
            print("Jawaban Anda Benar ! ")
        else:
            print("Jawaban Anda Masih Salah")
        return round(eval(pertanyaan),3), pertanyaan

    elif tingkatan == "2":
        a = random.randint(20,70)
        b = random.randint(20,70)
        c = random.randint(20,70)
        operasi = ['+','-','/','*']
        x = random.choice(operasi)
        y = random.choice(operasi)
        
        pertanyaan = str(a)+str(x)+str(b)+str(y)+str(c) 
        print("Berapakah hasil dari",pertanyaan,"?")
        jawaban= float(input("Masukan Jawaban Anda : "))
        if jawaban == round(eval(pertanyaan),3):
            print("Jawaban Anda Benar ! ")
        else:
            print("Jawaban Anda Masih Salah")
        
        return round(eval(pertanyaan),3), pertanyaan
    

    elif tingkatan == "3":
        a = random.randint(20,100)
        b = random.randint(20,100)
        c = random.randint(20,100)
        d = random.randint(20,100)
        operasi = ['+','-','/','*']
        x = random.choice(operasi)
        y = random.choice(operasi)
        z = random.choice(operasi)
        pertanyaan = str(a) +str(x) +str(b) +str(y) +str(c)+str(z)+str(d)
        print("Berapakah hasil dari",pertanyaan,"?")
        jawaban= float(input("Masukan Jawaban Anda : "))
        if jawaban == round(eval(pertanyaan),3):
            print("Jawaban Anda Benar ! ")
        else:
            print("Jawaban Anda Masih Salah")
        
        return round(eval(pertanyaan),3), pertanyaan

def cekHasil():
    x,y =generate(tingkatan=input)
    print("Hasil dari",y,"=",x)
cekHasil()
