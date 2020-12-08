# this is the logging page for the application

from forLabAssist import forLabAssist
from forPatients import forPatient
from tkinter import *  # for the GUI components
import tkinter.messagebox  # to notify the user about warning and others
import pymysql  # to establish connection to MySQL database
from PIL import ImageTk, Image


#import forPatients
#import forLabAssist
#import forPhi


class login():         # define our class as login and inherit tk class to this class
    # this is the default constructor and it will call as soon as instance of this class is created or basically initializing the class
    def __init__(self, root):
        # ========login page design goes under here======================
        self.root = root
        self.root.title("LOGIN")  # set the title bar name
        # set the size of the loginpage and put the X and Y cordinates for top left corner
        self.root.geometry("1000x600+400+200")
        self.root.iconbitmap("images/icon1.ico")  # set the icon for title bar
        # =====background image================
        self.bg = ImageTk.PhotoImage(Image.open(
            "images/bg02.jpg"))  # define the image
        self.bg_image = Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)
        self.root.resizable(False, False)  # to avoid the maximize option

    # =========main title label=================================
        title = Label(self.root, text="PCR Test Management\n System", font=(
            "Impact", 30, "bold"), fg="#03506f", anchor=CENTER, bg='#ffffff')
        title.pack(side=TOP, pady=20, padx=10)

    # ====================User selection frame goes under here==================
        userSelect_Frame = Frame(self.root, bg='#d0e8f2')
        userSelect_Frame.place(x=150, y=150, height=330, width=500)

    # ==================to select the user type==================================
        self.user = IntVar()

        # radio button definition
        self.phi_user = Radiobutton(
            userSelect_Frame,
            text='PHI',
            variable=self.user,
            value=1,
            bg='#d0e8f2', font=("Impact", 15),
            fg="#03506f", width=10)

        self.patient = Radiobutton(
            userSelect_Frame,
            text='Patient',
            variable=self.user,
            value=2,
            bg='#d0e8f2',
            font=("Impact", 15),
            fg="#03506f", width=10)

        self.lab_user = Radiobutton(
            userSelect_Frame,
            text='Lab Assistant',
            variable=self.user,
            value=3, bg='#d0e8f2',
            font=("Impact", 15),
            fg="#03506f", width=10)

        # radio button placement inside the frame
        self.phi_user.grid(row=0, column=0)
        self.patient.grid(row=0, column=1)
        self.lab_user.grid(row=0, column=2)

        # defaultly select the patient radio button
        self.user.set(2)

    # ====================Login frame goes under here!==========================
        main_Frame = Frame(self.root, bg='#d0e8f2')
        main_Frame.place(x=150, y=200, height=330, width=500)

    # =================user name field and password field
        # FOR THE    PICTURE
        self.user_image = PhotoImage(file="images/userName.png")
        userName_Label = Label(
            main_Frame, image=self.user_image, bg='#d0e8f2', width=128, height=128)
        userName_Label.grid(row=1, column=0)
        # FOR THE INPUT FIELD

        self.userName = Entry(main_Frame, fg='#03506f', font=(
            "Goudy old style", 20, "bold"), bg="lightgray", justify=CENTER)
        self.userName.grid(row=1, column=1, padx=10, pady=10)

        # FOR  THE PASSWORD PICTURE
        self.pwd_image = PhotoImage(file="images/pwd.png")
        pwd_pic_Label = Label(main_Frame, image=self.pwd_image,
                              bg='#d0e8f2', width=128, height=50)
        pwd_pic_Label.grid(row=2, column=0)

        # FOR THE PASSWORD INPUT FIELD
        self.pwd = Entry(main_Frame, fg='#03506f', font=(
            "Goudy old style", 20, "bold"), bg="lightgray", show="*", justify=CENTER)
        self.pwd.grid(row=2, column=1, padx=10, pady=50)

        # =============================button functionality=================================
        # ====exit button in the login form========================

        def iExit():
            userRespond = tkinter.messagebox.askokcancel(
                "PCR SYSTEM", "Confirm if you want to exit")

            if userRespond > 0:
                root.destroy()
                return

            # ========for the login to the system===========================

        def rootLogin():
            # first lets get all the input from the form
            radio_button_Input = self.user.get()
            userNameField = self.userName.get()
            userPassword = self.pwd.get()

            # lets check for the validity of the data
            if radio_button_Input == 1:
                userType = "phi"  # for PHI
            elif radio_button_Input == 2:
                userType = "pati"  # for patients
            else:
                userType = "lab"  # for lab assistant

            # check the password field and username validity
            if(len(userNameField) == 0 or len(userPassword) == 0):
                tkinter.messagebox.showwarning(
                    "INVALID DATA!", "OOPS! Empty data Fields! ")

            # then we have to create  the database connection and check for the credintilas
            sqlConnect = pymysql.connect(
                host="localhost", user="root", password="", database="pcr_system_db")

            # this is the cursor to manipulate db data
            cur = sqlConnect.cursor()

            # lets execute the queary upon that data base and fetch the data
            cur.execute("SELECT * FROM logindata WHERE userName LIKE (%s) AND userType =(%s)",
                        (str(userNameField), str(userType)))

            self.allowAccess = False       # to track the access to the program
            result = cur.fetchall()  # fetch all available result in the database

            sqlConnect.commit() #commit all the queries 
            sqlConnect.close()  #and close the data base connection

            if len(result) != 0:  # Which mean it has some data fot given password and user type
                for rows in result:
                    if rows[1] == userNameField and rows[2] == userPassword:
                        self.allowAccess = True

            else:
                tkinter.messagebox.showwarning(
                    "INVALID DATA!", "Username or Password is incorrect")
                self.userName.delete(0, END)  # to reset the data entry fields
                self.pwd.delete(0, END)

            if(self.allowAccess):
                tkinter.messagebox.showinfo("Successful Login!", "\tWelcome to \nPCR Management System!")
                # now we have to open the corresponding page according to the userType
                if(userType == "pati"):
                    import forPatients
                    root2=Tk()
                    app2=forPatients.forPatient(root2)
                    root.destroy()
                    root2.mainloop()
                elif(userType == "phi"):
                    import forPhi
                    root3=Tk()
                    app3=forPhi.forPhi(root3)
                    root.destroy()
                    root3.mainloop()
                elif(userType=="lab"):
                    import forLabAssist
                    root4=Tk()
                    app4=forLabAssist.forLabAssist(root4)
                    root.destroy()
                    root4.mainloop()
                    
                  # and destroy current page

    # =================login button and the exit button goes here=======================
        login_Button = Button(main_Frame, text="LOGIN", font=(
            "Goudy old style", 15, "bold"), bg="white", justify=CENTER, command=rootLogin)
        login_Button.place(x=140, y=250, width=100)

        exit_Button = Button(main_Frame, text="EXIT", font=(
            "Goudy old style", 15, "bold"), fg="red", justify=CENTER, command=iExit)
        exit_Button.place(x=325, y=250, width=100)


if __name__ == "__main__":  # lets create the object of that class and call it
    root = Tk()
    app = login(root)
    root.mainloop()
