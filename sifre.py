import hashlib

def sonucyazdir(liste):
    str1 = ''.join(liste)
    print("Hexadecimal = ",str1)
    return int(str1, 16) #Sonuç olarak 10'luk sayı sisteminde sonuç döndürebilmek için dönüşüm yapıyorum

n = int(input("Kaç basamaklı bir şifre üretmek istiyorsunuz ? : "))
filename = './sifre.py'
liste = []

with open(filename,'rb') as open_file: #rb = read binary
    content = open_file.read() 
    x0=hashlib.md5(content).hexdigest() #x0 değişkenime ilk atamayı gerçekleştiriyorum
    liste.append(x0[7])

for i in range(1,n):
    x=hashlib.md5(x0.encode('utf-8')).hexdigest()
    liste.append(x[7])
    x0=x

print("Decimal = ",sonucyazdir(liste))
