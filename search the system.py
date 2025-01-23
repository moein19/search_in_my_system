import os
import customtkinter
import subprocess
from tkinter.messagebox import *
import pyttsx3

class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
        self.title("Search the System")

        pyttsx3.speak("little q is shotrcut for exit the program")
        
        self.entry = customtkinter.CTkEntry(self,placeholder_text="Enter your name of file for return the its address : ",width=350)
        
        self.entry2 = customtkinter.CTkEntry(self,placeholder_text="please enter drive : ")
        self.entry2.pack(pady=10)
        self.entry.pack(pady=15)

        self.entry2.bind("<FocusOut>",command=self.chtext)

        self.btn = customtkinter.CTkButton(self,command=self.get_address,text="Search the Drive ",fg_color="Red",hover_color="Blue",text_color="Black")
        self.btn.pack(pady=20)

        self.combo = customtkinter.CTkComboBox(self,command=self.go_expe,width=300,values=["Search the your drive"])
        self.combo.pack(pady=25)

        self.bind("<Key>",func=self.q)

    def go_expe(self,ch):
        customtkinter.filedialog.Open

    def q(self,ch):
        if ch.keysym == "q":
            self.destroy()

    def chtext(self,text):
        self.btn.configure(text=f"Search the Drive {self.entry2.get()}")

    def get_address(self):
        l = []
        for root,dire,file in os.walk(self.entry2.get()+":"):
            if self.entry.get() in file:
                l.append(root)
        self.combo.configure(values=l)
        showinfo("OK",f"path of file {self.entry.get()} added to list")

if __name__ == "__main__":
    window = Window()
    window.mainloop()