import tkinter as tk

root = tk.Tk()

root.title("Wishlist")
root.configure(background="#000F36")
root.geometry("390x740+1080+20")
root.resizable(False,False)

def showPage(page):
    page.tkraise()

page1 = tk.Frame(root, bg="#000F36")
pageLogin = tk.Frame(root, bg="#000F36")
pageRegister = tk.Frame(root, bg="#B61818")

for p in (page1, pageLogin, pageRegister):
    p.place(x=0, y=0, relwidth=1, relheight=1)

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
    command=lambda: showPage(page1)
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
    pageLogin,
    text="REGISTER",
    font=("fc motorway", 36, "bold"),
    fg="white",
    bg=pageLogin["bg"]
).pack(pady=70)

showPage(pageRegister)
root.mainloop()