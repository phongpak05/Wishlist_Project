import tkinter as tk


def create_bottom_nav(parent):

    bottom_nav = tk.Frame(parent, height=75, bg="#0F172A")
    bottom_nav.pack(side="bottom", fill="x")

    top_line = tk.Frame(bottom_nav, height=1, bg="#1E293B")
    top_line.pack(side="top", fill="x")

    nav_frame = tk.Frame(bottom_nav, bg="#0F172A")
    nav_frame.pack(expand=True, fill="both")

    button_style = {
        "bg": "#0F172A",
        "fg": "#94A3B8",
        "activebackground": "#0F172A",
        "activeforeground": "white",
        "border": 0,
        "highlightthickness": 0,
        "font": ("Segoe UI Emoji", 18),
        "relief": "flat",
        "bd": 0,
        "cursor": "hand2"
    }

    buttons = []
    active_button = []

    def set_active(selected_btn):
        for btn in buttons:
            btn.config(fg="#94A3B8")
        selected_btn.config(fg="white")

    def on_enter(e):
        e.widget.config(fg="white")

    def on_leave(e):
        if e.widget not in active_button:
            e.widget.config(fg="#94A3B8")

    def create_button(icon):
        btn = tk.Button(nav_frame, text=icon, **button_style)
        btn.pack(side="left", expand=True, fill="both")

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

        def on_click():
            active_button.clear()
            active_button.append(btn)
            set_active(btn)

        btn.config(command=on_click)

        buttons.append(btn)
        return btn

    btn_home = create_button("🏠")
    btn_chart = create_button("📊")
    btn_history = create_button("🕒")
    btn_setting = create_button("⚙")

    active_button.append(btn_home)
    set_active(btn_home)

root = tk.Tk()
root.geometry("390x740")
root.configure(bg="white")
root.title("Finance App")

root.resizable(False, False)

create_bottom_nav(root)

root.mainloop()