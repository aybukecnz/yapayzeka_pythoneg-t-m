import matematik as math

math.bol(20,2)

faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)
#print(int(krediAdi))
faiz = str(faiz)
print(type(faiz))

vade = int(input("Lütfen istediğiniz vade sayısını giriniz: "))

print(type (vade))

vade = vade + 12

# dize interpolasyonu
# Seçtiğiniz vade sonucu ortaya çıkan vade:

print("Seçtiğiniz vade sonucu ortaya çıkan vade: "+ str(vade))

print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade))
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade} ")

isim = input("İsminizi giriniz")
metin = "Merhaba {name}".format(name=123)
print(metin)

# f-dizisi
metin = f"Hoşgeldiniz {1+1}"

print(metin)

# listeler
# döngüler
# fonksiyonlar
krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))
print(krediler[0])
print(len(krediler)) #length
# print(krediler [3]) => hata verir
dizi = ["İhtiyaç Kredisi", 10, 5.2]
print(dizi)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]

print(type (krediler))
print(krediler[0])

print(len(krediler)) #length
# print(krediler [3]) => hata verir

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("ay")

krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"])
print(krediler)

# for
# i=0 i<10

for i in range(10) :
    print("xx")
    print(i)
    
for i in range(5,11) :
    print(i)
    
# i aralığında (0.1,0.5) için:
# print(i)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]

for kredi in krediler:
    print(kredi)

print("***************")

for i in range(len(krediler)):
    print(krediler[i])
    
# sonsuz döngü
i = 0
while i < 10 :
    print("x")
    i += 1
print("y")

while True:
    print("X")
    break

print("*******")
i =0
while i < len(krediler):
    i+=1
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break

print("**** Son Döngü *****")

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
i = 0

while i < len(krediler):
    i+=1
    print(i)
    print(krediler[i])
    if krediler[i] == "Konut Kredisi": 
        break
    
#fonksiyonlar

fiyat =100
indirim=20
#definition define
def calculate():
    print(100-20)
    
def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)  
    
def sayHello(name):
    print(f"Merhaba {name}")
    
calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Aybüke")
sayHello("Ahmet")

def calculateAndReturn(fiyat,indirim):
    return fiyat-indirim

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat + 10)

def calculatePrice(price, discount):
    print(price-discount)
    
def calculatePriceAndReturn(price,discount):
    return price-discount

#fonk1= calculatePrice(100,50)
fonk2= calculatePriceAndReturn(300,100)
#print(f"161. satır: {fonk1}")
print(f"162. satır: {fonk2}")

#3.video
# sınıflar classlar
# modül
# paket yönetimi

class Human:
    name="Halit"
    #built-in
def __init__(self): 
    print("Bir human instance'i üretildi")
    
def __str__(self):
    return f"STR fonksiyonundan dönen değer:", {self.name}
    def talk(self,sentence):
        name="Ercan"
        print(f"{self.name}:{sentence}")
    def walk(self):
        print(f"{self.name} is walking...")

# instance => örnek
human1 = Human()
human1.talk("Hi")
#human1.walk()
print(human1)

human2 = Human()
human2.name ="Cem"
human2.talk("Selam","Mevlüt")
human2.walk()
print(human2)


