import tkinter as tk
from tkinter import messagebox

def calculate_tax():
    try:
        income = float(entry_income.get())
        other_income = float(entry_other_income.get())
        num_children = int(entry_children.get())
        donation = float(entry_donation.get())

        total_income = income + other_income

        personal_deduction = 30000

        child_deduction = 0
        if num_children >= 1:
            child_deduction += 30000
        if num_children >= 2:
            child_deduction += 60000
        if num_children > 2:
            child_deduction += (num_children - 2) * 60000

        donation_deduction = min(donation * 3, 20000)

        total_deduction = personal_deduction + child_deduction + donation_deduction

        net_income = total_income - total_deduction
        if net_income < 0:
            net_income = 0

        tax = 0
        brackets = [
            (150000, 0.00),
            (300000, 0.05),
            (500000, 0.10),
            (750000, 0.15),
            (1000000, 0.20),
            (2000000, 0.25),
            (5000000, 0.30),
            (float('inf'), 0.35)
        ]

        prev_limit = 0
        for limit, rate in brackets:
            if net_income > prev_limit:
                taxable = min(net_income, limit) - prev_limit
                tax += taxable * rate
                prev_limit = limit
            else:
                break

        result_label.config(
            text=f"เงินได้สุทธิ: {net_income:,.2f} บาท\n"
                 f"ภาษีที่ต้องชำระ: {tax:,.2f} บาท"
        )

    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกข้อมูลเป็นตัวเลขให้ถูกต้อง")

root = tk.Tk()
root.title("Income Tax Calculator")
root.geometry("520x500")
root.resizable(False, False)
root.configure(bg="#E8F0FE")

header = tk.Frame(root, bg="#1E3A8A", height=80)
header.pack(fill="x")

tk.Label(
    header,
    text="โปรแกรมคำนวณภาษีเงินได้บุคคลธรรมดา",
    bg="#1E3A8A",
    fg="white",
    font=("Arial", 16, "bold")
).pack(pady=20)

card = tk.Frame(root, bg="white", bd=0)
card.place(relx=0.5, rely=0.55, anchor="center", width=450, height=340)

def create_input(label_text, row):
    tk.Label(card, text=label_text, bg="white", font=("Arial", 11)).grid(
        row=row, column=0, padx=15, pady=10, sticky="e"
    )
    entry = tk.Entry(card, width=25, font=("Arial", 11), bd=2, relief="groove")
    entry.grid(row=row, column=1, padx=15)
    return entry

entry_income = create_input("รายได้ทั้งปี (บาท):", 0)
entry_other_income = create_input("รายได้อื่นๆ (บาท):", 1)
entry_children = create_input("จำนวนบุตร:", 2)
entry_donation = create_input("เงินบริจาค (บาท):", 3)

tk.Button(
    card,
    text="คำนวณภาษี",
    command=calculate_tax,
    bg="#2563EB",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    relief="flat",
    cursor="hand2"
).grid(row=4, column=0, columnspan=2, pady=20)

result_label = tk.Label(
    card,
    text="",
    bg="white",
    fg="#1E3A8A",
    font=("Arial", 12, "bold")
)
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()