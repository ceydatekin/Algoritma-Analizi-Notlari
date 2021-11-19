import pandas as pd
import numpy as np
import pandas as pd
import os
from sklearn.cluster import KMeans
import sklearn.metrics as sm
import random
import itertools

#excelden okuyup kümeleme ile yapmak istedim
#df = pd.read_excel("kumeleme_sonucu.xls")
#v = df.iloc[:,1].values
#v =v.reshape(-1,1)
#K-means kümeleme yönetemi ile bu fotmata getirdim ama bunu nasıl kullanacağımı bilemediğim için elle istenilen sayıya göre random üç sınıflı
#küme oluşturmaya karar verdim a-b-c-d değerlerini bulma mantığım için
#model = KMeans(n_clusters=3,random_state=1)
#model.fit(v)
#model.labels_[:]

küme1=[1,1,1,1,1,2,2,2,2,3,3,3,3,3,3]
küme2=[1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3]
küme3=[1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3]

#başlangıç olarak kümelerin 1-2-3 sınıflarına göre ayrılması gerektiğini düşündüm
deneme1=[]
deneme2=[]
deneme3=[]

for i in küme1:
    if(i == 1):
        deneme1.append(i);
    elif(i==2):
        deneme2.append(i);
    else:
        deneme3.append(i);

deneme21=[]
deneme22=[]
deneme23=[]

for i in küme2:
    if(i == 1):
        deneme21.append(i);
    elif(i==2):
        deneme22.append(i);
    else:
        deneme23.append(i);

deneme31=[]
deneme32=[]
deneme33=[]

for i in küme3:
    if(i == 1):
        deneme31.append(i);
    elif(i==2):
        deneme32.append(i);
    else:
        deneme33.append(i);

#birinci küme - ikinci küme a değeri
a=len(list(itertools.combinations(deneme1,2)))+len(list(itertools.combinations(deneme2,2)))+len(list(itertools.combinations(deneme3,2)))+len(list(itertools.combinations(deneme21,2)))+len(list(itertools.combinations(deneme22,2)))+len(list(itertools.combinations(deneme23,2)))
b=(len(deneme1)*len(deneme21))+(len(deneme2)*len(deneme22))+(len(deneme3)*len(deneme23))
c=len(list(itertools.combinations(deneme1,1)))*len(list(itertools.combinations(deneme2,1)))+len(list(itertools.combinations(deneme1,1)))*len(list(itertools.combinations(deneme3,1)))+len(list(itertools.combinations(deneme2,1)))*len(list(itertools.combinations(deneme3,1)))+len(list(itertools.combinations(deneme21,1)))*len(list(itertools.combinations(deneme22,1)))+len(list(itertools.combinations(deneme21,1)))*len(list(itertools.combinations(deneme23,1)))+len(list(itertools.combinations(deneme22,1)))*len(list(itertools.combinations(deneme23,1)))
d=len(deneme1)*len(deneme22)+len(deneme1)*len(deneme23)+len(deneme2)*len(deneme23)+len(deneme21)*len(deneme2)+len(deneme21)*len(deneme3)+len(deneme22)*len(deneme3)

#iki küme için tek tek yapsamda üçü için el ile denemek istedim sonra onu rastegele belirlenmiş küme sayıları ve eleman sayılarıyla deneyeceğim.
#el ile hazrıladığım kümelerin hesabı

b=0
d=0
for i in range(len(list(itertools.combinations([küme1,küme2,küme3], 2)))):
    komb = list(itertools.combinations([küme1, küme2, küme3], 2))
    de=komb[i][0]
    den=komb[i][1]
    #üç sınıfım kesin olduğu için 1-2-3 iterasyonlarını range ile döndürdüm.
    for j in range(1,4):
        b+=de.count(j)*den.count(j)
        if(j==1):
            d+=de.count(j)*den.count(2)+de.count(j)*den.count(3)+de.count(2)*den.count(j)+de.count(3)*den.count(j)
        if(j==2):
            d+=de.count(j)*den.count(3)+de.count(3)*den.count(j)
print("b sayısı:" + str(b))
print("d sayısı:" + str(d))
a=0
c=0
for i in range(len(list(itertools.combinations([küme1,küme2,küme3], 1)))):
    komb = list(itertools.combinations([küme1, küme2, küme3], 1))
    de=komb[i][0]
    deneme1=[]
    deneme2=[]
    deneme3=[]
    for i in de:
        if(i == 1):
            deneme1.append(i);
        elif(i==2):
            deneme2.append(i);
        else:
            deneme3.append(i);
    a+=len(list(itertools.combinations(deneme1,2)))+len(list(itertools.combinations(deneme2,2)))+len(list(itertools.combinations(deneme3,2)))
    c+=len(list(itertools.combinations(deneme1,1)))*len(list(itertools.combinations(deneme2,1)))+len(list(itertools.combinations(deneme1,1)))*len(list(itertools.combinations(deneme3,1)))+len(list(itertools.combinations(deneme2,1)))*len(list(itertools.combinations(deneme3,1)))
