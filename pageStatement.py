import tkinter as tk

class StatementPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#d9d9d9")

        title_font = ("Segoe UI", 26, "bold")
        card_big_font = ("Helvetica", 16, "bold")
        card_small_font = ("Helvetica", 10)

        title_label = tk.Label(self, text="Statement",
                               font=title_font,
                               bg="#d9d9d9")
        title_label.pack(pady=50)

        top_frame = tk.Frame(self, bg="#d9d9d9")
        top_frame.pack(pady=20)

        income_frame = tk.Frame(top_frame, width=150, height=100, bg="#000033")
        income_frame.pack(side="left", padx=10)
        income_frame.pack_propagate(False)

        tk.Label(income_frame, text="X,XXX", font=card_big_font,
                 bg="#000033", fg="white").pack(pady=(10,0), anchor="w", padx=15)

        tk.Label(income_frame, text="Total Income", font=card_small_font,
                 bg="#000033", fg="white").pack(anchor="w", padx=15)

        expense_frame = tk.Frame(top_frame, width=150, height=100, bg="#f0f0f0")
        expense_frame.pack(side="left", padx=10)
        expense_frame.pack_propagate(False)

        tk.Label(expense_frame, text="X,XXX", font=card_big_font,
                 bg="#f0f0f0", fg="black").pack(pady=(10,0), anchor="w", padx=15)

        tk.Label(expense_frame, text="Total Expense", font=card_small_font,
                 bg="#f0f0f0", fg="black").pack(anchor="w", padx=15)

        balance_frame = tk.Frame(self, width=330, height=120, bg="#cfcfcf")
        balance_frame.pack()
        balance_frame.pack_propagate(False)

        tk.Label(balance_frame, text="X,XXX", font=card_big_font,
                 bg="#cfcfcf").pack(pady=(10,0))

        tk.Label(balance_frame, text="Balance", font=card_small_font,
                 bg="#cfcfcf").pack()
        
        tk.Button(income_frame,
                  text="📝",
                  font=("Arial",10),
                  bg=income_frame["bg"],
                  fg="white",
                  border=0,
                  activebackground=income_frame["bg"],
                  activeforeground="white",
                  ).place(relx=1.0, rely=1.0,x=-8, y=-8,anchor="se")
        tk.Button(expense_frame,
                  text="📝",
                  font=("Arial",10),
                  bg=expense_frame["bg"],
                  fg="black",
                  border=0,
                  activebackground=expense_frame["bg"],
                  activeforeground="black",
                  ).place(relx=1.0, rely=1.0,x=-8, y=-8,anchor="se")
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Statement Test")
    root.geometry("390x740")

    page = StatementPage(root)
    page.pack(fill="both", expand=True)

    root.mainloop()