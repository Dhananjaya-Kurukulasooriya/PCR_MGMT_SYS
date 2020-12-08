from tkinter import *  # for the GUI components
import tkinter.messagebox  # to notify the user about warning and others
import pymysql  # to establish connection to MySQL database
from PIL import ImageTk, Image


class forPatient():

    def __init__(self, root2):
        self.root2 = root2
        self.root2.title("forPatient")  # set the title bar name
        # set the size of the loginpage and put the X and Y cordinates for top left corner
        self.root2.geometry("1000x600+400+200")
        self.root2.iconbitmap("images/icon1.ico")  # set the icon for title bar
        # =====background image================
        
        self.root2.resizable(False, False)  # to avoid the maximize option

    # =========main title label=================================
        title = Label(self.root2, text="For patients", font=(
            "Impact", 30, "bold"), fg="#03506f", anchor=CENTER, bg='#ffffff')
        title.pack(side=TOP, pady=20, padx=10)

if __name__ == '__main__':
    
    root2=Tk()
    app2=forPatient(root2)
    root2.mainloop()