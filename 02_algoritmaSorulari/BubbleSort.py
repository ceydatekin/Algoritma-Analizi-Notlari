def swap(dizi,indis1,indis2):
    temp = dizi[indis2]
    dizi[indis2]=dizi[indis1]
    dizi[indis1]= temp

def bubbleSort(dizi):
    for siralanacakindex in range(len(dizi)-1,-1,-1):
        for kontrolindexi in range(len(dizi)-1,-1,-1):
            if(dizi[siralanacakindex] < dizi[kontrolindexi] or dizi[siralanacakindex] == dizi[kontrolindexi]):
                continue
            elif(dizi[siralanacakindex] > dizi[kontrolindexi]):
                swap(dizi, siralanacakindex, kontrolindexi)
    print("bubblesort ile sıralanmış dizimiz:")
    print(dizi)
dizi=[14,25,36,12,45,13,52,11,22,21,54,10,33,12]
bubbleSort(dizi)