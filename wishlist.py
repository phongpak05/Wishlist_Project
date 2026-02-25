import customtkinter as ctk
from pageWelcome import pageWelcome
from pageLogin import pageLogin
from pageRegister import pageRegister
from pageHome import pageHome
from pageNewplan import pageNewplan
from components import planCard

class app(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("390x740+00+30")
        self.resizable(False, False)
        self.title("WISHLIST")

        self.current_username = "Username"
        self.plans = []

        self.pages = {}
        self.pages["welcome"] = pageWelcome(self, self.showPage)
        self.pages["login"] = pageLogin(self, self.showPage)
        self.pages["register"] = pageRegister(self, self.showPage)

        self.pages["home"] = pageHome(self, self.showPage, self)
        self.pages["newplan"] = pageNewplan(self, self.showPage, self)

        for page in self.pages.values():
            page.place(x=0, y=0, relwidth=1, relheight=1)

        self.showPage("welcome")

    def showPage(self, name):
        page = self.pages[name]
        page.tkraise()

        if name == "home" and hasattr(page, "refresh"):
            page.refresh()

if __name__ == "__main__":
    app = app()
    app.mainloop()