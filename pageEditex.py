import tkinter as tk


class EditExpensePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#E9E9E9")

        header = tk.Frame(self, bg="#E9E9E9")
        header.pack(fill="x", pady=(20, 0))

        back_btn = tk.Label(
            header,
            text="<",
            font=("Arial", 18, "bold"),
            bg="#E9E9E9",
            fg="black",
            cursor="hand2"
        )
        back_btn.pack(side="left", padx=20)

        title = tk.Label(
            self,
            text="Edit Expense",
            font=("Arial Black", 18),
            bg="#E9E9E9",
            fg="black"
        )
        title.pack(pady=(10, 30))

        form_frame = tk.Frame(self, bg="#E9E9E9")
        form_frame.pack(pady=10)

        income_label = tk.Label(
            form_frame,
            text="Income",
            font=("Arial", 10),
            bg="#E9E9E9",
            fg="#444"
        )
        income_label.pack(anchor="w")

        self.income_entry = tk.Entry(
            form_frame,
            font=("Arial", 12),
            bg="#DDDDDD",
            relief="flat",
            width=25
        )
        self.income_entry.insert(0, "Bath")
        self.income_entry.pack(pady=5, ipady=6)

        save_btn = tk.Button(
            self,
            text="Save",
            command=self.save,
            font=("Arial", 12, "bold"),
            bg="#1E7D22",
            fg="white",
            activebackground="#16651A",
            relief="flat",
            width=12
        )
        save_btn.pack(pady=20)

    def save(self):
        print("Saved:", self.income_entry.get())

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Expense App")
    root.geometry("390x740")

    root.resizable(False, False)

    page = EditExpensePage(root)
    page.pack(fill="both", expand=True)

    root.mainloop()