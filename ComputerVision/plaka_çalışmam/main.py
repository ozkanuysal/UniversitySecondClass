import cv2
W=640
H=480
TanımlamaCascade=cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
mınArea=500
color=(255,0,255)
kamera=cv2.VideoCapture(0)
kamera.set(3,W)
kamera.set(4,H)
kamera.set(10,150)
while True:
    basarı,resım=kamera.read()
    grı=cv2.cvtColor(resım,cv2.COLOR_BGR2GRAY)
    plaka=TanımlamaCascade.detectMultiScale(grı,1.1,4)
    for(x,y,w,h)in plaka:
        area=w*h
        if area>mınArea:
            cv2.rectangle(resım,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(resım,"PLAKAMIZ",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi=resım[y:y+h,x:x+w]
            cv2.imshow("ROI",imgRoi)

    cv2.imshow("Sonuc",resım)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("Taranan"+".jpg",imgRoi)
        break