import customtkinter as ctk
from pageWelcome import pageWelcome
from pageLogin import pageLogin
from pageRegister import pageRegister
from pageHome import pageHome
from pageNewplan import pageNewplan
from components import planCard
from pageStatement import pageStatement
from pageHistory import pageHistory
from pageSetting import pageSetting
from pageDetails import pageDetails

class app(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("390x740+150+50")
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
        self.pages["statement"] = pageStatement(self, self.showPage, self)
        self.pages["history"] = pageHistory(self, self.showPage, self)
        self.pages["setting"] = pageSetting(self, self.showPage, self)
        self.pages["detail"] = pageDetails(self, self.showPage, self)

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