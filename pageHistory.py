import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class pageHistory(ctk.CTkFrame):
    def __init__(self, master, showPage, controller):
        super().__init__(master, fg_color="#F5F5F5")

        self.showPage = showPage
        self.controller = controller

        self.pack(fill="both", expand=True)

        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="both", expand=True)

        title_label = ctk.CTkLabel(
            content,
            text="History",
            font=("Arial", 26, "bold"),
            text_color="black"
        )
        title_label.pack(pady=(30, 20))

        user_frame = ctk.CTkFrame(
            content,
            fg_color="#0A1E4A",
            corner_radius=18,
            height=62
        )
        user_frame.pack(padx=30, pady=10, fill="x")
        user_frame.pack_propagate(False)

        ctk.CTkLabel(
            user_frame,
            text="👤",
            font=("Arial", 48),
            text_color="#FFFFFF"
        ).place(relx=0.12, rely=0.45, anchor="center")

        username_label = ctk.CTkLabel(
            user_frame,
            text=getattr(self.controller, "current_username", "Username"),
            font=("Arial", 19, "bold"),
            text_color="white"
        )
        username_label.place(relx=0.28, rely=0.5, anchor="w")

        self.create_history_card(content, "iphone", 100)
        self.create_history_card(content, "ipad", 80)
        self.create_history_card(content, "airpod", 60)

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
    root = ctk.CTk()
    root.geometry("390x740")
    root.resizable(False, False)

    def dummy_showPage(name):
        print("Go to:", name)

    dummy_controller = type("C", (), {"current_username": "Username"})()

    page = pageHistory(root, dummy_showPage, dummy_controller)

    root.mainloop()