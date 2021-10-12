import cv2

wajah = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam= cv2.VideoCapture(0)

while 1:
    ret,img = cam.read()
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    deteksi=wajah.detectMultiScale(gray,1.2,5)
    font=cv2.FONT_HERSHEY_SIMPLEX
    jumlah=0

    for(x,y,w,h) in deteksi:
        jumlah=jumlah+1
        cv2.putText(img,"Wajah",(x+90,y-15),font,0.75,(235,206,135),2,cv2.LINE_AA)
        cv2.rectangle(img,(x,y),(x+w,y+h),(114,128,250),2)
        rGray=gray[y:y+h,x:x+w]
        color=img[y:y+h,x:x+w]

    width = 720
    height = 500
    size = (width,height)

    newSize = cv2.resize(img,size)
    cv2.putText(newSize,"jumlah wajah : "+str(jumlah)+" buah",(10,30),font,1,(0,0,0),2)
    cv2.imshow('deteksi wajah',newSize)
    k=cv2.waitKey(30)&0xff
    if k ==27:
        break

cam.release()
cv2.destroyAllWindows()
