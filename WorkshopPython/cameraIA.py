import os
import cv2 as cv2
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import webbrowser
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import h5py
from keras.models import load_model
from keras.models import save
from Stat import count
from Stat import stat
from Stat import StatFirebase
from FirebaseQuentin.connect import insertEmotion
import emoji
import tkinter as tk

path = "EmotionStat.txt"

f = open(path, "a", encoding="utf-8")

# load model
model = load_model(r"C:\Users\loicr\Desktop\EPSI\I1\workshop_Quentin\WorkshopPython\best_model.h5")

face_haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, test_img = cap.read()  # captures frame and returns boolean value and captured image
    if not ret:
        continue
    gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)

    faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)

    for (x, y, w, h) in faces_detected:
        cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)
        roi_gray = gray_img[y:y + w, x:x + h]  # cropping region of interest i.e. face area from  image
        roi_gray = cv2.resize(roi_gray, (224, 224))
        img_pixels = image.img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis=0)
        img_pixels /= 255

        predictions = model.predict(img_pixels)

        # find max indexed array
        max_index = np.argmax(predictions[0])

        emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
        predicted_emotion = emotions[max_index]

        cv2.putText(test_img, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        print(predicted_emotion)
        insertEmotion(predicted_emotion)
        f.write(predicted_emotion)
        f.write("\n")
        if predicted_emotion == "disgust":
            webbrowser.open("https://www.youtube.com/watch?v=kqS92AVScEU%22")
            exit()
        if predicted_emotion == "angry":
            #print(emoji.emojize(":angry:"))
            tk.Button(text='\U0001F620', font=("", 100)).pack()        
            tk.mainloop()
        if predicted_emotion == "surprise":
            print(emoji.emojize(":open_mouth:"))
            tk.Button(text='\U0001F62F', font=("", 100)).pack()        
            tk.mainloop()
            exit()
        if predicted_emotion == "fear":
            print(emoji.emojize(":fearful:"))
            tk.Button(text='\U0001F628', font=("", 100)).pack()        
            tk.mainloop()
            exit()
        if predicted_emotion == "happy":
            tk.Button(text='\U0001F64B', font=("", 100)).pack()        
            tk.mainloop()
            exit()
        if predicted_emotion == "sad":
            tk.Button(text='\U0001F622', font=("", 100)).pack()        
            tk.mainloop()
            exit()
        if predicted_emotion == "neutral":
            print(emoji.emojize(":neutral_face:"))
            tk.Button(text='\U0001F610', font=("", 100)).pack()        
            tk.mainloop()
            exit()

    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('Facial emotion analysis ', resized_img)

    if cv2.waitKey(10) == ord('q'):  # wait until 'q' key is pressed
        break

cap.release()
cv2.destroyAllWindows
f.close()
print("-----------------")
#count("EmotionStat.txt")
print("-----------------")
#stat("EmotionStat.txt")