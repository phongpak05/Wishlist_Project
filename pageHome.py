import customtkinter as ctk
from menu import create_bottom_nav
from components import planCard

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
            font=("fc motorway", 58, "bold"),
            text_color="black"
        ).pack(pady=(16, 10))

        user_bar = ctk.CTkFrame(
            header,
            fg_color="#0A1E4A",
            corner_radius=18,
            height=62
        )
        user_bar.pack(padx=20, pady=(0, 10), fill="x")
        user_bar.pack_propagate(False)

        ctk.CTkLabel(
                user_bar, 
                text="👤",
                font=("Arial", 48),
                text_color="#FFFFFF"
            ).place(relx=0.12, rely=0.45, anchor="center")

        self.username_label = ctk.CTkLabel(
            user_bar,
            text="Username",
            font=("Arial", 22),
            text_color="white")
        
        self.username_label.place(x=78, rely=0.5, anchor="w")

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
            hover_color="#0A1E4A",
            text_color="white",
            command=lambda: self.showPage("newplan"))
        
        self.add_btn.grid(row=1, column=0, pady=20)

        self.footer = ctk.CTkFrame(self, 
                                   height=80, 
                                   corner_radius=0, 
                                   fg_color="#0A1E4A")
        self.footer.grid(row=2, column=0, sticky="ew")
        self.footer.grid_propagate(False)
        create_bottom_nav(self.footer, self.showPage)

    def refresh(self):
        self.username_label.configure(text=getattr(self.controller, "current_username", "Username"))

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
            card = planCard(
                self.list_frame,
                name=p.get("name", f"plan {i+1}"),
                percent=p.get("percent", 0),
                bar_color=p.get("color", "#2E7D32"),
                command=lambda pid=p.get("id", i+1): self.on_open_details(pid)
            )
            card.grid(row=i, column=0, sticky="ew", pady=8)

    def on_open_details(self, plan_id):
        print("Open details for plan_id:", plan_id)