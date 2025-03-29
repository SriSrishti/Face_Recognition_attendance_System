from os import DirEntry
import re
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import pymysql
from tkcalendar import DateEntry
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 25, "bold"), bg="sky blue", fg="green")
        title_lbl.place(x=0, y=5, width=1530, height=40)

        # first image
        img_top = Image.open(r"images/Face_Detect/face-recognition.jpg")
        img_top = img_top.resize((1500, 650), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1500, height=650)

        # button
        b1_1 = Button(f_lbl, text="Face Recognition", command=self.face_recog, width=10, font=("Times New Roman", 18, "bold"), bg="blue", fg="white")
        b1_1.place(x=850, y=500, width=200, height=40)

    # =============face recognition==================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                # Default values if no record found
                n, r, d = "Unknown", "Unknown", "Unknown"

                try:
                    conn = pymysql.connect(host="localhost", user="root", password="Kumari@123", database="face_recognizer")
                    my_cursor = conn.cursor()

                    # Get student details
                    my_cursor.execute("SELECT Name, Roll, Dep FROM student WHERE Student_id=%s", (id,))
                    result = my_cursor.fetchone()  # Fetch one row instead of fetchall()
                    
                    if result:
                        n, r, d = result  # Correctly unpack the fetched data

                except Exception as e:
                    messagebox.showerror("Error", f"Error due to: {str(e)}")
                finally:
                    if 'conn' in locals():
                        conn.close()

                if confidence > 37:  # Lowered confidence threshold for better results
                    cv2.putText(img, f"ID: {id}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Dep.: {d}", (x, y - 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

            return img


        def recognize(img, clf, faceCascade):
            coords = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture = cv2.VideoCapture(0)
        while True:
            ret, img = video_capture.read()
            if not ret:
                break
            
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # 13 is the Enter Key
                break

        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
