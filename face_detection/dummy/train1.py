from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Train Data Set",font=("times new roman",25,"bold"),bg="sky blue",fg="blue")
        title_lbl.place(x=0, y=5, width=1530, height=40)

        # top image
        img_top = Image.open(r"images\train_data_img\trained_Data_1.jpeg")
        img_top = img_top.resize((1530, 300), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1530, height=350)

        
        # button
        b1_1=Button(self.root,text="Train Data",command=self.train_classifier, width=10,font=("Times New Roman",30,"bold"), bg="lightgreen",fg="black")
        b1_1.place(x=0, y=350, width=1530, height=40)

        # bottom_image
        img_bottom = Image.open(r"images\train_data_img\trained_data_2.jpeg")
        img_bottom = img_bottom.resize((1530, 300), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=390, width=1530, height=300)

    #================Function=============
    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = cv2.imread(image)  # Load color image
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
            imageNp = np.array(gray_img, 'uint8')  # Convert to NumPy array
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", gray_img)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        # Train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
