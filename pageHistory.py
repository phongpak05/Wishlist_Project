import customtkinter as ctk
from menu import create_bottom_nav
from userBar import userBar

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


        content = ctk.CTkFrame(self, fg_color="transparent")
        content.grid(row=1, column=0, sticky="nsew")

        self.create_history_card(content, "iphone", 100)
        self.create_history_card(content, "ipad", 100)
        self.create_history_card(content, "airpod", 100)

        footer = ctk.CTkFrame(
            self,
            height=80,
            corner_radius=0,
            fg_color="#0A1E4A"
        )
        footer.grid(row=2, column=0, sticky="ew")
        footer.grid_propagate(False)

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