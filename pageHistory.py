import customtkinter as ctk
from menu import create_bottom_nav
from userBar import userBar
from components import planCard

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class pageHistory(ctk.CTkFrame):
    def __init__(self, parent, showPage, app):
        super().__init__(parent)
        self.showPage = showPage
        self.app = app

        self.configure(fg_color="#F5F5F5")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = ctk.CTkFrame(self, height=160, corner_radius=0, fg_color="#F5F5F5")
        header.grid(row=0, column=0, sticky="ew")
        header.grid_propagate(False)

        title_label = ctk.CTkLabel(
            header,
            text="HISTORY",
            font=("Arial", 42, "bold"),
            text_color="black"
        )
        title_label.pack(pady=(16, 10))

        self.user_bar = userBar(header, "Username")
        self.user_bar.pack(padx=20, pady=(0, 10), fill="x")


        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.grid(row=1, column=0, sticky="nsew")

        footer = ctk.CTkFrame(
            self,
            height=80,
            corner_radius=0,
            fg_color="#0A1E4A"
        )
        footer.grid(row=2, column=0, sticky="ew")
        footer.grid_propagate(False)

        create_bottom_nav(footer, self.showPage)


    def refresh(self):
        for widget in self.content.winfo_children():
            widget.destroy()

        history = self.app.history

        if not history:
            ctk.CTkLabel(
                self.content,
                text="No completed plans",
                font=("Arial", 16)
            ).pack(pady=40)
            return

        for plan in history:

            card = planCard(
                self.content,
                name=plan["name"],
                percent=1,
                bar_color="#1B7F2A",
                command=lambda p=plan: self.open_detail(p)
            )

            card.pack(padx=30, pady=12, fill="x")


    def open_detail(self, plan):
        self.app.current_plan = plan
        self.showPage("detailhome")