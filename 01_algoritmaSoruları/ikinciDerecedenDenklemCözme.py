#2. dereceden deklemin köklerini bulmaya yarayan fonksiyon
#döndürme tipi float
import math
def  RootsOf(a,b,c):
    result= []
    delta= math.sqrt((b*b)-(4*a*c))
    if (delta == 0):
        x1 = -(b)/(2*a)
        x2 = x1
        result.append(x1)
        result.append(x2)
        return result
    elif (delta>0):
        x1= (-b + delta)/(2*a)
        x2 = (-b - delta) / (2 * a)
        result.append(x1)
        result.append(x2)
        return result
    else:
        return "denklemin reel kökü yoktur"

#2 bilinmeyenli denklemin çözümünü yapan fonksiyon
def SolveTwoVariables(kx1, ky1, r1, kx2, ky2, r2):
    if(kx1 == kx2):
        y =(-r1 + r2) / (-ky1 * ky2)
        x = (r1 - (ky1 * y)) / kx1
        sonuc = "x= " + str(x) + " y= "+ str(y)
        return sonuc
    if((kx1<0 and kx2>0 ) or (kx1>0 and kx2<0)):
        y=(kx2*r1 + kx1*r2) / (ky1*kx2 + ky2*kx1)
        x = (r1 - (ky1 * y)) / kx1
        sonuc = "x= " + str(x) + " y= " + str(y)
        return sonuc
    if ((kx1 < 0 and kx2 < 0) or (kx1 > 0 and kx2 > 0)):
        y = ((-kx2 * r1) + (kx1 * r2)) / ((ky1 * -kx2) + (ky2 * kx1))
        x = (r1 - (ky1 * y)) / kx1
        sonuc = "x = " + str(x) +"  "+ " y = " + str(y)
        return sonuc

#roman rakamına çevirme
def DexToRoman(number):
    birler={ 0:"",1:"|", 2: "||", 3: "|||",4: "|V",5: "V",6: "V|",7: "V||",8: "V|||", 9: "|V"}
    onlar = {0:"",1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"}
    yuzler = {0:"",1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"}
    if(number == 1000):
        return "M"
    else:
        if(len(str(number))==3):
            birler_basamagi = number % 10
            number = int(number/10)
            onlar_basamagi = number % 10
            yuzler_basamagi = int(number/10)
            sonuc= yuzler[yuzler_basamagi]+onlar[onlar_basamagi]+birler[birler_basamagi]
            return sonuc
        elif(len(str(number))==2):
            birler_basamagi = number % 10
            number = int(number / 10)
            onlar_basamagi = number % 10
            sonuc = onlar[onlar_basamagi] + birler[birler_basamagi]
            return sonuc
        elif (len(str(number)) == 1):
            birler_basamagi = number % 10
            sonuc = birler[birler_basamagi]
            return sonuc

print("Lütfen yapmak istediğiniz işlemi seçiniz: ")
print("1. İkinci dereceden denklemin köklerini bulma")
print("2. İki bilinmeyenli denklemin çözümünü bulma")
print("3. Bine kadar verilen sayıyı roma rakamına çevirme")
secim= int(input("seciminizi yapınız: "))
if(secim == 1):
    print("ax^2 + bx + c = 0 formatında")
    a = int(input("a değerini giriniz"))
    b = int(input("b değerini giriniz"))
    c = int(input("c değerini giriniz"))
    print("sonucunuz:")
    print(RootsOf(a,b,c))
    print("Örnek Çözümler")
    print(RootsOf(1,-44,435))
    print(RootsOf(1, 2 , 1))
elif(secim == 2):
    print("kx1*x + ky1*y =r1")
    print("kx2*x + ky2*y =r2 formatında")
    kx1 = int(input("kx1 değerini giriniz"))
    ky1 = int(input("ky1 değerini giriniz"))
    r1 = int(input("r1 değerini giriniz"))
    kx2 = int(input("kx2 değerini giriniz"))
    ky2 = int(input("ky2 değerini giriniz"))
    r2 = int(input("r2 değerini giriniz"))
    print("sonucunuz:")
    print(SolveTwoVariables(kx1,ky1,r1,kx2,ky2,r2))
    print("Örnek Çözümler")
    print(SolveTwoVariables(4, 2, 8, 5, 3, 9))
    print(SolveTwoVariables(2, -1, 2, 1, 2, 1))
    print(SolveTwoVariables(1, -1, 2, 0.5, 0.5, 6))
elif(secim == 3):
    number= int(input("lütfen sayi giriniz"))
    print("sonucunuz:")
    print(DexToRoman(number))
    print("Örnek Çözümler")
    print(DexToRoman(135))
    print(DexToRoman(5))
    print(DexToRoman(40))

