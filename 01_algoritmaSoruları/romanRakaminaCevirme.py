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
print(DexToRoman(135))
print(DexToRoman(40))
print(DexToRoman(13))