import tkinter as tk

def create_bottom_nav(parent):
    bottom_nav = tk.Frame(parent, height=70, bg="#000033")
    bottom_nav.pack(side="bottom", fill="x")

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


# ===== main window =====
root = tk.Tk()
root.geometry("390x740")
root.configure(bg="white")

create_bottom_nav(root)

root.mainloop()
