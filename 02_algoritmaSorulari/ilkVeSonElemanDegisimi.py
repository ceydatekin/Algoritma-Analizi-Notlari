def elemanDegistir():
    dizi=[1,2,3,4,5,6,7,8,9,10,11,12]
    print("dizinin ilk hali:")
    print(dizi)
    temp = dizi[len(dizi)-1]
    dizi[len(dizi)-1]=dizi[0]
    dizi[0]= temp
    print("dizinin birinci ve son elemanının değişmiş hali:")
    print(dizi)
elemanDegistir()