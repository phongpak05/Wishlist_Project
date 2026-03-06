import customtkinter as ctk
from menu import create_bottom_nav
from components import planCard
from userBar import userBar

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class pageHome(ctk.CTkFrame):
    def __init__(self, master, showPage, controller):
        super().__init__(master, fg_color="#F5F5F5")

        self.controller = controller
        self.showPage = showPage

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=0)

        header = ctk.CTkFrame(self, height=160, corner_radius=0, fg_color="#F5F5F5")
        header.grid(row=0, column=0, sticky="ew")
        header.grid_propagate(False)

        ctk.CTkLabel(
            header,
            text="HOME",
            font=("Arial", 42, "bold"),
            text_color="black"
        ).pack(pady=(16, 10))

        self.user_bar = userBar(header, "Username")
        self.user_bar.pack(padx=20, pady=(0, 10), fill="x")

        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        self.content.grid_rowconfigure(0, weight=1)
        self.content.grid_columnconfigure(0, weight=1)

        self.list_frame = ctk.CTkScrollableFrame(self.content, fg_color="transparent")
        self.list_frame.grid(row=0, column=0, sticky="nsew")
        self.list_frame.grid_columnconfigure(0, weight=1)

        self.add_btn = ctk.CTkButton(
            self.content,
            text="+ Plan",
            width=160,
            height=44,
            corner_radius=12,
            fg_color="#0A1E4A",
            hover_color="#081633",
            text_color="white",
            command=self.go_add_plan
        )
        self.add_btn.grid(row=1, column=0, pady=20)

        self.footer = ctk.CTkFrame(
            self,
            height=80,
            corner_radius=0,
            fg_color="#0A1E4A"
        )
        self.footer.grid(row=2, column=0, sticky="ew")
        self.footer.grid_propagate(False)

        create_bottom_nav(self.footer, self.showPage)

    def refresh(self):

        self.user_bar.set_username(
            getattr(self.controller, "current_username", "Username")
        )

        for w in self.list_frame.winfo_children():
            w.destroy()

        plans = getattr(self.controller, "plans", [])

        if len(plans) == 0:
            empty = ctk.CTkFrame(self.list_frame, corner_radius=16, fg_color="#FFFFFF")
            empty.grid(row=0, column=0, sticky="ew", pady=20)
            empty.grid_columnconfigure(0, weight=1)

            ctk.CTkLabel(
                empty,
                text="ยังไม่มีแผนการออม\nกด + Plan เพื่อเพิ่มแผนใหม่",
                font=("Arial", 14),
                text_color="gray"
            ).grid(row=0, column=0, pady=30, padx=20)

            return

        for i, p in enumerate(plans):

            percent = 0
            if p.get("target", 0) > 0:
                percent = p.get("saved", 0) / p.get("target", 1)

            card = planCard(
                self.list_frame,
                name=p.get("name", f"plan {i+1}"),
                percent=percent,
                bar_color=p.get("color", "#2E7D32"),
                command=lambda pid=p.get("id", i+1): self.on_open_details(pid)
            )

            card.grid(row=i, column=0, sticky="ew", pady=8)

    def on_open_details(self, plan_id):

        for p in self.controller.plans:
            if p["id"] == plan_id:
                self.controller.current_plan = p
                break

        self.showPage("detailhome")

    def go_add_plan(self):

        if (self.controller.income is None 
            or self.controller.expense is None
            or self.controller.permonth is None):
            self.show_warning_popup()
            return

        self.showPage("newplan")

    def show_warning_popup(self):

        popup = ctk.CTkToplevel(self)
        popup.geometry("320x170")
        popup.title("Warning")

        popup.transient(self.winfo_toplevel())
        popup.grab_set()

        x = self.winfo_rootx() + 40
        y = self.winfo_rooty() + 200
        popup.geometry(f"+{x}+{y}")

        label = ctk.CTkLabel(
            popup,
            text="กรุณากรอก Statement ก่อน",
            font=("Arial", 16),
            wraplength=260
        )
        label.pack(pady=30)

        btn = ctk.CTkButton(
            popup,
            text="OK",
            hover=False,
            command=lambda : [popup.destroy(), self.showPage("statement")]
        )
        btn.pack(pady=10)