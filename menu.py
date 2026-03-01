import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def create_bottom_nav(parent, showPage=None):

    bottom_nav = ctk.CTkFrame(parent, height=70, corner_radius=0 , fg_color="#000033")
    bottom_nav.pack(side="bottom", fill="x")

    btn_home = ctk.CTkButton(
        bottom_nav,
        text="🏠",
        fg_color="transparent",
        font = ("Segoe UI Emoji", 24),
        hover=False,
        width=80,
        command=(lambda: showPage("home")) if showPage else None
    )
    btn_home.pack(side="left", expand=True, pady=10)

    btn_chart = ctk.CTkButton(
        bottom_nav,
        text="📊",
        fg_color="transparent",
        font = ("Segoe UI Emoji", 24),
        hover=False,
        width=80,
        command=(lambda: showPage("statement")) if showPage else None
    )
    btn_chart.pack(side="left", expand=True, pady=10)

    btn_history = ctk.CTkButton(
        bottom_nav,
        text="🕒",
        fg_color="transparent",
        font = ("Segoe UI Emoji", 24),
        hover=False,
        width=80,
        command=(lambda: showPage("history")) if showPage else None
    )
    btn_history.pack(side="left", expand=True, pady=10)

    btn_setting = ctk.CTkButton(
        bottom_nav,
        text="⚙",
        fg_color="transparent",
        font = ("Segoe UI Emoji", 24),
        hover=False,
        width=80,
        command=(lambda: showPage("setting")) if showPage else None
    )
    btn_setting.pack(side="left", expand=True, pady=10)


if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("390x740")

    create_bottom_nav(app)

    app.mainloop()