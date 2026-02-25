import customtkinter as ctk

ctk.set_appearance_mode("light")

def create_bottom_nav(parent):

    bottom_nav = ctk.CTkFrame(
        parent,
        height=68,  
        fg_color="#0A1E4A",
        corner_radius=0
    )
    bottom_nav.pack(side="bottom", fill="x")
    bottom_nav.pack_propagate(False)

    nav_frame = ctk.CTkFrame(bottom_nav, fg_color="transparent")
    nav_frame.pack(expand=True, fill="both")

    buttons = []
    active_button = []

    def set_active(selected_btn):
        for btn in buttons:
            btn.configure(text_color="#94A3B8")
        selected_btn.configure(text_color="white")

    def create_button(icon, column):

        btn = ctk.CTkButton(
            nav_frame,
            text=icon,
            fg_color="transparent",
            hover_color="#0A1E4A",
            text_color="#94A3B8",
            font=("Segoe UI Emoji", 24),
            corner_radius=0,
            border_width=0,
            height=68
        )

        btn.grid(row=0, column=column, sticky="nsew")

        def on_click():
            active_button.clear()
            active_button.append(btn)
            set_active(btn)

        btn.configure(command=on_click)

        buttons.append(btn)
        return btn

    for i in range(4):
        nav_frame.grid_columnconfigure(i, weight=1)

    btn_home = create_button("🏠", 0)
    btn_chart = create_button("📊", 1)
    btn_history = create_button("🕒", 2)
    btn_setting = create_button("⚙", 3)

    active_button.append(btn_home)
    set_active(btn_home)

root = ctk.CTk()
root.geometry("390x740")
root.title("Finance App")
root.resizable(False, False)

create_bottom_nav(root)

root.mainloop()