print("c sayısı:" + str(c))
print("a sayısı:" + str(a))
jaccard = a/(a+b+c)
print("jaccard indeksi = "+str(jaccard))
rand = (a+d)/(a+b+c)
print("rand indeksi = "+ str(rand))

#derste çözdüğümüz küme örnekleri
küme5=[1,1,2,2,3]
küme6=[1,2,2]

b=0
d=0
for i in range(len(list(itertools.combinations([küme5,küme6], 2)))):
    komb3 = list(itertools.combinations([küme5, küme6], 2))
    de=komb3[i][0]
    den=komb3[i][1]
    #üç sınıfım kesin olduğu için 1-2-3 iterasyonlarını range ile döndürdüm.
    for j in range(1,4):
        b+=de.count(j)*den.count(j)
        if(j==1):
            d+=de.count(j)*den.count(2)+de.count(j)*den.count(3)+de.count(2)*den.count(j)+de.count(3)*den.count(j)
        if(j==2):
            d+=de.count(j)*den.count(3)+de.count(3)*den.count(j)
print("b sayısı:" + str(b))
print("d sayısı:" + str(d))
a=0
c=0
for i in range(len(list(itertools.combinations([küme5,küme6], 1)))):
    komb3 = list(itertools.combinations([küme5, küme6], 1))
    de=komb3[i][0]
    deneme1=[]
    deneme2=[]
    deneme3=[]
    for i in de:
        if(i == 1):
            deneme1.append(i);
        elif(i==2):
            deneme2.append(i);
        else:
            deneme3.append(i);
    a+=len(list(itertools.combinations(deneme1,2)))+len(list(itertools.combinations(deneme2,2)))+len(list(itertools.combinations(deneme3,2)))
    c+=len(list(itertools.combinations(deneme1,1)))*len(list(itertools.combinations(deneme2,1)))+len(list(itertools.combinations(deneme1,1)))*len(list(itertools.combinations(deneme3,1)))+len(list(itertools.combinations(deneme2,1)))*len(list(itertools.combinations(deneme3,1)))
print("c sayısı:" + str(c))
print("a sayısı:" + str(a))
jaccard = a/(a+b+c)
print("jaccard indeksi = "+str(jaccard))
rand = (a+d)/(a+b+c)
print("rand indeksi = "+ str(rand))





toplamkümelistesi=[]
#üç sınıflı random sayılarda kümelenmiş bir kümeleme işlemi ile
küme_sayisi = int(input("küme sayisini giriniz"))
for i in range(0,küme_sayisi):
    eleman_sayisi=int(input("eleman sayısını giriniz"))
    yeniküme=[]
    for j in range(0,eleman_sayisi):
        yeniküme.append(random.randint(1,3))
    toplamkümelistesi.append(yeniküme)


#Sonra b-d değerlerim için üçlü veya çoklu küme sayılarımda 2'li iterasyonlarından toplu işlem yapmam gerektiğini düşündüm
#bu sebeple kümelerini kombinasyonu ile b-d değerlerini bulmaya karar verdim
#Kümelerin hepsini bir liste şeklinde tutup arttırılabilir olarak ayarladım

b=0
d=0
for i in range(len(list(itertools.combinations(toplamkümelistesi, 2)))):
    komb2 = list(itertools.combinations(toplamkümelistesi, 2))
    de=komb2[i][0]
    den=komb2[i][1]
    #üç sınıfım kesin olduğu için 1-2-3 iterasyonlarını range ile döndürdüm.
    for j in range(1,4):
        b+=de.count(j)*den.count(j)
        if(j==1):
            d+=de.count(j)*den.count(2)+de.count(j)*den.count(3)+de.count(2)*den.count(j)+de.count(3)*den.count(j)
        if(j==2):
            d+=de.count(j)*den.count(3)+de.count(3)*den.count(j)
print("b sayısı:" + str(b))
print("d sayısı:" + str(d))
a=0
c=0
for i in range(len(list(itertools.combinations(toplamkümelistesi, 1)))):
    komb2 = list(itertools.combinations(toplamkümelistesi, 1))
    de=komb2[i][0]
    deneme1=[]
    deneme2=[]
    deneme3=[]
    for i in de:
        if(i == 1):
            deneme1.append(i);
        elif(i==2):
            deneme2.append(i);
        else:
            deneme3.append(i);
    a+=len(list(itertools.combinations(deneme1,2)))+len(list(itertools.combinations(deneme2,2)))+len(list(itertools.combinations(deneme3,2)))
    c+=len(list(itertools.combinations(deneme1,1)))*len(list(itertools.combinations(deneme2,1)))+len(list(itertools.combinations(deneme1,1)))*len(list(itertools.combinations(deneme3,1)))+len(list(itertools.combinations(deneme2,1)))*len(list(itertools.combinations(deneme3,1)))
print("c sayısı:" + str(c))
print("a sayısı:" + str(a))
jaccard = a/(a+b+c)
print("jaccard indeksi = "+str(jaccard))
rand = (a+d)/(a+b+c)
print("rand indeksi = "+ str(rand))