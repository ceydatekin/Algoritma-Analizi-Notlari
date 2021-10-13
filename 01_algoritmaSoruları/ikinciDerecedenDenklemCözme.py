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

print("Örnek Çözümler")
print(RootsOf(1,-44,435))
print(RootsOf(1, 2 , 1))
