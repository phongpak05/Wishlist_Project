import tkinter as tk

def create_bottom_nav(parent):
    bottom_nav = tk.Frame(parent, height=70, bg="#000033")
    bottom_nav.pack(side="bottom", fill="x")

    btn_home = tk.Button(bottom_nav, text="🏠",
                         bg="#000033", fg="white",
                         activebackground=bottom_nav["bg"],activeforeground="white",
                         border=0,
                         font=("Segoe UI", 16))
    btn_home.pack(side="left", expand=True)

    btn_chart = tk.Button(bottom_nav, text="📊",
                          bg="#000033", fg="white",
                          activebackground=bottom_nav["bg"],activeforeground="white",
                          border=0,
                          font=("Segoe UI", 16))
    btn_chart.pack(side="left", expand=True)

    btn_history = tk.Button(bottom_nav, text="🕒",
                            bg="#000033", fg="white",
                            activebackground=bottom_nav["bg"],activeforeground="white",
                            border=0,
                            font=("Segoe UI", 16))
    btn_history.pack(side="left", expand=True)

    btn_setting = tk.Button(bottom_nav, text="⚙",
                            bg="#000033", fg="white",
                            activebackground=bottom_nav["bg"],activeforeground="white",
                            border=0,
                            font=("Segoe UI", 16))
    btn_setting.pack(side="left", expand=True)


# ===== main window =====
root = tk.Tk()
root.geometry("390x740+1080+20")

create_bottom_nav(root)

root.mainloop()
