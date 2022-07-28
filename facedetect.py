# import cv2
# trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# img=cv2.imread('index.jpg')
# # cv2.imshow('facedetect', img)

# grayscaled_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)
# for i in face_coordinates:
#     [x,y,w,h]=i
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# cv2.imshow('facedetect',img)
# cv2.waitKey()
# print('Code Completed')
import cv2
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
webcam=cv2.VideoCapture(0)
# key=cv2.waitKey(1)
# cv2.imshow('facedetect', img)
while True:
    successful_frame_read,img=webcam.read()
    grayscaled_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)
    for i in face_coordinates:
        [x,y,w,h]=i
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('facedetect',img)
    key=cv2.waitKey(1)
    if key==81 or key==113:
        break
webcam.release()
print('Code Completed')
