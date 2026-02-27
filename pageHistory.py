import customtkinter as ctk
from menu import create_bottom_nav

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class pageHistory(ctk.CTkFrame):

    def __init__(self, parent, showPage, app):
        super().__init__(parent)

        self.showPage = showPage
        self.app = app

        self.configure(fg_color="#F2F2F2")

        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="both", expand=True)

        title_label = ctk.CTkLabel(
            content,
            text="History",
            font=("Arial", 26, "bold"),
            text_color="black"
        )
        title_label.pack(pady=(30, 10))

        user_frame = ctk.CTkFrame(
            content,
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

        self.create_history_card(content, "iphone", 100)
        self.create_history_card(content, "ipad", 100)
        self.create_history_card(content, "airpod", 100)

        footer = ctk.CTkFrame(
            self,
            height=80,
            corner_radius=0,
            fg_color="#0A1E4A"
        )
        footer.pack(side="bottom", fill="x")

        create_bottom_nav(footer, self.showPage)

    def create_history_card(self, parent, name, percent):

        card = ctk.CTkFrame(
            parent,
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

        percent_label = ctk.CTkLabel(
            top_row,
            text=f"{percent}%",
            font=("Arial", 13),
            text_color="black"
        )
        percent_label.pack(side="right", padx=(0, 5))

        arrow_label = ctk.CTkLabel(
            top_row,
            text=">",
            font=("Arial", 14),
            text_color="black"
        )
        arrow_label.pack(side="right")

        progress = ctk.CTkProgressBar(
            content,
            height=10,
            corner_radius=10,
            progress_color="#1B7F2A"
        )
        progress.pack(fill="x", pady=(10, 0))
        progress.set(percent / 100)


if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("390x740")

    page = pageHistory(app, None, None)
    page.pack(fill="both", expand=True)

    app.mainloop()