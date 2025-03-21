from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Load and resize image
        # first_image
        img = Image.open(r"C:\Users\Smriti\Documents\Python_Projects\face_detection\images\f_r_1.jpeg")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # level of image
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # second-image
        img1 = Image.open(r"C:\Users\Smriti\Documents\Python_Projects\face_detection\images\face_2.jpeg")
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # third image
        img2 = Image.open(r"C:\Users\Smriti\Documents\Python_Projects\face_detection\images\fr_3.jpeg")
        img2 = img2.resize((450, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=450, height=130)
        
        # background_image
        img3 = Image.open(r"C:\Users\Smriti\Documents\Python_Projects\face_detection\images\bg_img.jpeg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", 
                          font=("times new roman", 30, "bold"), bg="sky blue", fg="purple")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Button settings
        button_width = 200
        button_height = 200
        start_x = 250  # Adjusted to center buttons properly
        start_y = 100
        gap_x = 250
        gap_y = 250

        # Student button
        img4 = Image.open(r"C:\Users\Smriti\Documents\Python_Projects\face_detection\images\student_img.jpeg")
        img4 = img4.resize((button_width, button_height), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, cursor="hand2")
        b1.place(x=start_x, y=start_y, width=button_width, height=button_height)

        b1_1 = Button(bg_img, text="Student Details", cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="sky blue", fg="black")
        b1_1.place(x=start_x, y=start_y + button_height, width=button_width, height=30)

        # Face Detector
        img5 = Image.open(r"C:\Users\Smriti\Documents\Python_Projects\face_detection\images\detect_Face.jpeg")
        img5 = img5.resize((button_width, button_height), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b2.place(x=start_x + gap_x, y=start_y, width=button_width, height=button_height)

        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="sky blue", fg="black")
        b2_1.place(x=start_x + gap_x, y=start_y + button_height, width=button_width, height=30)

        # Attendance Button
        img6 = Image.open(r"C:\Users\Smriti\Documents\Python_Projects\face_detection\images\attendance_btn.jpeg")
        img6 = img6.resize((button_width, button_height), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b3.place(x=start_x + gap_x * 2, y=start_y, width=button_width, height=button_height)

        b3_1 = Button(bg_img, text="Attendance", cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="sky blue", fg="black")
        b3_1.place(x=start_x + gap_x * 2, y=start_y + button_height, width=button_width, height=30)

        # Help Button
        img7 = Image.open(r"C:\Users\Smriti\Documents\Python_Projects\face_detection\images\Help.jpeg")
        img7 = img7.resize((button_width, button_height), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b4.place(x=start_x + gap_x * 3, y=start_y, width=button_width, height=button_height)

        b4_1 = Button(bg_img, text="Help", cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="sky blue", fg="black")
        b4_1.place(x=start_x + gap_x * 3, y=start_y + button_height, width=button_width, height=30)

        # Second Row
        start_y += gap_y

        # Train Data
        img8 = Image.open(r"C:\Users\Smriti\Documents\Python_Projects\face_detection\images\data_train.jpeg")
        img8 = img8.resize((button_width, button_height), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b5.place(x=start_x, y=start_y, width=button_width, height=button_height)

        b5_1 = Button(bg_img, text="Train Data", cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="sky blue", fg="black")
        b5_1.place(x=start_x, y=start_y + button_height, width=button_width, height=30)

        # Photos Folder
        img9 = Image.open(r"C:\Users\Smriti\Documents\Python_Projects\face_detection\images\img_folder.jpeg")
        img9 = img9.resize((button_width, button_height), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b6.place(x=start_x + gap_x, y=start_y, width=button_width, height=button_height)

        b6_1 = Button(bg_img, text="Images Store", cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="sky blue", fg="black")
        b6_1.place(x=start_x + gap_x, y=start_y + button_height, width=button_width, height=30)

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
