import random
def sirasizRandomDizi():
    dizi_boyutu= int(input("lütfen dizi boyutunu giriniz"))
    dizi=[]
    for i in range(0,dizi_boyutu):
        dizi.append(random.randint(0, 100))
    return dizi

print(sirasizRandomDizi())