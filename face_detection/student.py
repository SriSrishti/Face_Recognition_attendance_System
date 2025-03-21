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

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student_Detail")


        # ===========Variables=============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        # first_image
        img = Image.open(r"images\student_detail_img\students_group.webp")
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
        img2 = Image.open(r"images\student_detail_img\notebook.jpeg")
        img2 = img2.resize((450, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=450, height=130)

         # background_image
        img3 = Image.open(r"images\student_detail_img\bg_img.jpeg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1500, height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="sky blue",fg="blue")
        title_lbl.place(x=0, y=5, width=1530, height=40)

        
        # main_frame
        main_frame=Frame(bg_img, bd=2, bg="lightgreen")
        main_frame.place(x=20,y=50,width=1320,height=500)

        # Left lable frame
        Left_frame=LabelFrame(main_frame,bd=2, relief=RIDGE, bg="lightpink", text="Student Details", font=("Times New Roman",12,"bold"))
        Left_frame.place(x=10, y=15, width=650, height=470)

        img_left = Image.open(r"images\student_detail_img\group_Std.jpeg")
        img_left = img_left.resize((250, 50), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=150, y=0, width=250, height=50)

        # curret_course
        current_course=LabelFrame(Left_frame,bd=2, relief=RIDGE, bg="lightblue", text="Current Course Information", font=("Times New Roman",12,"bold"))
        current_course.place(x=5, y=55, width=630, height=120)

        # department label
        dep_label = Label(current_course,text="Department:",font=("Times New Roman",12,"bold"), bg="lightblue", )
        
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo=ttk.Combobox(current_course,textvariable=self.var_dep,font=("Times New Roman",12,"bold"),width=17, state="readonly")
        
        dep_combo['values']=("Select Department","Engineering & Technology","Business & Management","Computer & IT Courses")
       
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1,padx=2,pady=10, sticky=W)

        # Course
        course_label = Label(current_course,text="Course:",font=("Times New Roman",12,"bold"), bg="lightblue", )
        
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo=ttk.Combobox(current_course,textvariable=self.var_course,font=("Times New Roman",12,"bold"),width=20, state="readonly")
        
        course_combo['values']=("Select Course","Bachelor of Computer Applications (BCA)","Master of Computer Application (MCA)","Cybersecurity","Ethical Hacking","Cloud Computing","Artificial Intelligence","Data Science")
       
        course_combo.current(0)
        course_combo.grid(row=0, column=3,padx=2,pady=10, sticky=W)

        # year
        year_label = Label(current_course,text="Session:",font=("Times New Roman",12,"bold"), bg="lightblue", )
        
        year_label.grid(row=1, column=0, padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course,textvariable=self.var_year,font=("Times New Roman",12,"bold"),width=17, state="readonly")
        
        year_combo['values']=("Select Session","2020-2022","2021-2023","2022-2024","2023-2025","2024-2026","2025-2027")
       
        year_combo.current(0)
        year_combo.grid(row=1, column=1,padx=2,pady=10, sticky=W)

        # Semester label
        semester_label = Label(current_course,text="Semester:",font=("Times New Roman",12,"bold"), bg="lightblue", )
        
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo=ttk.Combobox(current_course,textvariable=self.var_sem,font=("Times New Roman",12,"bold"), width=20, state="readonly")
        
        semester_combo['values']=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6","Sem-7","Sem-8")
       
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3,padx=2,pady=10, sticky=W)

        
        # Class Student Information
        class_student=LabelFrame(Left_frame,bd=2, relief=RIDGE, bg="lightblue", text="Class Student Information", font=("Times New Roman",12,"bold"))
        class_student.place(x=5, y=180, width=630, height=260)

        # Student ID
        studentId_label = Label(class_student, text="Student Id:", font=("Times New Roman", 12, "bold"), bg="lightblue")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry = ttk.Entry(class_student, textvariable=self.var_std_id, width=17, font=("Times New Roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)
        studentID_entry.bind("<FocusOut>", self.validate_student_id)  # Validate on focus out

        # Student Name
        studentName_label = Label(class_student, text="Student Name:", font=("Times New Roman", 12, "bold"), bg="lightblue")
        studentName_label.grid(row=0, column=2, padx=10, sticky=W)

        studentName_entry = ttk.Entry(class_student, textvariable=self.var_std_name, width=17, font=("Times New Roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, sticky=W)
        studentName_entry.bind("<FocusOut>", self.validate_name)  # Validate on focus out

        # Class Division
        class_div_label = Label(class_student, text="Class Div.:", font=("Times New Roman", 12, "bold"), bg="lightblue")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        div_combo = ttk.Combobox(class_student, textvariable=self.var_div, width=15, font=("Times New Roman", 12, "bold"), state="readonly")
        div_combo["values"] = ("A", "B", "C", "D", "E", "F")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        roll_no_label = Label(class_student, text="Roll No.:", font=("Times New Roman", 12, "bold"), bg="lightblue")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student, textvariable=self.var_roll, width=17, font=("Times New Roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender (Dropdown)
        gender_label = Label(class_student, text="Gender:", font=("Times New Roman", 12, "bold"), bg="lightblue")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student, textvariable=self.var_gender, width=15, font=("Times New Roman", 12, "bold"), state="readonly")
        gender_combo["values"] = ("Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date of Birth (Date Picker)
        dob_label = Label(class_student, text="D.O.B.:", font=("Times New Roman", 12, "bold"), bg="lightblue")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = DateEntry(class_student, textvariable=self.var_dob, width=15, font=("Times New Roman", 12, "bold"), background="darkblue", foreground="white", borderwidth=2)
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_student, text="E-mail:", font=("Times New Roman", 12, "bold"), bg="lightblue")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student, textvariable=self.var_email, width=17, font=("Times New Roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        email_entry.bind("<FocusOut>", self.validate_email) 

        # Address
        address_label = Label(class_student,text="Address:",font=("Times New Roman",12,"bold"), bg="lightblue", )
        address_label.grid(row=3, column=2, padx=10,pady=5 ,sticky=W)

        address_entry=ttk.Entry(class_student,textvariable=self.var_address,width=17,font=("Times New Roman",12,"bold"))
        address_entry.grid(row=3, column=3,padx=10,pady=5, sticky=W)

        # Phone Number
        phone_label = Label(class_student, text="Phone No.:", font=("Times New Roman", 12, "bold"), bg="lightblue")
        phone_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student, textvariable=self.var_phone, width=17, font=("Times New Roman", 12, "bold"))
        phone_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)
        phone_entry.bind("<FocusOut>", self.validate_phone)  # Validate on focus out

        # Teacher Name
        teacher_label = Label(class_student,text="Teacher Name:",font=("Times New Roman",12,"bold"), bg="lightblue", )
        teacher_label.grid(row=4, column=2, padx=10,pady=5 ,sticky=W)

        teacher_entry=ttk.Entry(class_student,textvariable=self.var_teacher,width=17,font=("Times New Roman",12,"bold"))
        teacher_entry.grid(row=4, column=3,padx=10,pady=5, sticky=W)

        

        # Radio Buttons
        # Radio button 1
        self.var_radio1=StringVar()
        radio_btn1=ttk.Radiobutton(class_student,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radio_btn1.grid(row=6, column=0, padx=5, pady=5)

        # take photo sample
        take_photo=Button(class_student,text="Take photo", width=10,command=self.generate_dataset,font=("Times New Roman",12,"bold"), bg="lightgreen",fg="black")
        take_photo.grid(row=6, column=1)

        # update photo
        update_photo=Button(class_student,text="Update photo", width=10,font=("Times New Roman",12,"bold"), bg="lightgreen",fg="black")
        update_photo.grid(row=6, column=2)

        # radio button 2
        self.var_radio2=StringVar()
        radio_btn2=ttk.Radiobutton(class_student,variable=self.var_radio1,text="No Photo Sample",value="No")
        radio_btn2.grid(row=6, column=3, padx=5, pady=5)

        # Button_frame
        btn_frame=Frame(class_student, bd=2, relief=RIDGE, bg="lightgreen")
        btn_frame.place(x=0,y=200,width=600, height=35)

        # save button
        save_btn=Button(btn_frame,text="Save", command=self.add_data, width=15,font=("Times New Roman",12,"bold"), bg="blue",fg="white")
        save_btn.grid(row=0, column=0)
        
         #Update button
        update_btn=Button(btn_frame,text="Update",command=self.update_data ,width=15,font=("Times New Roman",12,"bold"), bg="blue",fg="white")
        update_btn.grid(row=0, column=1,padx=4)
        
         #Delete button
        delete_btn=Button(btn_frame,text="Delete", command=self.delete_data,width=15,font=("Times New Roman",12,"bold"), bg="blue",fg="white")
        delete_btn.grid(row=0, column=2,padx=4)

         #Reset button
        reset_btn=Button(btn_frame,text="Reset", command=self.reset_data,width=15,font=("Times New Roman",12,"bold"), bg="blue",fg="white")
        reset_btn.grid(row=0, column=3, padx=4)

        # Right lable frame
        Right_frame=LabelFrame(main_frame,bd=2, relief=RIDGE, bg="lightpink", text="Student Details", font=("Times New Roman",12,"bold"))
        Right_frame.place(x=670, y=15, width=640, height=470)

        # image right
        img_right = Image.open(r"images\student_detail_img\student_Details.jpeg")
        img_right = img_right.resize((150, 50), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=200, y=0, width=150, height=50)

        # Search System
        search_frame=LabelFrame(Right_frame,bd=2, relief=RIDGE, bg="lightblue", text="Search System", font=("Times New Roman",12,"bold"))
        search_frame.place(x=5, y=55, width=620, height=75)

        # 
        search_label = Label(search_frame,text="Search By:",font=("Times New Roman",12,"bold"), bg="lightblue", )
        search_label.grid(row=0, column=0, padx=10,pady=5 ,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("Times New Roman",12,"bold"),width=12, state="readonly")
        
        search_combo['values']=("Select","Roll_No","Phone No.")
       
        search_combo.current(0)
        search_combo.grid(row=0, column=1,padx=2,pady=10, sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("Times New Roman",12,"bold"))
        search_entry.grid(row=0, column=2,padx=5, sticky=W)

        #search button
        search_btn=Button(search_frame,text="Search", width=12,font=("Times New Roman",12,"bold"), bg="lightgreen",fg="black")
        search_btn.grid(row=0, column=3, padx=2)

        showAll_btn=Button(search_frame,text="Show All", width=12,font=("Times New Roman",12,"bold"), bg="lightgreen",fg="black")
        showAll_btn.grid(row=0, column=4, padx=2)


        # Table Frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="lightblue")
        table_frame.place(x=5, y=150, width=620, height=290)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, 
                                          columns=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), 
                                          xscrollcommand=scroll_x.set, 
                                          yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Times New Roman", 12,"bold"))

        # Corrected Column Headings
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Div")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo")
        self.student_table["show"] = "headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)
        
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease >", self.get_cursor)
        self.fetch_data()

    # Validation Functions
    def validate_student_id(self, event):
        student_id = self.var_std_id.get()
        if not re.match(r"^F-\d{4}-\d{4}$", student_id):
            messagebox.showerror("Error", "Student ID must be in the format F-YYYY-NNNN where Y is year and N is number.")
            self.var_std_id.set("")

    def validate_name(self, event):
        name = self.var_std_name.get()
        if not name.istitle():
            messagebox.showerror("Error", "Name must start with a capital letter.")
            self.var_std_name.set("")

    def validate_email(self, event):
        email = self.var_email.get()
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            messagebox.showerror("Error", "Invalid email format. It must end with @domainname.com")
            self.var_email.set("")

    def validate_phone(self, event):
        phone = self.var_phone.get()
        if not re.match(r"^\d{10}$", phone):
            messagebox.showerror("Error", "Phone number must be exactly 10 digits.")
            self.var_phone.set("")


    # ============Function declartion===========
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==" " or self.var_std_id.get()==" ":
            messagebox.showerror("Error","All fields are required.",parent=self.root)
        else:
            try:
                conn = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="Kumari@123",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO student (Dep, Course, Year, Semester, Student_id, Name, Division, Roll, Gender, Dob, Email, Phone, Address, Teacher, PhotoSample) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get()
                    )
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully!!", parent=self.root)
            except mysql.connector.Error as es:
                messagebox.showerror("Error", f"MySQL Error: {str(es)}", parent=self.root)
                print(f"MySQL Error: {str(es)}")  # Additional logging
            except Exception as e:
                messagebox.showerror("Error", f"Unexpected Error: {str(e)}", parent=self.root)
                print(f"Unexpected Error: {str(e)}")  # Additional logging)

    # ==========fetch data ============
    def fetch_data(self):
        conn = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="Kumari@123",
                    database="face_recognizer"
                )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ==========Get Cursor========
    def get_cursor(self,event = ""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_sem.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    # ==========Update Function========
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()==" " or self.var_std_id.get()==" ":
            messagebox.showerror("Error","All fields are required.",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details?",parent=self.root)
                if Update>0:
                    conn = pymysql.connect(
                        host="localhost",
                        user="root",
                        password="Kumari@123",
                        database="face_recognizer"
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated!!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

    # ==========Delete Function========
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required.",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student details?",parent=self.root)
                if delete>0:
                    conn = pymysql.connect(
                        host="localhost",
                        user="root",
                        password="Kumari@123",
                        database="face_recognizer"
                    )
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
   
    # ==========Reset Function========
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    
    # ==========Generate Data Set or Take Photo Sample========
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required.", parent=self.root)
        else:
            try:
                conn = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="Kumari@123",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1

                # Update the student record with the correct Student_id
                my_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()  # Use the correct Student_id value
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data on face frontals from OpenCV
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    cropped_face = face_cropped(my_frame)
                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (450, 450))  # Resize the cropped face
                        # Save the face in color (do not convert to grayscale)
                        file_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:  # Stop when Enter key is pressed or 100 images are captured
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed!!")
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
                

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()