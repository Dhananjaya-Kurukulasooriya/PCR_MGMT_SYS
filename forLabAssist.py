from tkinter import *  # for the GUI components
import tkinter.messagebox  # to notify the user about warning and others
import pymysql  # to establish connection to MySQL database
from PIL import ImageTk, Image


class forLabAssist():
    def __init__(self, root4):
        self.root4 = root4

    def __init__(self, root4):
        self.root4 = root4
        self.root4.title("forPatient")  # set the title bar name
        # set the size of the loginpage and put the X and Y cordinates for top left corner
        self.root4.geometry("1000x600+400+200")
        self.root4.iconbitmap("images/icon1.ico")  # set the icon for title bar
        # =====background image================
        
        self.root4.resizable(False, False)  # to avoid the maximize option

    # =========main title label=================================
        title = Label(self.root4, text="For Lab Assistants", font=(
            "Impact", 30, "bold"), fg="#03506f", anchor=CENTER, bg='#ffffff')
        title.pack(side=TOP, pady=20, padx=10)

if __name__ == '__main__':
    
    root4=Tk()
    app4=forLabAssist(root4)
    root4.mainloop()