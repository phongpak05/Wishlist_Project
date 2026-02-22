import customtkinter as ctk

class pageWelcome(ctk.CTkFrame):
    def __init__(self, parent,showPage):
        super().__init__(parent, fg_color="#000F36")

        welcomeFont = ("fc motorway",75,"bold")
        buttonFont = ("coda",26)

        frame = ctk.CTkFrame(self,fg_color="#000F36")
        frame.place(relx=0.5, rely=0.35, anchor = "center")

        ctk.CTkLabel(frame, 
                     text="WISH", 
                     font=welcomeFont, 
                     text_color="#2EC7AD").pack(side="left")
        
        ctk.CTkLabel(frame, 
                     text="LIST", 
                     font=welcomeFont, 
                     text_color="white").pack(side="left")

        ctk.CTkButton(self, 
                      text="Login", 
                      width=150, 
                      height= 40,
                      font=buttonFont,
                      fg_color="white",
                      hover_color="white",
                      command=lambda:showPage("login"),
                      text_color="black").place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkButton(self, 
                      text="Register", 
                      width=150,
                      height=40, 
                      font=buttonFont,
                      fg_color="white",
                      hover_color="white",
                       command=lambda:showPage("register"),
                      text_color="black").place(relx=0.5, rely=0.58, anchor="center")

if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Welcome to my Program")
    root.geometry("390x740")
    root.resizable(False,False)

    page = pageWelcome(root)
    page.pack(fill="both", expand=True)

    root.mainloop()