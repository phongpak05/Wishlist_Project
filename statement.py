import tkinter as tk

# ======================
# ตั้งค่าหน้าต่างหลัก
# ======================
root = tk.Tk()
root.title("Wishlist App")
root.geometry("390x740")
root.resizable(False, False)
root.configure(bg="#d9d9d9")

# ======================
# ฟอนต์
# ======================
title_font = ("Segoe UI", 26, "bold")
card_big_font = ("Helvetica", 16, "bold")
card_small_font = ("Helvetica", 10)

# ======================
# หัวข้อ Statement
# ======================
title_label = tk.Label(root, text="Statement",
                       font=title_font,
                       bg="#d9d9d9",
                       fg="black")
title_label.pack(pady=50)

# ======================
# Frame สำหรับ Income/Expense
# ======================
top_frame = tk.Frame(root, bg="#d9d9d9")
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
balance_frame = tk.Frame(root,
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
                            bg=income_frame["bg"],
                            activebackground=income_frame["bg"],
                            activeforeground="white",
                            fg="white",
                            border=0)

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

def create_bottom_nav(parent):
    bottom_nav = tk.Frame(parent, height=70, bg="#000033")
    bottom_nav.pack(side="bottom", fill="x")

    btn_home = tk.Button(bottom_nav, text="🏠",
                         bg="#000033", fg="white",
                         border=0,
                         activebackground=bottom_nav["bg"],
                         activeforeground="white",
                         font=("Segoe UI", 16))
    btn_home.pack(side="left", expand=True)

    btn_chart = tk.Button(bottom_nav, text="📊",
                          bg="#000033", fg="white",
                          border=0,
                          font=("Segoe UI", 16))
    btn_chart.pack(side="left", expand=True)

    btn_history = tk.Button(bottom_nav, text="🕒",
                            bg="#000033", fg="white",
                            border=0,
                            font=("Segoe UI", 16))
    btn_history.pack(side="left", expand=True)

    btn_setting = tk.Button(bottom_nav, text="⚙",
                            bg="#000033", fg="white",
                            border=0,
                            font=("Segoe UI", 16))
    btn_setting.pack(side="left", expand=True)


# ======================
# เริ่มโปรแกรม
# ======================
create_bottom_nav(root)
root.mainloop()