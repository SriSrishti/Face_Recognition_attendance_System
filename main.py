from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Load and resize image
        # first_image
        img = Image.open(r"images\f_r_1.jpeg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # level of image
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # second-image
        img1 = Image.open(r"images\face_2.jpeg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # level of image
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # third image
        img2 = Image.open(r"images\fr_3.jpeg")
        img2 = img2.resize((450, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Corrected: Use 'image' instead of 'Image'
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=450, height=130)
        
        # background_image
        img3 = Image.open(r"images\bg_img.jpeg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

       
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="sky blue",fg="purple")
        title_lbl.place(x=0, y=0, width=1450, height=30)


        # student button
        img4 = Image.open(r"images\student_img.jpeg")
        img4 = img4.resize((200,200), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150, y=100, width=200, height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2", font=("times new roman",15,"bold"),bg="sky blue",fg="black")
        b1_1.place(x=150, y=300, width=200, height=30)

        # detect face
        img5 = Image.open(r"images\detect_Face.jpeg")
        img5 = img5.resize((200,200), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b2.place(x=450, y=100, width=200, height=200)

        b2_1=Button(bg_img,text="Face Detector",cursor="hand2", font=("times new roman",15,"bold"),bg="sky blue",fg="black")
        b2_1.place(x=450, y=300, width=200, height=30)

        # Attendance Button
        img6 = Image.open(r"images\attendance_btn.jpeg")
        img6 = img6.resize((200,200), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b3.place(x=750, y=100, width=200, height=200)

        b3_1=Button(bg_img,text="Attendance",cursor="hand2", font=("times new roman",15,"bold"),bg="sky blue",fg="black")
        b3_1.place(x=750, y=300, width=200, height=30)

        # Help btn
        img7 = Image.open(r"images\Help.jpeg")
        img7 = img7.resize((200,200), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b4.place(x=1050, y=100, width=200, height=200)

        b4_1=Button(bg_img,text="How May I Help You?",cursor="hand2", font=("times new roman",15,"bold"),bg="sky blue",fg="black")
        b4_1.place(x=1050, y=300, width=200, height=30)

        # Train Data
        img8 = Image.open(r"images\data_train.jpeg")
        img8 = img8.resize((200,200), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b5.place(x=150, y=350, width=200, height=150)

        b5_1=Button(bg_img,text="Train Data",cursor="hand2", font=("times new roman",15,"bold"),bg="sky blue",fg="black")
        b5_1.place(x=150, y=500, width=200, height=30)

        # Photos Folders
        img9 = Image.open(r"images\img_folder.jpeg")
        img9 = img9.resize((200,200), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=450, y=350, width=200, height=150)

        b6_1=Button(bg_img,text="Images_store",cursor="hand2",command=self.open_img, font=("times new roman",15,"bold"),bg="sky blue",fg="black")
        b6_1.place(x=450, y=500, width=200, height=30)


         # Developer_details
        img11 = Image.open(r"images\developer.jpeg  ")
        img11 = img11.resize((200,200), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b8.place(x=750, y=350, width=200, height=150)

        b8_1=Button(bg_img,text="Developer_details",cursor="hand2", font=("times new roman",15,"bold"),bg="sky blue",fg="black")
        b8_1.place(x=750, y=500, width=200, height=30)


        # Exit btn
        img12 = Image.open(r"images\exit_btn.webp ")
        img12 = img12.resize((200,200), Image.Resampling.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b9=Button(bg_img,image=self.photoimg12,cursor="hand2")
        b9.place(x=1050, y=350, width=200, height=150)

        b9_1=Button(bg_img,text="Exit",cursor="hand2", font=("times new roman",15,"bold"),bg="sky blue",fg="black")
        b9_1.place(x=1050, y=500, width=200, height=30)

    
    def open_img(self):
        os.startfile("data") 
    # ================Function Button===================
    def student_details(self):
        self.new_window= Toplevel(self.root)
        self.app=Student(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
