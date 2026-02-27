import customtkinter as ctk
from menu import create_bottom_nav
from userBar import userBar

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class pageSetting(ctk.CTkFrame):
    def __init__(self, master, showPage, controller):
        super().__init__(master, fg_color="#F5F5F5")

        self.controller = controller
        self.showPage = showPage

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = ctk.CTkFrame(self, height=160, corner_radius=0, fg_color="#F5F5F5")
        header.grid(row=0, column=0, sticky="ew")
        header.grid_propagate(False)

        title = ctk.CTkLabel(
            header,
            text="SETTING",  
            font=("fc motorway", 58, "bold"),
            text_color="black"
        )
        title.pack(pady=(16, 10))

        self.user_bar = userBar(header, "Username")
        self.user_bar.pack(padx=20, pady=(0, 10), fill="x")

        content = ctk.CTkFrame(self, fg_color="transparent")
        content.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

        logout_button = ctk.CTkButton(
            content,
            text="Log Out",
            width=160,
            height=44,
            corner_radius=12,
            fg_color="#6E0E0A",
            hover_color="#8B0000",
            text_color="white"
        )
        logout_button.pack(pady=40)

        footer = ctk.CTkFrame(
            self,
            height=80,
            corner_radius=0,
            fg_color="#0A1E4A"
        )
        footer.grid(row=2, column=0, sticky="ew")
        footer.grid_propagate(False)

        create_bottom_nav(footer, self.showPage)