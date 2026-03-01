import customtkinter as ctk
<<<<<<< HEAD
=======
from menu import create_bottom_nav
>>>>>>> 939e1c34bfce591eef17abec4e2222a94e2232ca

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class pageDetails(ctk.CTkFrame):
<<<<<<< HEAD
    def __init__(self, master):
        super().__init__(master, fg_color="#F5F5F5")
        self.pack(fill="both", expand=True)

        # ---------- Header ----------
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", pady=(12, 4))

        ctk.CTkLabel(
            header,
            text="Details",
            font=("Arial", 22, "bold")
        ).pack(anchor="center")

        # ---------- Cards Area ----------
=======
    def __init__(self, master, showPage, controller):
        super().__init__(master, fg_color="#F5F5F5")
        self.showPage = showPage
        self.controller = controller

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", pady=(12, 4))

        ctk.CTkLabel(header, 
                     text="Details", 
                     font=("Arial", 42, "bold"), 
                     text_color="black").pack(pady=(18, 10))

        ctk.CTkButton(
            header,
            text="‹",
            width=36,
            height=36,
            fg_color="transparent",
            hover=False,
            text_color="black",
            font=("Arial", 28, "bold"),
            command=lambda: self.showPage("home"),
        ).place(x=14, y=18)

>>>>>>> 939e1c34bfce591eef17abec4e2222a94e2232ca
        card_area = ctk.CTkFrame(
            self,
            fg_color="transparent",
            width=390,
<<<<<<< HEAD
            height=400          # ⬅️ คุมความสูงไม่ให้ล้น
=======
            height=400
>>>>>>> 939e1c34bfce591eef17abec4e2222a94e2232ca
        )
        card_area.pack(pady=8)
        card_area.pack_propagate(False)

<<<<<<< HEAD
        # ---------- Cards (สมดุลแล้ว) ----------
        self.card(card_area, "X,XXX", "Target Amount", 30, 50, dark=True)
        self.card(card_area, "X,XXX", "Current Save", 200, 50)
        self.card(card_area, "X,XXX", "Monthly Save", 30, 230)
        self.card(card_area, "X,XXX", "Remaining", 200, 230)

        # ---------- Progress ----------
=======
        self.card(card_area, "X,XXX", "Target Amount", 30, 50, dark=True)
        self.card(card_area, "X,XXX", "Current Save", 200, 50)
        self.card(card_area, "X,XXX", "Monthly Save", 30, 200)
        self.card(card_area, "X,XXX", "Remaining", 200, 200)

>>>>>>> 939e1c34bfce591eef17abec4e2222a94e2232ca
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

<<<<<<< HEAD
        # ---------- Done Button ----------
=======
>>>>>>> 939e1c34bfce591eef17abec4e2222a94e2232ca
        ctk.CTkButton(
            self,
            text="Done",
            width=220,
            height=44,
            fg_color="#6E0E0A",
            hover_color="#7A0000",
            font=("Arial", 16, "bold")
        ).pack(pady=(6, 18))
<<<<<<< HEAD

    # ---------- Card ----------
=======
        
        footer = ctk.CTkFrame(
                self,
                height=80,
                corner_radius=0,
                fg_color="transparent"
                )
        footer.pack(side="bottom", fill="x")
        footer.pack_propagate(False)

        create_bottom_nav(footer, self.showPage)

>>>>>>> 939e1c34bfce591eef17abec4e2222a94e2232ca
    def card(self, parent, value, label, x, y, dark=False):
        bg = "#0A1E4A" if dark else "#E9E9E9"
        txt = "white" if dark else "black"

        card = ctk.CTkFrame(
            parent,
<<<<<<< HEAD
            width=160,          # ✅ ขนาดที่เหมาะสม
=======
            width=160,
>>>>>>> 939e1c34bfce591eef17abec4e2222a94e2232ca
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

<<<<<<< HEAD

# ---------- RUN ----------
=======
        

>>>>>>> 939e1c34bfce591eef17abec4e2222a94e2232ca
if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Saving App")
    app.geometry("390x740")
    app.resizable(False, False)

<<<<<<< HEAD
    pageDetails(app)
=======
    page = pageDetails(app, None, None)
    page.pack(fill="both", expand=True)

>>>>>>> 939e1c34bfce591eef17abec4e2222a94e2232ca
    app.mainloop()