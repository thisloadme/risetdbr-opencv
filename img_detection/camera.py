import cv2
# Load file cascade untuk mendeteksi wajah
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Buka kamera laptop
cap = cv2.VideoCapture(0)
while True:
    # Baca frame dari kamera
    ret, img = cap.read()
    # Ubah gambar ke skala abu-abu
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Deteksi wajah dalam gambar skala abu-abu
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # Gambar kotak biru di sekitar wajah yang terdeteksi
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    # Tampilkan gambar hasil deteksi
    cv2.imshow('img',img)
    # Tekan ESC untuk keluar program
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# Tutup kamera dan jendela program
cap.release()
cv2.destroyAllWindows()