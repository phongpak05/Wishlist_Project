import customtkinter as ctk

class userBar(ctk.CTkFrame):
    def __init__(self, parent, username="Username"):
        super().__init__(
            parent,
            fg_color="#0A1E4A",
            corner_radius=18,
            height=62
        )

        self.pack_propagate(False)

        ctk.CTkLabel(
            self,
            text="👤",
            font=("Arial", 48),
            text_color="#FFFFFF"
        ).place(relx=0.12, rely=0.45, anchor="center")

        self.username = ctk.CTkLabel(
            self,
            text=username,
            font=("Arial", 22),
            text_color="white"
        )
        self.username.place(x=78, rely=0.5, anchor="w")

    def set_username(self, name):
        self.username.configure(text=name)