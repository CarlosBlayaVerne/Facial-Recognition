import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
import face_recognition



def __draw_label(img, text, pos, bg_color):
    #font_face = cv2.FONT_HERSHEY_SIMPLEX
    font_face = cv2.FONT_ITALIC
    scale = 0.4
    color = (0, 0, 0)
    thickness = cv2.FILLED
    margin = 2

    txt_size = cv2.getTextSize(text, font_face, scale, thickness)

    end_x = pos[0] + txt_size[0][0] + margin
    end_y = pos[1] - txt_size[0][1] - margin

    cv2.rectangle(img, pos, (end_x, end_y), bg_color, thickness)
    cv2.putText(img, text, pos, font_face, scale, color, 1, cv2.LINE_AA)



cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

video_capture = cv2.VideoCapture(0)
#video_capture = cv2.VideoCapture("rtsp://admin:s0l4dm.45@10.2.10.40:554/h264/ch1/main/av_stream")
anterior = 0

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    count=0
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imwrite( "frame%d.jpg" % count, frame) 
        count += 1
        print ("frame%d.jpg" % count)

        imagen = "samuel1.jpeg"
        known_image = face_recognition.load_image_file(imagen)
        biden_encoding = face_recognition.face_encodings(known_image)[0]
        try:
            unknown_encoding = face_recognition.face_encodings(frame)[0]
            #Makes face comparison between teo images konw and unknow
            results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
            #we get the face location from the unknow image for the face recognice
            image = face_recognition.load_image_file(imagen)
            face_locations = face_recognition.face_locations(image)
            print(results[0])
            # draw the label into the frame
            if(results[0]==True):
                __draw_label(frame, 'Cara Encontrada Samuel Pineiro', (x,y), (255,0,0))
                cv2.imshow('Frame',frame)

        except IndexError as e:
            print(e)


    if anterior != len(faces):
        anterior = len(faces)
        log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))


    # Display the resulting frame
    cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame
    cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()


