def swap(dizi,indis1,indis2):
    print("dizinin ilk hali:")
    print(dizi)
    temp = dizi[indis2]
    dizi[indis2]=dizi[indis1]
    dizi[indis1]= temp
    print("dizinin elemanları değişmiş hali:")
    print(dizi)

dizi=[1,2,3,4,5,6,7,8,9,10,11,12]
swap(dizi, 0, 5)