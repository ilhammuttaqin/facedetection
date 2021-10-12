import cv2

wajah = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('gambar.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

deteksi=wajah.detectMultiScale(gray,1.1,5)
font=cv2.FONT_HERSHEY_SIMPLEX
jumlah=0

for(x,y,w,h) in deteksi:
    jumlah=jumlah+1
    cv2.putText(img,"wajah",(x,y-15),font,0.75,(0,0,255),2,cv2.LINE_AA)
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    rGray=gray[y:y+h,x:x+w]
    color=img[y:y+h,x:x+w]

width = 720
height = 480
size = (width,height)

newSize = cv2.resize(img,size)

cv2.putText(newSize,"jumlah wajah : "+str(jumlah)+" buah",(10,30),font,1,(0,0,0))
cv2.imshow('img',newSize)
cv2.waitKey(0)
cv2.destroyAllWindows()
