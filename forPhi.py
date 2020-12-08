from tkinter import *  # for the GUI components
import tkinter.messagebox  # to notify the user about warning and others
import pymysql  # to establish connection to MySQL database
from PIL import ImageTk, Image


class forPhi():
    def __init__(self, root3):
        self.root3 = root3
        self.root3.title("forPHI")  # set the title bar name
        # set the size of the loginpage and put the X and Y cordinates for top left corner
        self.root3.geometry("1000x600+400+200")
        self.root3.iconbitmap("images/icon1.ico")  # set the icon for title bar
        # =====background image================
        
        self.root3.resizable(False, False)  # to avoid the maximize option

    # =========main title label=================================
        title = Label(self.root3, text="For PHI", font=(
            "Impact", 30, "bold"), fg="#03506f", anchor=CENTER, bg='#ffffff')
        title.pack(side=TOP, pady=20, padx=10)

if __name__ == '__main__':
    
    root3=Tk()
    app3=forPhi(root3)
    root3.mainloop()