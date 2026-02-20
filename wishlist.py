import tkinter as tk

root = tk.Tk()

root.title("Wishlist")
root.configure(background="#000F36")
root.geometry("390x740+1080+20")
root.resizable(False,False)

title_font = ("Segoe UI", 26, "bold")
card_big_font = ("Helvetica", 16, "bold")
card_small_font = ("Helvetica", 10)


def showPage(page):
    page.tkraise()

page1 = tk.Frame(root, bg="#000F36")
pageLogin = tk.Frame(root, bg="#000F36")
pageRegister = tk.Frame(root, bg="#000F36")
pageHome = tk.Frame(root, bg="#d9d9d9")
pageStatement = tk.Frame(root, bg="#d9d9d9")
pageHistory = tk.Frame(root, bg="#d9d9d9")
pageSetting = tk.Frame(root, bg="#d9d9d9")


for p in (page1, pageLogin, pageRegister , pageStatement,pageHome,pageHistory,pageSetting):
    p.place(x=0, y=0, relwidth=1, relheight=1)

def create_bottom_nav(parent):
    bottom_nav = tk.Frame(parent, height=70, bg="#000033")
    bottom_nav.pack(side="bottom", fill="x")
    bottom_nav.pack_propagate(False)

    button_style = {
        "bg": "#000033",
        "fg": "white",
        "activebackground": "#000033",   # ตอนกด ไม่เปลี่ยนสี
        "activeforeground": "white",
        "border": 0,
        "highlightthickness": 0,
        "font": ("Segoe UI", 16),
        "relief": "flat",
        "bd": 0
    }

    btn_home = tk.Button(bottom_nav, text="🏠", **button_style)
    btn_home.pack(side="left", expand=True, fill="both")

    btn_chart = tk.Button(bottom_nav, text="📊", **button_style)
    btn_chart.pack(side="left", expand=True, fill="both")

    btn_history = tk.Button(bottom_nav, text="🕒", **button_style)
    btn_history.pack(side="left", expand=True, fill="both")

    btn_setting = tk.Button(bottom_nav, text="⚙", **button_style)
    btn_setting.pack(side="left", expand=True, fill="both")

    return bottom_nav

page_with_nav = [pageStatement]
for page in page_with_nav:
    create_bottom_nav(page)

page_no_nav = [page1,pageLogin,pageRegister]

frame = tk.Frame(page1, bg=page1["bg"])
frame.place(relx=0.5, rely=0.35, anchor="center")

# ==================== Page1 =====================
frame = tk.Frame(page1, bg=page1["bg"])
frame.place(relx=0.5, rely=0.35, anchor="center")

tk.Label(
    frame, text="WISH",
    font=("fc motorway", 48, "bold"),
    fg="#2EC7AD", bg=page1["bg"]
).pack(side="left")

tk.Label(
    frame, text="LIST",
    font=("fc motorway", 48, "bold"),
    fg="white", bg=page1["bg"]
).pack(side="left")

loginBTN = tk.Button(
    page1,
    text="LOGIN",
    font=("coda", 16, "bold"),
    bg="white", fg="black", bd=0,
    width=10,
    command=lambda: showPage(pageLogin)
)
loginBTN.place(relx=0.5, rely=0.5, anchor="center")

regisBTN = tk.Button(
    page1,
    text="Register",
    font=("coda", 16, "bold"),
    bg="white", fg="black", bd=0,
    width=10,
    command=lambda: showPage(pageRegister)
)
regisBTN.place(relx=0.5, rely=0.58, anchor="center")


# ==================== PageLogin =====================

tk.Label(
    pageLogin,
    text="LOGIN",
    font=("fc motorway", 36, "bold"),
    fg="white",
    bg=pageLogin["bg"]
).pack(pady=70)

tk.Button(
    pageLogin,
    text="Done",
    fg="black",
    font=("coda" , 16 , "bold"),
    width=10,
    bg="white", bd=0,
    command=lambda: showPage(pageStatement)
).place(relx=0.5, rely=0.54, anchor="center")

username = tk.Label(
    pageLogin,
    text="Username",
    font=("coda", 12 ,"bold"),
    fg="white",
    bg=pageLogin["bg"]
).place(relx=0.24, rely=0.283, anchor="center")

password = tk.Label(
    pageLogin,
    text="Password",
    font=("coda", 12 ,"bold"),
    fg="white",
    bg=pageLogin["bg"]
).place(relx=0.24, rely=0.375, anchor="center")

usename = tk.Entry(
    pageLogin,
    width=23,
    font=("coda",16)
).pack(pady=30)

password = tk.Entry(
    pageLogin,
    width=23,
    font=("coda",16)
).pack(pady=10)

# ==================== PageRegister =====================
tk.Label(
    pageRegister,
    text="REGISTER",
    font=("fc motorway", 36, "bold"),
    fg="white",
    bg=pageLogin["bg"]
).pack(pady=60)

