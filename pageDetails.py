import customtkinter as ctk
from menu import create_bottom_nav

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class pageDetails(ctk.CTkFrame):
    def __init__(self, master, showPage, controller):
        super().__init__(master, fg_color="#F5F5F5")
        self.showPage = showPage
        self.controller = controller

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", pady=(12, 4))

        ctk.CTkLabel(
            header,
            text="Details",
            font=("Arial", 22, "bold")
        ).pack(anchor="center")

        card_area = ctk.CTkFrame(
            self,
            fg_color="transparent",
            width=390,
            height=400
        )
        card_area.pack(pady=8)
        card_area.pack_propagate(False)

        self.card(card_area, "X,XXX", "Target Amount", 30, 50, dark=True)
        self.card(card_area, "X,XXX", "Current Save", 200, 50)
        self.card(card_area, "X,XXX", "Monthly Save", 30, 200)
        self.card(card_area, "X,XXX", "Remaining", 200, 200)

        progress_section = ctk.CTkFrame(self, fg_color="transparent")
        progress_section.pack(fill="x", padx=30, pady=(0, 8))

        ctk.CTkLabel(progress_section, text="100%").pack(anchor="e")

        bar1 = ctk.CTkProgressBar(
            progress_section,
            height=12,
            progress_color="#2E7D32",
            fg_color="#A5D6A7"
        )
        bar1.set(1)
        bar1.pack(fill="x", pady=(0, 6))

        ctk.CTkLabel(
            progress_section,
            text="3/3 Month",
            font=("Arial", 11)
        ).pack(anchor="e", pady=(0, 6))

        bar2 = ctk.CTkProgressBar(
            progress_section,
            height=12,
            progress_color="#2E7D32",
            fg_color="#E0E0E0"
        )
        bar2.set(1)
        bar2.pack(fill="x")

        ctk.CTkButton(
            self,
            text="Done",
            width=220,
            height=44,
            fg_color="#6E0E0A",
            hover_color="#7A0000",
            font=("Arial", 16, "bold")
        ).pack(pady=(6, 18))
        
        footer = ctk.CTkFrame(
                self,
                height=80,
                corner_radius=0,
                fg_color="transparent"
                )
        footer.pack(side="bottom", fill="x")
        footer.pack_propagate(False)

        create_bottom_nav(footer, self.showPage)

    def card(self, parent, value, label, x, y, dark=False):
        bg = "#0A1E4A" if dark else "#E9E9E9"
        txt = "white" if dark else "black"

        card = ctk.CTkFrame(
            parent,
            width=160,
            height=140,
            corner_radius=15,
            fg_color=bg
        )
        card.place(x=x, y=y)

        ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 26, "bold"),
            text_color=txt
        ).place(relx=0.5, rely=0.45, anchor="center")

        ctk.CTkLabel(
            card,
            text=label,
            font=("Arial", 14),
            text_color=txt
        ).place(relx=0.5, rely=0.7, anchor="center")

        

if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Saving App")
    app.geometry("390x740")
    app.resizable(False, False)

    page = pageDetails(app, None, None)
    page.pack(fill="both", expand=True)

    app.mainloop()