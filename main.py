import tkinter as tk,sys
import customtkinter as Ctk
from tkinter import *

root = Ctk.CTk()
resolution="500x500"
root.geometry(resolution)
root.title("GOD DAMNIT")
BackgroundMainMenu=PhotoImage(file = "assets/ball2.png")

label1 = Label( root, image = BackgroundMainMenu) 
label1.place(x = 0, y = 0) 
  
label2 = Label( root, text = "Welcome") 
label2.pack(pady = 50) 
# all the calls
def button_exit():
    sys.exit(0)

def play():
    import root

# Create Frame 

frame1 = Frame(root) 
frame1.pack() 

# Add buttons 
button1 = Ctk.CTkButton(frame1,text="Exit",command=button_exit) 
button1.pack() 

button2 = Ctk.CTkButton(frame1, text = "Start") 
button2.pack() 
  
button3 = Ctk.CTkButton( frame1, text = "Reset") 
button3.pack()

root.mainloop()