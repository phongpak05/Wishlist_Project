import customtkinter as ctk
<<<<<<< HEAD
=======
from menu import create_bottom_nav
from userBar import userBar
from components import planCard
>>>>>>> 939e1c34bfce591eef17abec4e2222a94e2232ca

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

<<<<<<< HEAD

class pageHistory(ctk.CTkFrame):
    def __init__(self, master, showPage, controller):
        super().__init__(master, fg_color="#F5F5F5")

        self.showPage = showPage
        self.controller = controller

        self.pack(fill="both", expand=True)

        content = ctk.CTkFrame(self, fg_color="transparent")
        content.pack(fill="both", expand=True)
=======

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
>>>>>>> 939e1c34bfce591eef17abec4e2222a94e2232ca

        title_label = ctk.CTkLabel(
            header,
            text="HISTORY",
            font=("Arial", 42, "bold"),
            text_color="black"
        )
<<<<<<< HEAD
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
=======
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

>>>>>>> 939e1c34bfce591eef17abec4e2222a94e2232ca

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

<<<<<<< HEAD
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
=======
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
>>>>>>> 939e1c34bfce591eef17abec4e2222a94e2232ca