tk.Label(
    pageRegister,
    text="Email",
    font=("coda", 12 ,"bold"),
    fg="white",
    bg=pageLogin["bg"]
).place(relx=0.2, rely=0.248, anchor="center")

tk.Label(
    pageRegister,
    text="Username",
    font=("coda", 12 ,"bold"),
    fg="white",
    bg=pageLogin["bg"]
).place(relx=0.245, rely=0.356, anchor="center")

tk.Label(
    pageRegister,
    text="Password",
    font=("coda", 12 ,"bold"),
    fg="white",
    bg=pageLogin["bg"]
).place(relx=0.245, rely=0.462, anchor="center")

tk.Label(
    pageRegister,
    text="Confirm",
    font=("coda", 12 ,"bold"),
    fg="white",
    bg=pageLogin["bg"]
).place(relx=0.224, rely=0.568, anchor="center")

email = tk.Entry(
    pageRegister,
    width=23,
    font=("coda",16)
).pack(pady=25)

usename = tk.Entry(
    pageRegister,
    width=23,
    font=("coda",16)
).pack(pady=25)

password = tk.Entry(
    pageRegister,
    width=23,
    font=("coda",16)
).pack(pady=25)

conPassword = tk.Entry(
    pageRegister,
    width=23,
    font=("coda",16)
).pack(pady=25)

tk.Button(
    pageRegister,
    text="Done",
    fg="black",
    font=("coda" , 16 , "bold"),
    width=10,
    bg="white", bd=0,
    command=lambda: showPage(pageLogin)
).pack(pady=25)

title_label = tk.Label(pageStatement, text="Statement",
                       font=title_font,
                       bg="#d9d9d9",
                       fg="black")
title_label.pack(pady=50)

# ==================== PageHome =====================
top_frame = tk.Frame(pageHome, bg="#d9d9d9")
top_frame.pack(pady=20)



# ======================
# Frame สำหรับ Income/Expense
# ======================
top_frame = tk.Frame(pageStatement, bg="#d9d9d9")
top_frame.pack(pady=20)

# ===== Total Income =====
income_frame = tk.Frame(top_frame,
                        width=150,
                        height=100,
                        bg="#000033")
income_frame.pack(side="left", padx=10)
income_frame.pack_propagate(False)

income_amount = tk.Label(income_frame,
                         text="X,XXX",
                         font=card_big_font,
                         bg="#000033",
                         fg="white")
income_amount.pack(pady=(10, 0), anchor="w", padx=15)

income_label = tk.Label(income_frame,
                        text="Total Income",
                        font=card_small_font,
                        bg="#000033",
                        fg="white")
income_label.pack(anchor="w", padx=15)

# ===== Total Expense =====
expense_frame = tk.Frame(top_frame,
                         width=150,
                         height=100,
                         bg="#f0f0f0")
expense_frame.pack(side="left", padx=10)
expense_frame.pack_propagate(False)

expense_amount = tk.Label(expense_frame,
                          text="X,XXX",
                          font=card_big_font,
                          bg="#f0f0f0",
                          fg="black")
expense_amount.pack(pady=(10, 0), anchor="w", padx=15)

expense_label = tk.Label(expense_frame,
                         text="Total Expense",
                         font=card_small_font,
                         bg="#f0f0f0",
                         fg="black")
expense_label.pack(anchor="w", padx=15)

# ======================
# Balance Card
# ======================
balance_frame = tk.Frame(pageStatement,
                         width=330,
                         height=120,
                         bg="#cfcfcf")
balance_frame.pack(pady=0)
balance_frame.pack_propagate(False)

balance_amount = tk.Label(balance_frame,
                          text="X,XXX",
                          font=card_big_font,
                          bg="#cfcfcf",
                          fg="black")
balance_amount.pack(pady=(10, 0))

balance_label = tk.Label(balance_frame,
                         text="Balance",
                         font=card_small_font,
                         bg="#cfcfcf",
                         fg="black")
balance_label.pack()

edit_income_btn = tk.Button(income_frame,
                            text="📝",
                            font=("Arial", 10),
                            bg="#000033",
                            fg="white",
                            border=0,
                            activebackground="#000033",
                            activeforeground="white",
                            cursor="hand2",)

edit_income_btn.place(relx=1.0, rely=1.0,
                      x=-8, y=-8,
                      anchor="se")

edit_expense_btn = tk.Button(expense_frame,
                             text="📝",
                             font=("Arial", 10),
                             bg="#f0f0f0",
                             fg="black",
                             border=0,
                             activebackground="#f0f0f0",
                             activeforeground="black",
                             cursor="hand2")

edit_expense_btn.place(relx=1.0, rely=1.0,
                       x=-8, y=-8,
                       anchor="se")



showPage(page1)
root.mainloop()