import customtkinter as ctk
from menu import create_bottom_nav

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class pageSetting(ctk.CTkFrame):
    def __init__(self, master, showPage, controller):
        super().__init__(master, fg_color="#F5F5F5")
        self.showPage = showPage
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)   # content
        self.grid_rowconfigure(1, weight=0)   # footer
        self.grid_columnconfigure(0, weight=1)

        content = ctk.CTkFrame(self, fg_color="transparent")
        content.grid(row=0, column=0, sticky="nsew")
        content.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(
            content,
            text="Setting",
            font=("Arial", 26, "bold"),
            text_color="black"
        )
        title_label.pack(pady=(30, 20))

        user_frame = ctk.CTkFrame(
            content,
            fg_color="#14213D",
            corner_radius=20,
            height=70
        )
        user_frame.pack(padx=30, pady=10, fill="x")
        user_frame.pack_propagate(False)

        profile_circle = ctk.CTkFrame(
            user_frame,
            width=50,
            height=50,
            corner_radius=25,
            fg_color="white"
        )
        profile_circle.pack(side="left", padx=20)
        profile_circle.pack_propagate(False)

        profile_icon = ctk.CTkLabel(
            profile_circle,
            text="👤",
            font=("Arial", 22),
            text_color="#14213D"
        )
        profile_icon.place(relx=0.5, rely=0.5, anchor="center")

        username_label = ctk.CTkLabel(
            user_frame,
            text=getattr(self.controller, "current_username", "Username"),
            font=("Arial", 18, "bold"),
            text_color="white"
        )
        username_label.pack(side="left")

        
        spacer = ctk.CTkFrame(content, fg_color="transparent")
        spacer.pack(fill="both", expand=True)

        logout_button = ctk.CTkButton(
            content,
            text="Log Out",
            font=("Arial", 16, "bold"),
            width=160,
            height=45,
            corner_radius=15,
            fg_color="#6E0E0A",
            hover=False
        )
        logout_button.pack(pady=(0, 30))

        # ===== footer =====
        footer = ctk.CTkFrame(self, height=80, corner_radius=0, fg_color="#0A1E4A")
        footer.grid(row=1, column=0, sticky="ew")
        footer.grid_propagate(False)

        create_bottom_nav(footer, self.showPage)


if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("390x740+00+30")
    root.resizable(False, False)

    def dummy_showPage(name):
        print("go to:", name)

    dummy_controller = type("C", (), {"current_username": "Username"})()

    page = pageSetting(root, dummy_showPage, dummy_controller)
    page.pack(fill="both", expand=True)

    root.mainloop()