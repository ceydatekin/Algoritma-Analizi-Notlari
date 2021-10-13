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

print(SolveTwoVariables(4,2,8,5,3,9))
print(SolveTwoVariables(2,-1,2,1,2,1))
print(SolveTwoVariables(1,-1,2,0.5,0.5,6))