import customtkinter as ctk

def create_bottom_nav(parent, showPage):
    bottom_nav = ctk.CTkFrame(parent, height=70, fg_color="#0A1E4A", corner_radius=0)
    bottom_nav.pack(fill="both", expand=True)
    bottom_nav.pack_propagate(False)

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

    btn_home = tk.Button(bottom_nav, 
                         text="🏠", 
                         **button_style)
    btn_home.pack(side="left", expand=True, fill="both")

    ctk.CTkButton(
        bottom_nav, 
        text="📊", 
        **button_style,
        command=lambda: showPage("statement")
    ).pack(side="left", expand=True, fill="both")

    ctk.CTkButton(
        bottom_nav, 
        text="🕒", 
        **button_style,
        command=lambda: showPage("history")
    ).pack(side="left", expand=True, fill="both")

    ctk.CTkButton(
        bottom_nav, 
        text="⚙", 
        **button_style,
        command=lambda: showPage("setting")
    ).pack(side="left", expand=True, fill="both")

    return bottom_nav