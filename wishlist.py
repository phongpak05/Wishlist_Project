import customtkinter as ctk
from pageWelcome import pageWelcome
from pageLogin import pageLogin
from pageRegister import pageRegister

class app(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("390x740")
        self.resizable(False,False)
        self.title("WISHLIST")

        self.pages = {}

        self.pages["welcome"] = pageWelcome(self,self.showPage)
        self.pages["login"] = pageLogin(self,self.showPage)
        self.pages["register"] = pageRegister(self,self.showPage)

        for page in self.pages.values():
            page.place(x=0,y=0,relwidth=1,relheight=1)

        self.showPage("welcome")

    def showPage(self,name):
        self.pages[name].tkraise()

if __name__ == "__main__":
    app = app()
    app.mainloop()