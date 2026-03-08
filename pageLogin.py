import customtkinter as ctk

class pageLogin(ctk.CTkFrame):
    def __init__(self,parent,showPage):
        super().__init__(parent , fg_color="#000F36")

        self.showPage = showPage

        titleFont = ("fc motorway",45,"bold")
        buttonFont = ("coda",26)
        normalFont = ("coda",18)

        header = ctk.CTkFrame(self,fg_color="transparent",height=200)
        header.pack(fill="x")
        header.pack_propagate(False)

        content = ctk.CTkFrame(self,fg_color="transparent")
        content.pack(fill="both",expand=True)

        ctk.CTkLabel(header,
                     text="Login",
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

        # ENTRY USERNAME
        self.username_entry = ctk.CTkEntry(content,
                     width=270,
                     height=30,
                     fg_color="white",
                     border_color="white",
                     text_color= "#000000"
                     )
        self.username_entry.place(relx=0.5,rely=0.1,anchor="center")

        # ENTRY PASSWORD
        self.password_entry = ctk.CTkEntry(content,
                     width=270,
                     height=30,
                     fg_color="white",
                     border_color="white",
                     text_color= "#000000",
                     show="*"
                     )
        self.password_entry.place(relx=0.5,rely=0.25,anchor="center")

        # LOGIN BUTTON
        ctk.CTkButton(content,
                      text="Done",
                      font=buttonFont,
                      fg_color="white",
                      hover_color="white",
                      command=self.check_login,
                      text_color="black"
                      ).place(relx=0.5,rely=0.42,anchor="center")

        ctk.CTkLabel(content,
                     text="Username",
                     font = normalFont,
                     text_color="white"
                     ).place(relx=0.27,rely=0.04,anchor="center")

        ctk.CTkLabel(content,
                     text="Password",
                     font = normalFont,
                     text_color="white",
                     fg_color="transparent"
                     ).place(relx=0.27,rely=0.19,anchor="center")

        # ERROR MESSAGE
        self.error_label = ctk.CTkLabel(content,
                                        text="",
                                        text_color="red",
                                        font=("Arial",14))
        self.error_label.place(relx=0.5,rely=0.52,anchor="center")

    # LOGIN CHECK
    def check_login(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        correct_user = "admin"
        correct_pass = "1234"

        if username == correct_user and password == correct_pass:
            self.error_label.configure(text="")
            self.showPage("home")
        else:
            self.error_label.configure(text="Username หรือ Password ไม่ถูกต้อง")


if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Welcome to my Program")
    root.geometry("390x740+200+80")
    root.resizable(False,False)

    # test function
    def showPage(name):
        print("Go to page:", name)

    page = pageLogin(root,showPage)
    page.pack(fill="both", expand=True)

    root.mainloop()