import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class pageHistory(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("History")
        self.geometry("390x740")
        self.resizable(False, False)
        self.configure(fg_color="#F2F2F2")

        title_label = ctk.CTkLabel(
            self,
            text="History",
            font=("Arial", 26, "bold"),
            text_color="black"
        )
        title_label.pack(pady=(30, 10))

        user_frame = ctk.CTkFrame(
            self,
            fg_color="#14213D",
            corner_radius=20,
            height=80
        )
        user_frame.pack(padx=30, pady=15, fill="x")
        user_frame.pack_propagate(False)

        profile_circle = ctk.CTkFrame(
            user_frame,
            width=56,
            height=56,
            corner_radius=28,
            fg_color="white"
        )
        profile_circle.pack(side="left", padx=20)
        profile_circle.pack_propagate(False)

        profile_icon = ctk.CTkLabel(
            profile_circle,
            text="👤",
            font=("Arial", 24),
            text_color="#14213D"
        )
        profile_icon.place(relx=0.5, rely=0.5, anchor="center")

        username_label = ctk.CTkLabel(
            user_frame,
            text="Username",
            font=("Arial", 19, "bold"),
            text_color="white"
        )
        username_label.pack(side="left")

        self.create_history_card("iphone", 100)
        self.create_history_card("ipad", 100)
        self.create_history_card("airpod", 100)

    def create_history_card(self, name, percent):

        card = ctk.CTkFrame(
            self,
            fg_color="#E6E6E6",
            corner_radius=20,
            height=90
        )
        card.pack(padx=30, pady=12, fill="x")
        card.pack_propagate(False)

        icon_box = ctk.CTkFrame(
            card,
            width=45,
            height=45,
            fg_color="#1B7F2A",
            corner_radius=10
        )
        icon_box.pack(side="left", padx=15)
        icon_box.pack_propagate(False)

        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(side="left", fill="both", expand=True, pady=15)

        top_row = ctk.CTkFrame(content, fg_color="transparent")
        top_row.pack(fill="x")

        name_label = ctk.CTkLabel(
            top_row,
            text=name,
            font=("Arial", 15, "bold"),
            text_color="black"
        )
        name_label.pack(side="left")

        arrow_label = ctk.CTkLabel(
            top_row,
            text=">",
            font=("Arial", 14),
            text_color="black"
        )
        arrow_label.pack(side="right")

        percent_label = ctk.CTkLabel(
            top_row,
            text=f"{percent}%",
            font=("Arial", 13),
            text_color="black"
        )
        percent_label.pack(side="right", padx=(0,5))

        progress = ctk.CTkProgressBar(
            content,
            height=10,
            corner_radius=10,
            progress_color="#1B7F2A"
        )
        progress.pack(fill="x", pady=(10, 0))
        progress.set(percent / 100)

if __name__ == "__main__":
    app = pageHistory()
    app.mainloop()