import customtkinter as ctk
from menu import create_bottom_nav

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class pageStatement(ctk.CTkFrame):
    def __init__(self, master, showPage, controller):
        super().__init__(master, fg_color="#F5F5F5")
        self.showPage = showPage
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)   # content
        self.grid_rowconfigure(1, weight=0)   # footer
        self.grid_columnconfigure(0, weight=1)

        title_font = ("Motorway", 28, "bold")
        card_big_font = ("Arial", 16, "bold")
        card_small_font = ("Arial", 11)

        content = ctk.CTkFrame(self, 
                               fg_color="transparent")
        content.grid(row=0, column=0, sticky="nsew")
        content.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(content, 
                                   text="Statement", font=title_font)
        title_label.pack(pady=50)

        top_frame = ctk.CTkFrame(content, fg_color="transparent")
        top_frame.pack(pady=20)

        income_frame = ctk.CTkFrame(top_frame, 
                                    width=160, 
                                    height=130, fg_color="#0A1E4A", corner_radius=20)
        income_frame.pack(side="left", padx=10)
        income_frame.pack_propagate(False)

        income_amount = ctk.CTkLabel(income_frame, 
                                     text="X,XXX", font=card_big_font, text_color="white")
        income_amount.pack(pady=(10, 0), anchor="w", padx=15)

        income_label = ctk.CTkLabel(income_frame, text="Total Income", font=card_small_font, text_color="white")
        income_label.pack(anchor="w", padx=15)

        edit_income_btn = ctk.CTkButton(
            income_frame, 
            text="📝", 
            width=25, 
            height=25,
            fg_color="transparent", 
            hover=False, 
            text_color="white", 
            font=("Arial", 12)
        )
        edit_income_btn.place(relx=1.0, rely=1.0, x=-8, y=-8, anchor="se")

        def press_income(e): edit_income_btn.place_configure(x=-8, y=-6)
        def release_income(e): edit_income_btn.place_configure(x=-8, y=-8)
        edit_income_btn.bind("<ButtonPress-1>", press_income)
        edit_income_btn.bind("<ButtonRelease-1>", release_income)

        expense_frame = ctk.CTkFrame(top_frame, 
                                     width=160, 
                                     height=130, fg_color="#cfcfcf", corner_radius=20)
        expense_frame.pack(side="left", padx=10)
        expense_frame.pack_propagate(False)

        expense_amount = ctk.CTkLabel(expense_frame, 
                                      text="X,XXX", font=card_big_font, text_color="black")
        expense_amount.pack(pady=(10, 0), anchor="w", padx=15)

        expense_label = ctk.CTkLabel(expense_frame, 
                                     text="Total Expense", font=card_small_font, text_color="black")
        expense_label.pack(anchor="w", padx=15)

        edit_expense_btn = ctk.CTkButton(
            expense_frame, 
            text="📝", 
            width=25, 
            height=25,
            fg_color="transparent", 
            hover=False, 
            text_color="black", 
            font=("Arial", 12)
        )
        edit_expense_btn.place(relx=1.0, rely=1.0, x=-8, y=-8, anchor="se")

        def press_expense(e): edit_expense_btn.place_configure(x=-8, y=-6)
        def release_expense(e): edit_expense_btn.place_configure(x=-8, y=-8)
        edit_expense_btn.bind("<ButtonPress-1>", press_expense)
        edit_expense_btn.bind("<ButtonRelease-1>", release_expense)

        balance_frame = ctk.CTkFrame(content, 
                                     width=330, 
                                     height=120, fg_color="#cfcfcf", corner_radius=20)
        balance_frame.pack(pady=20)
        balance_frame.pack_propagate(False)

        balance_amount = ctk.CTkLabel(balance_frame, 
                                      text="X,XXX", font=card_big_font, text_color="black")
        balance_amount.pack(pady=(20, 0))

        balance_label = ctk.CTkLabel(balance_frame, 
                                     text="Balance", font=card_small_font, text_color="black")
        balance_label.pack()


        footer = ctk.CTkFrame(self, 
                              height=80, 
                              corner_radius=0, fg_color="#0A1E4A")
        footer.grid(row=1, column=0, sticky="ew")
        footer.grid_propagate(False)

        create_bottom_nav(footer, self.showPage)