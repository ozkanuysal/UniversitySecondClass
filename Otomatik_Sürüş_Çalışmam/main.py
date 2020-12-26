import cv2
import  numpy as np
import  matplotlib.pyplot as plt
#import pandas as pd
#import  scipy as sc
import os

def cannny(image):
    grı = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)  # resim gri
    blur = cv2.GaussianBlur(grı, (5, 5), 0)  # etrafı blurladık
    canny = cv2.Canny(blur, 50, 150)  # etraf simsiyah sadece beyaz çizgiler ile anlamaya çalışıyoruz
    return  canny
def koseler(image,lines):
    line_image=np.zeros_like(image)
    if lines is not None:
        for x1,y1,x2,y2 in lines:

            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
    return line_image
def koordinatlar(image,line_parameters):
    egıt,giris=line_parameters
    #print(image.shape)
    y1=image.shape[0]
    y2=int(y1*(3/5))
    x1=int((y1-giris)/egıt)
    x2=int((y2-giris)/egıt)
    return np.array([x1,y1,x2,y2])

def gorulen(image,lines):
    sol_duzelt=[]
    sag_duzelt=[]
    for line in lines:
        x1,y1,x2,y2=line.reshape(4)
        parametreler=np.polyfit((x1,x2),(y1,y2),1)
        print(parametreler)
        egıt=parametreler[0]
        giris=parametreler[1]
        if egıt<0:
            sol_duzelt.append((egıt,giris))
        else:
            sag_duzelt.append((egıt,giris))
    sol_ort=np.average(sol_duzelt, axis=0)
    sag_ort=np.average(sag_duzelt, axis=0)
    sol_cizgi=koordinatlar(image,sol_ort)
    sag_cizgi=koordinatlar(image,sag_ort)
    return np.array([sol_cizgi,sag_cizgi])


def karartma(image):
    yukseklık=image.shape[0]
    genıslık=np.array([
        [(200,yukseklık),(1100,yukseklık),(550,250)]
    ])
    maske=np.zeros_like(image)
    cv2.fillPoly(maske,genıslık,255)
    #filtreyi resme uygulayıp arka tarafı karartma durumu
    maskelı_resım=cv2.bitwise_and(image,maske)
    return  maskelı_resım

image = cv2.imread('test_image.jpg')
lane = np.copy(image)
#cannny_image=cannny(lane)
#maskelenmıs_resim=karartma(cannny_image)
#lines=cv2.HoughLinesP(maskelenmıs_resim,2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
#ort_cızgı=gorulen(lane,lines)
#line_image=koseler(lane,ort_cızgı)
#combo=cv2.addWeighted(lane,0.8,line_image,1,1)
#plt.imshow(cannny)
#plt.show()

#cv2.imshow("result",combo)
#cv2.waitKey(0)


cap=cv2.VideoCapture("test2.mp4")
while(cap.isOpened()):
    _, frame=cap.read()
    cannny_image = cannny(frame)
    maskelenmıs_resim = karartma(cannny_image)
    lines = cv2.HoughLinesP(maskelenmıs_resim, 2, np.pi / 180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    ort_cızgı = gorulen(frame, lines)
    line_image = koseler(frame, ort_cızgı)
    combo = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    # plt.imshow(cannny)
    # plt.show()

    cv2.imshow("result", combo)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyWindow()

