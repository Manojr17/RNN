import cv2
from PIL.features import features
from keras.models import model_from_json
import numpy as np
from keras.src.utils.dataset_utils import labels_to_dataset

from main import prediction

json_file=open("emotionRecognition.json","r")
model_json=json_file.read()
json_file.close()
model=model_from_json(model_json)
model.load_weights("emotionRecognition.keras")
haar_file=cv2.data.haarcascades+"haarcascade_frontalface_default.xml"
face_cascade=cv2.CascadeClassifier(haar_file)

def extract_features(image):
    feature=np.array(image)
    feature=feature.reshape(1,48,48,1)
    return feature / 255.0


webcam=cv2.VideoCapture(0)
labels={0 : "angry" , 1 : "disgust" , 2 : "fear" , 3 : "happy" , 4 : "neutral" ,
        5 : "sad" ,6 : "surprise"}
screen_width = 1366
screen_height = 768


cv2.namedWindow("Output",cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Output", cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

while True:
     i , im = webcam.read()
     gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiSacle(im, 1.3, 5)
     try:
         for (p, q, r, s) in faces:
             image = gray[q:q + s, p:p + r]
             cv2.rectangle(im,(p,q),(p + r,q + s),(255, 0 ,0), 2)
             image = cv2.resize(image,(48, 48))
             img = extract_features(image)
             pred = model.predict(img)
             prediction_label = labels[pred.argmax()]
             cv2.putText(im, "% s" %(prediction_label),(p - 10, q - 10),
                         cv2.FONT_HERSHEY_COMPLEX_SMALL, 2,(0,0, 255))

         im = cv2.resize(im,(screen_width, screen_height))

         cv2.imshow("Output", im)

         if cv2.waitkey(1) == 27:
             break

     except cv2.error:
         pass

webcam.release()
cv2.destroyAllWindows()

