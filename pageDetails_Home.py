import customtkinter as ctk
from menu import create_bottom_nav

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class pageDetailsHome(ctk.CTkFrame):
    def __init__(self, master, showPage, controller):
        super().__init__(master, fg_color="#F5F5F5")
        self.showPage = showPage
        self.controller = controller

        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", pady=(12, 4))

        ctk.CTkLabel(
            header,
            text="Details",
            font=("Arial", 42, "bold"),
            text_color="black"
        ).pack(pady=(18, 10))

        ctk.CTkButton(
            header,
            text="‹",
            width=36,
            height=36,
            fg_color="transparent",
            hover_color="#EEEEEE",
            text_color="black",
            font=("Arial", 28, "bold"),
            command=lambda: self.showPage("home"),
        ).place(x=14, y=18)

        card_area = ctk.CTkFrame(
            self,
            fg_color="transparent",
            width=390,
            height=350
        )
        card_area.pack(pady=8)
        card_area.pack_propagate(False)

        self.target_label = self.card(card_area, "0", "Target Amount", 30, 40, dark=True)
        self.saved_label = self.card(card_area, "0", "Current Save", 200, 40)
        self.monthly_label = self.card(card_area, "0", "Monthly Save", 30, 190)
        self.remaining_label = self.card(card_area, "0", "Remaining", 200, 190)

        progress_section = ctk.CTkFrame(self, fg_color="transparent")
        progress_section.pack(fill="x", padx=30, pady=(10, 8))

        self.bar1 = ctk.CTkProgressBar(
            progress_section,
            height=12,
            progress_color="#2E7D32",
            fg_color="#A5D6A7"
        )
        self.bar1.pack(fill="x", pady=(0, 10))
        self.bar1.set(0)

        ctk.CTkLabel(
            progress_section,
            text="Saving Progress",
            font=("Arial", 11)
        ).pack(anchor="e", pady=(0, 6))

        self.bar2 = ctk.CTkProgressBar(
            progress_section,
            height=12,
            progress_color="#2E7D32",
            fg_color="#E0E0E0"
        )
        self.bar2.pack(fill="x")
        self.bar2.set(0)

        self.add_btn = ctk.CTkButton(
            self,
            text="Add Saving",
            width=220,
            height=44,
            fg_color="#2CAD1B",
            hover=False,
            font=("Arial", 16, "bold"),
            command=lambda: self.showPage("addsaving")
        )
        self.add_btn.pack(pady=(6, 18))

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

        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=("Arial", 26, "bold"),
            text_color=txt
        )
        value_label.place(relx=0.5, rely=0.45, anchor="center")

        ctk.CTkLabel(
            card,
            text=label,
            font=("Arial", 14),
            text_color=txt
        ).place(relx=0.5, rely=0.7, anchor="center")

        return value_label

    def refresh(self):

        plan = self.controller.current_plan

        if not plan:
            return

        target = plan["target"]
        saved = plan["saved"]
        duration = plan["duration"]

        percent = saved / target if target else 0
        percent = min(percent, 1)

        plan["percent"] = percent

        remaining = max(target - saved, 0)
        monthly = target / duration if duration else 0

        self.bar1.set(percent)

        self.target_label.configure(text=f"{target:,.0f}")
        self.saved_label.configure(text=f"{saved:,.0f}")
        self.monthly_label.configure(text=f"{monthly:,.0f}")
        self.remaining_label.configure(text=f"{remaining:,.0f}")

        self.bar1.set(percent)

        if plan.get("completed"):
            self.add_btn.pack_forget()
        else:
            if not self.add_btn.winfo_ismapped():
                self.add_btn.pack(pady=(6, 18))