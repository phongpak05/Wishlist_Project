import customtkinter as ctk
from menu import create_bottom_nav

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class pagePermonth(ctk.CTkFrame):
    def __init__(self, master, showPage, controller):
        super().__init__(master, fg_color="#F5F5F5")
        self.showPage = showPage
        self.controller = controller

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = ctk.CTkFrame(self, height=160, corner_radius=0, fg_color="#F5F5F5")
        header.grid(row=0, column=0, sticky="ew")
        header.grid_propagate(False)

        ctk.CTkButton(
            header,
            text="‹",
            width=36,
            height=36,
            fg_color="transparent",
            hover=False,
            text_color="black",
            font=("Arial", 28, "bold"),
            command=lambda: self.showPage("statement"),
        ).place(x=14, y=18)

        ctk.CTkLabel(
            header,
            text="Edit Percent",
            font=("Arial", 42, "bold"),
            text_color="black"
        ).pack(pady=(18, 10))

        content = ctk.CTkFrame(self, fg_color="transparent")
        content.grid(row=1, column=0, sticky="nsew")

        form_frame = ctk.CTkFrame(content, fg_color="transparent")
        form_frame.pack(pady=20)

        label = ctk.CTkLabel(
            form_frame,
            text="Select Saving %",
            font=("Arial", 12),
            text_color="#444"
        )
        label.pack(anchor="w", padx=5)

        percent_options = [
            "10%", "20%", "30%", "40%", "50%",
            "60%", "70%", "80%", "90%", "100%"
        ]

        self.percent_dropdown = ctk.CTkOptionMenu(
            form_frame,
            values=percent_options,
            width=280,
            text_color= "black",
            fg_color= "white",
            button_color= "#BDBDBD",
            hover=False
        )
        self.percent_dropdown.pack(pady=5)

        save_btn = ctk.CTkButton(
            content,
            text="Save",
            command=self.save,
            font=("Arial", 12, "bold"),
            fg_color="#1E7D22",
            hover_color="#16651A",
            text_color="white",
            width=160,
            height=40
        )
        save_btn.pack(pady=20)

        footer = ctk.CTkFrame(
            self,
            height=80,
            corner_radius=0,
            fg_color="transparent"
        )
        footer.grid(row=2, column=0, sticky="ew")
        footer.grid_propagate(False)

        create_bottom_nav(footer, self.showPage)

    def save(self):

        percent = int(self.percent_dropdown.get().replace("%", ""))
        income = self.controller.income
        expense = self.controller.expense

        if income is None or expense is None:
            balance = 0
        else:
            balance = income - expense

        permonth = int(balance * (percent / 100))
        self.controller.permonth = permonth
        self.showPage("statement")