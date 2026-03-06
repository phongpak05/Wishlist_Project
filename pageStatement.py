import customtkinter as ctk
from menu import create_bottom_nav
from userBar import userBar
from tkinter import messagebox

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class pageStatement(ctk.CTkFrame):
    def __init__(self, master, showPage, controller):
        super().__init__(master, fg_color="#F5F5F5")
        self.showPage = showPage
        self.controller = controller

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = ctk.CTkFrame(self, height=160, corner_radius=0, fg_color="#F5F5F5")
        header.grid(row=0, column=0, sticky="ew")
        header.grid_propagate(False)

        ctk.CTkLabel(
            header,
            text="STATEMENT",
            font=("Arial", 42, "bold"),
            text_color="black"
        ).pack(pady=(16, 10))

        content = ctk.CTkFrame(self, fg_color="transparent")
        content.grid(row=1, column=0, sticky="nsew")

        title_font = ("Motorway", 28, "bold")
        card_big_font = ("Arial", 16, "bold")
        card_small_font = ("Arial", 11)

        top_frame = ctk.CTkFrame(content, fg_color="transparent")
        top_frame.pack(pady=20)

        income_frame = ctk.CTkFrame(
            top_frame,
            width=160,
            height=130,
            fg_color="#0A1E4A",
            corner_radius=20
        )
        income_frame.pack(side="left", padx=10)
        income_frame.pack_propagate(False)

        self.income_amount = ctk.CTkLabel(
            income_frame,
            text="0",
            font=card_big_font,
            text_color="white"
        )
        self.income_amount.pack(pady=(10, 0), anchor="w", padx=15)

        income_label = ctk.CTkLabel(
            income_frame,
            text="Total Income",
            font=card_small_font,
            text_color="white"
        )
        income_label.pack(anchor="w", padx=15)

        edit_income_btn = ctk.CTkButton(
            income_frame,
            text="📝",
            width=25,
            height=25,
            fg_color="transparent",
            hover=False,
            text_color="white",
            command=lambda: showPage("editincome")
        )
        edit_income_btn.place(relx=1.0, rely=1.0, x=-8, y=-8, anchor="se")

        expense_frame = ctk.CTkFrame(
            top_frame,
            width=160,
            height=130,
            fg_color="#cfcfcf",
            corner_radius=20
        )
        expense_frame.pack(side="left", padx=10)
        expense_frame.pack_propagate(False)

        self.expense_amount = ctk.CTkLabel(
            expense_frame,
            text="0",
            font=card_big_font,
            text_color="black"
        )
        self.expense_amount.pack(pady=(10, 0), anchor="w", padx=15)

        expense_label = ctk.CTkLabel(
            expense_frame,
            text="Total Expense",
            font=card_small_font,
            text_color="black"
        )
        expense_label.pack(anchor="w", padx=15)

        edit_expense_btn = ctk.CTkButton(
            expense_frame,
            text="📝",
            width=25,
            height=25,
            fg_color="transparent",
            hover=False,
            text_color="black",
            command=lambda: showPage("editexpense")
        )
        edit_expense_btn.place(relx=1.0, rely=1.0, x=-8, y=-8, anchor="se")

        bottom_frame = ctk.CTkFrame(content, fg_color="transparent")
        bottom_frame.pack(pady=10)

        balance_frame = ctk.CTkFrame(
            bottom_frame,
            width=160,
            height=130,
            fg_color="#cfcfcf",
            corner_radius=20
        )
        balance_frame.pack(side="left", padx=10)
        balance_frame.pack_propagate(False)

        self.balance_amount = ctk.CTkLabel(
            balance_frame,
            text="0",
            font=card_big_font,
            text_color="black"
        )
        self.balance_amount.pack(pady=(10, 0), anchor="w", padx=15)

        balance_label = ctk.CTkLabel(
            balance_frame,
            text="Balance",
            font=card_small_font,
            text_color="black"
        )
        balance_label.pack(anchor="w", padx=15)

        month_frame = ctk.CTkFrame(
            bottom_frame,
            width=160,
            height=130,
            fg_color="#cfcfcf",
            corner_radius=20
        )
        month_frame.pack(side="left", padx=10)
        month_frame.pack_propagate(False)

        self.month_amount = ctk.CTkLabel(
            month_frame,
            text="0",
            font=card_big_font,
            text_color="black"
        )
        self.month_amount.pack(pady=(10, 0), anchor="w", padx=15)

        month_label = ctk.CTkLabel(
            month_frame,
            text="Per month",
            font=card_small_font,
            text_color="black"
        )
        month_label.pack(anchor="w", padx=15)

        edit_month_amount_btn = ctk.CTkButton(
            month_frame,
            text="📝",
            width=25,
            height=25,
            fg_color="transparent",
            hover=False,
            text_color="black",
            command=lambda: showPage("editpermonth")
        )
        edit_month_amount_btn.place(relx=1.0, rely=1.0, x=-8, y=-8, anchor="se")

        footer = ctk.CTkFrame(
            self,
            height=80,
            corner_radius=0,
            fg_color="#0A1E4A"
        )
        footer.grid(row=2, column=0, sticky="ew")
        footer.grid_propagate(False)

        create_bottom_nav(footer, self.showPage)

    def refresh(self):

        income = self.controller.income
        expense = self.controller.expense
        permonth = self.controller.permonth

        if income is None:
            income = 0

        if expense is None:
            expense = 0

        balance = income - expense

        if balance < 0:
            messagebox.showwarning(
                "ข้อมูลไม่ถูกต้อง",
                "Expense ต้องไม่มากกว่า Income"
            )
            self.controller.expense = income
            balance = 0

        self.income_amount.configure(text=f"{income:,}")
        self.expense_amount.configure(text=f"{expense:,}")
        self.balance_amount.configure(text=f"{balance:,}")

        if permonth:
            self.month_amount.configure(text=f"{permonth:,}")
        else:
            self.month_amount.configure(text="0")