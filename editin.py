import tkinter as tk

# ==============================
# MAIN WINDOW
# ==============================
root = tk.Tk()
root.geometry("390x740")
root.configure(bg="#E9E9E9")
root.title("Edit Income")
root.resizable(False, False)

# ==============================
# HEADER (Back + Title)
# ==============================
header = tk.Frame(root, bg="#E9E9E9")
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
    root,
    text="Edit Income",
    font=("Arial Black", 18),
    bg="#E9E9E9",
    fg="black"
)
title.pack(pady=(10, 30))

# ==============================
# FORM SECTION
# ==============================
form_frame = tk.Frame(root, bg="#E9E9E9")
form_frame.pack(pady=10)

income_label = tk.Label(
    form_frame,
    text="Income",
    font=("Arial", 10),
    bg="#E9E9E9",
    fg="#444"
)
income_label.pack(anchor="w", padx=0)

income_entry = tk.Entry(
    form_frame,
    font=("Arial", 12),
    bg="#DDDDDD",
    relief="flat",
    width=25
)
income_entry.insert(0, "Bath")
income_entry.pack(pady=5, ipady=6)

# ==============================
# SAVE BUTTON
# ==============================
def save():
    print("Saved:", income_entry.get())

save_btn = tk.Button(
    root,
    text="Save",
    command=save,
    font=("Arial", 12, "bold"),
    bg="#1E7D22",
    fg="white",
    activebackground="#16651A",
    relief="flat",
    width=12
)
save_btn.pack(pady=20)

root.mainloop()
