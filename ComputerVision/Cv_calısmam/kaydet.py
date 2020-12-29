import cv2
import numpy as np
import os

kamera_port=0
kamera=cv2.VideoCapture(kamera_port,cv2.CAP_DSHOW)
kernel=np.ones((15,15),np.uint8)
ısım='uc'

while True:
    ret,Kare=kamera.read()
    kucuk = Kare[0:250,0:250]
    Hsv_formatı=cv2.cvtColor(kucuk,cv2.COLOR_BGR2GRAY)

    alt=np.array([0,68,100])
    ust=np.array([40,255,255])

    Hsv_sonuc=cv2.inRange(kucuk,alt,ust)
    Hsv_sonuc=cv2.morphologyEx(Hsv_sonuc,cv2.MORPH_CLOSE,kernel)


    Grı=cv2.cvtColor(kucuk,cv2.COLOR_BGR2HSV)
    alt=np.array([0,20,50])
    ust=np.array([90,255,255])
    sonuc=cv2.inRange(kucuk,alt,ust)
   # cv2.imshow("renj",sonuc)

   # _, frame = kamera.read()
   # # Convert BGR to HSV
   # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   # # define range of blue color in HSV
   # lower_blue = np.array([110, 50, 50])
   # upper_blue = np.array([130, 255, 255])
   # # Threshold the HSV image to get only blue colors
   # mask = cv2.inRange(hsv, lower_blue, upper_blue)
   # cv2.imshow('maske',mask)




    Sonuc=kucuk.copy()
    cnts,_=cv2.findContours(Hsv_sonuc,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    hmax=0
    wmax=0
    ındex=-1
    for t in range(len(cnts)):
        cnt=cnts[t]
        x,y,w,h = cv2.boundingRect(cnt)
        if(w>wmax and h>hmax):
            hmax=h
            wmax=w
            ındex=t
    if(len(cnts)>0):
         x,y,h,w=cv2.boundingRect(cnts[ındex])
         cv2.rectangle(Sonuc,(x,y),(x+w,y+h),(0,255,0),2)
         El_resim=Hsv_sonuc[y:y+h,x:x+w]
    #     cv2.imshow("eL resmı",El_resim)


    cv2.imshow("Kare",Kare)
    #cv2.imshow('Kucuk_alan',kucuk)
    #cv2.imshow('Uzay_goruntu',Hsv_sonuc)
    #cv2.imshow("Sonuç",Sonuc)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        #cv2.imwrite("Veri/" + ısım + ".jpg", El_resim)

        #path = "C:\Users\Ozkan\PycharmProjects\proje1\Veri"
        #cv2.imwrite(os.path.join("path" + ısım + ".jpg"), El_resim)
       # cv2.waitKey(0)
        break


#def load_images_from_folder(Veri):
 #   images = []
  #  for filename in os.listdir(Veri):
   #     img = cv2.imread(os.path.join(Veri,filename))
    #    if img is not None:
     #       images.append(img)
   # return images
#path="C:\Users\Ozkan\PycharmProjects\proje1\Veri"


#cv2.imwrite("Veri/" + ısım + ".jpg", El_resim)
#cv2.imwrite(os.path.join("path"+ısım+".jpg"),El_resim)
#cv2.waitKey(0)
cv2.imwrite("Veri/"+ısım+".jpg",kucuk)
kamera.release()
cv2.destroyAllWindows()
