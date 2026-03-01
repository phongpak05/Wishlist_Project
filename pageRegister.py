import customtkinter as ctk

class pageRegister(ctk.CTkFrame):
    def __init__(self,parent,showPage):
        super().__init__(parent , fg_color="#000F36")

        titleFont = ("fc motorway",45,"bold")
        buttonFont = ("coda",26)
        normalFont = ("coda",18)

        header = ctk.CTkFrame(self,fg_color="transparent",height=200)
        header.pack(fill="x")
        header.pack_propagate(False)


        ctk.CTkLabel(header,
                     text="Register",
                     font = ("Arial", 42, "bold"),
                     text_color="white"
                     ).place(relx=0.5,rely=0.65,anchor="center")
        ctk.CTkButton(header,
                     text="<",
                     width=35,
                     font = ("fc mootorway",32,"bold"),
                     text_color="white",
                     fg_color="transparent",
                     command=lambda:showPage("welcome"),
                     hover_color="#000F36"
                     ).place(x=15,y=25)
        ctk.CTkEntry(self,
                     width=270,
                     height=30,
                     fg_color="white",
                     border_color="white",
                     text_color= "#000000"
                     ).pack(pady=20)
        ctk.CTkEntry(self,
                     width=270,
                     height=30,
                     fg_color="white",
                     border_color="white",
                     text_color= "#000000"
                     ).pack(pady=20)
        ctk.CTkEntry(self,
                     width=270,
                     height=30,
                     fg_color="white",
                     border_color="white",
                     text_color= "#000000"
                     ).pack(pady=20)
        ctk.CTkEntry(self,
                     width=270,
                     height=30,
                     fg_color="white",
                     border_color="white",
                     text_color= "#000000"
                     ).pack(pady=20)
        ctk.CTkLabel(self,
                     text="Email",
                     font = normalFont,
                     text_color="white"
                     ).place(relx=0.22,rely=0.275,anchor="center")
        ctk.CTkLabel(self,
                     text="Username",
                     font = normalFont,
                     text_color="white"
                     ).place(relx=0.27,rely=0.372,anchor="center")
        ctk.CTkLabel(self,
                     text="Password",
                     font = normalFont,
                     text_color="white",
                     fg_color="transparent"
                     ).place(relx=0.27,rely=0.468,anchor="center")
        ctk.CTkLabel(self,
                     text="Confirm",
                     font = normalFont,
                     text_color="white"
                     ).place(relx=0.245,rely=0.561,anchor="center")
        ctk.CTkButton(self,
                      text="Done",
                      font=buttonFont,
                      fg_color="white",
                      hover_color="white",
                      command=lambda:showPage("login"),
                      text_color="black"                      
                      ).place(relx=0.5,rely=0.7,anchor="center")
                     
        
if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Welcome to my Program")
    root.geometry("390x740+200+80")
    root.resizable(False,False)

    page = pageRegister(root)
    page.pack(fill="both", expand=True)

    root.mainloop()