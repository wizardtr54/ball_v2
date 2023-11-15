import ursina
import customtkinter as Ctk



def button_event():
    print("button pressed")

button = Ctk.CTkButton(text="CTkButton", command=button_event)
