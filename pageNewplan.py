import customtkinter as ctk
from menu import create_bottom_nav

class pageNewplan(ctk.CTkFrame):
    def __init__(self, parent, showPage, controller):
        super().__init__(parent, fg_color="#F5F5F5")
        self.showPage = showPage
        self.controller = controller

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = ctk.CTkFrame(self, 
                              height=120, 
                              corner_radius=0, 
                              fg_color="#F5F5F5")
        header.grid(row=0, column=0, sticky="ew")
        header.grid_propagate(False)

        ctk.CTkLabel(header, 
                     text="New Plan", 
                     font=("Arial", 22, "bold"), 
                     text_color="black").pack(pady=(18, 10))

        ctk.CTkButton(header, 
                      text="Back", 
                      width=80, 
                      height=32,
                      command=lambda: self.showPage("home")
        ).pack()

        content = ctk.CTkFrame(self, 
                               fg_color="transparent")
        content.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)
        content.grid_columnconfigure(0, weight=1)

        self.ent_name = ctk.CTkEntry(content, 
                                     placeholder_text="Goal name (e.g., iPhone)")
        self.ent_name.grid(row=0, column=0, sticky="ew", pady=(10, 8))

        self.ent_target = ctk.CTkEntry(content, 
                                       placeholder_text="Target amount (Baht)")
        self.ent_target.grid(row=1, column=0, sticky="ew", pady=8)

        self.ent_duration = ctk.CTkEntry(content, 
                                         placeholder_text="Duration (months)")
        self.ent_duration.grid(row=2, column=0, sticky="ew", pady=8)

        self.ent_priority = ctk.CTkEntry(content, 
                                         placeholder_text="Priority (1-5)")
        self.ent_priority.grid(row=3, column=0, sticky="ew", pady=8)

        self.err = ctk.CTkLabel(content, 
                                text="", text_color="red")
        self.err.grid(row=4, column=0, sticky="w", pady=(4, 0))

        ctk.CTkButton(content, 
                      text="Save Plan", 
                      height=44, 
                      corner_radius=12,
                      fg_color="#0A1E4A", 
                      hover_color="#0A1E4A",
                      command=self.on_save
        ).grid(row=5, column=0, sticky="ew", pady=(16, 0))

        footer = ctk.CTkFrame(self, 
                              height=80, 
                              corner_radius=0, 
                              fg_color="#0A1E4A")
        footer.grid(row=2, column=0, sticky="ew")
        footer.grid_propagate(False)
        create_bottom_nav(footer)

    def on_save(self):
        name = self.ent_name.get().strip()
        target = self.ent_target.get().strip()
        duration = self.ent_duration.get().strip()
        priority = self.ent_priority.get().strip()

        if not name:
            self.err.configure(text="กรุณากรอกชื่อแผน")
            return

        try:
            target_val = float(target) if target else 0
            duration_val = int(duration) if duration else 0
            priority_val = int(priority) if priority else 1
        except ValueError:
            self.err.configure(text="กรุณากรอกตัวเลขให้ถูกต้อง")
            return

        new_id = len(self.controller.plans) + 1
        self.controller.plans.append({
            "id": new_id,
            "name": name,
            "percent": 0,         
            "color": "#2E7D32",
            "target": target_val,
            "duration": duration_val,
            "priority": priority_val
        })

        self.ent_name.delete(0, "end")
        self.ent_target.delete(0, "end")
        self.ent_duration.delete(0, "end")
        self.ent_priority.delete(0, "end")
        self.err.configure(text="")

        self.showPage("home")