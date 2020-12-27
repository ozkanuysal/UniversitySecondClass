import cv2
import  numpy as np
resim=cv2.imread("ay.jpg")
Resim_Gri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
Blur=cv2.GaussianBlur(Resim_Gri,(5,5),0)
ret,Threshhold=cv2.threshold(Blur,130,255,cv2.THRESH_BINARY)
Maske=cv2.bitwise_and(resim,resim,mask=Threshhold)
HSV=cv2.cvtColor(Maske,cv2.COLOR_BGR2HSV)
Gri_alt=np.array([0,0,15])
Gri_ust=np.array([255,20,255])
Gri_filtre=cv2.inRange(HSV,Gri_alt,Gri_ust)

Sonuç=resim.copy()
_, cnts, _ = cv2.findContours(Gri_filtre,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
W=0
H=0
ındex=-1
for t in range(len(cnts)):
    x,y,w,h=cv2.boundingRect(cnts(ındex))
    cv2.rectangle(Sonuç,(x,y),(x+w,y+h),(0,255,0),2)


#cv2.imshow("Resim_gri",Resim_Gri)
#cv2.imshow("Resim_Blur",Blur)
#cv2.imshow("Threshold",Threshhold)
#cv2.imshow("Maskeli",Maske)
#cv2.imshow("Filtreli",Gri_filtre)
cv2.imshow("Sonuç",Sonuç)
cv2.waitKey(0)


