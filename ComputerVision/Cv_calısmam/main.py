import cv2
import numpy as np
import os
kamera_port=0
kamera=cv2.VideoCapture(kamera_port,cv2.CAP_DSHOW)

kernel=np.ones((12,12),np.uint8)


def ResimFarkBul(Resim1,Resim2):
    Resim2=cv2.resize(Resim2,(Resim1.shape[1],Resim1.shape[0]))
    Fark_Resim=cv2.absdiff(Resim1,Resim2)
    Fark_Sayı=cv2.countNonZero(Fark_Resim)
    return Fark_Sayı




def Veriyükle():
    Veri_isimler=[]
    Veri_Resimler=[]
    Dosyalar=os.listdir("Veri/")
    for Dosya in Dosyalar:
        Veri_isimler.append(Dosya.replace(".jpg",""))
        Veri_Resimler.append(cv2.imread("Veri/"+Dosya,0))

    return Veri_isimler,Veri_Resimler



def sınıf(Resim,Veri_isimler,Veri_Resimler):
    min_ındex=0
    mın_deger=ResimFarkBul(Resim,Veri_Resimler[0])
    for t in range(len(Veri_isimler)):
        Fark_Deger=ResimFarkBul(Resim,Veri_Resimler[t])
        if(Fark_Deger<mın_deger):
            mın_deger=Fark_Deger
            min_ındex=t
        return  Veri_isimler[min_ındex]
Veri_isimler,Veri_Resimler=Veriyükle()
Veri_Resim1=cv2.imread("Veri/bir.jpg",0)


while True:
    ret,Kare=kamera.read()
    kucuk = Kare[0:200,0:250]
    Hsv_formatı=cv2.cvtColor(kucuk,cv2.COLOR_BGR2GRAY)
    Kesilmiş_Kare_Gri =cv2.cvtColor(kucuk,cv2.COLOR_BGR2GRAY)
    Kesilmiş_Kare_HSV =cv2.cvtColor(kucuk,cv2.COLOR_BGR2HSV)
    alt = np.array([0, 20, 40])
    ust = np.array([40, 255, 255])
    Renk_sonuc=cv2.inRange(Kesilmiş_Kare_HSV,alt,ust)
    Renk_sonuc=cv2.morphologyEx(Renk_sonuc,cv2.MORPH_CLOSE,kernel)
    Renk_sonuc=cv2.dilate(Renk_sonuc,kernel,iterations=1)
    sonuc=kucuk.copy()
    cnts,_=cv2.findContours(Renk_sonuc,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    genıslık=0
    uzunluk=0
    Max_ındex=-1
    for t in range(len(cnts)):
         cnt=cnts[t]
         x,y,w,h = cv2.boundingRect(cnt)
         if(w>genıslık and h>uzunluk):
            uzunluk=h
            genıslık=w
            Max_ındex=t
    if(len(cnts)>0):
        x,y,w,h=cv2.boundingRect(cnts[Max_ındex])
        cv2.rectangle(sonuc,(x,y),(x+w,y+h),(0,255,0),2)
        EL_Resim=Renk_sonuc[y:y+h,x:x+w]
     #   cv2.imshow("El_resim",EL_Resim)
        print(sınıf(EL_Resim,Veri_isimler,Veri_Resimler))

    #cv2.imshow("Kare",Kare)
    cv2.imshow("Kesilmiş kare",kucuk)
    #cv2.imshow("Renk sonuc",Renk_sonuc)
    #cv2.imshow("sonuc",sonuc)



    #Hsv_sonuc=cv2.inRange(kucuk,alt,ust)
    #Hsv_sonuc=cv2.morphologyEx(Hsv_sonuc,cv2.MORPH_CLOSE,kernel)

    #Grı=cv2.cvtColor(kucuk,cv2.COLOR_BGR2HSV)
    #alt=np.array([0,20,50])
    #ust=np.array([90,255,255])
    #sonuc=cv2.inRange(kucuk,alt,ust)
    #cv2.imshow("renj",sonuc)

    #Sonuc=kucuk.copy()
    #cnts,_=cv2.findContours(Hsv_sonuc,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    #hmax=0
    #wmax=0
    #ındex=-1
    #for t in range(len(cnts)):
    #    cnt=cnts[t]
    #    x,y,w,h = cv2.boundingRect(cnt)
    #    if(w>wmax and h>hmax):
    #        hmax=h
    #        wmax=w
    #        ındex=t
    #if(len(cnts)>0):
     #         x,y,h,w=cv2.boundingRect(cnts[ındex])
     #         cv2.rectangle(Sonuc,(x,y),(x+w,y+h),(0,255,0),2)
    #          El_resim=Hsv_sonuc[y:y+h,x:x+w]
    #          cv2.imshow("eL resmı",El_resim)
    #          ResimFarkBul(El_resim,Veri_Resimi)

    #cv2.imshow("Kare",Kare)
    #cv2.imshow('Kucuk_alan',kucuk)
    #cv2.imshow('Uzay_goruntu',Hsv_sonuc)
    #cv2.imshow("Sonuç",Sonuc)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break


kamera.release()
cv2.destroyAllWindows()