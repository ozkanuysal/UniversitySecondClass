import cv2

kamera=cv2.VideoCapture(0)
cv2.namedWindow('sketch')
while True:
    ret,frame=kamera.read()
    image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    image=cv2.GaussianBlur(image,(7,7),0)
    image=cv2.Canny(image,10,60)
    ret,image=cv2.threshold(image,50,255,cv2.THRESH_BINARY_INV)
    cv2.imshow("orjinal",frame)
    cv2.imshow("sketch",image)
    if cv2.waitKey(1)==ord('q'):
        break

kamera.release()
cv2.destroyWindow()