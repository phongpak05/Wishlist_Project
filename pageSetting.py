import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class SettingPage(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Setting")
        self.geometry("390x740")
        self.resizable(False, False)
        self.configure(fg_color="#F2F2F2")

        title_label = ctk.CTkLabel(
            self,
            text="Setting",
            font=("Arial", 26, "bold"),
            text_color="black"
        )
        title_label.pack(pady=(30, 20))

        user_frame = ctk.CTkFrame(
            self,
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
            text="Username",
            font=("Arial", 18, "bold"),
            text_color="white"
        )
        username_label.pack(side="left")

        logout_button = ctk.CTkButton(
            self,
            text="Log Out",
            font=("Arial", 16, "bold"),
            width=160,
            height=45,
            corner_radius=15,
            fg_color="#6E0E0A",
            hover_color="#8B0000"
        )
        logout_button.pack(pady=(400, 120))

if __name__ == "__main__":
    app = SettingPage()
    app.mainloop()