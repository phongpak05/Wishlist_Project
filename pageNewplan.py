import customtkinter as ctk
from menu import create_bottom_nav

class pageNewplan(ctk.CTkFrame):
    def __init__(self, parent, showPage, controller):
        super().__init__(parent, fg_color="#EEEEEE")
        self.showPage = showPage
        self.controller = controller

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = ctk.CTkFrame(self, height=160, 
                              corner_radius=0, 
                              fg_color="#EEEEEE")
        header.grid(row=0, column=0, sticky="ew")
        header.grid_propagate(False)

        ctk.CTkLabel(header, 
                     text="New Plan", 
                     font=("Arial", 42, "bold"), 
                     text_color="black").pack(pady=(18, 10))

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

        content = ctk.CTkFrame(self, fg_color="transparent")
        content.grid(row=1, column=0, sticky="nsew")
        content.grid_columnconfigure(0, weight=1)

        form = ctk.CTkFrame(content, fg_color="transparent")
        form.grid(row=0, column=0, sticky="n", pady=(10, 0))

        FORM_W = 280

        def label(text, r, top=10):
            ctk.CTkLabel(
                form, text=text,
                font=("Arial", 14, "bold"),
                text_color="black"
            ).grid(row=r, column=0, sticky="w", padx=0, pady=(top, 4))

        def entry(widget, r):
            widget.configure(width=FORM_W, height=34, corner_radius=6)
            widget.grid(row=r, column=0, sticky="w")

        label("Goal", 0, top=6)
        self.ent_name = ctk.CTkEntry(form, 
                                     placeholder_text="name",
                                     fg_color="white",
                                     border_color="white")
        entry(self.ent_name, 1)

        label("Price", 2, top=14)
        self.ent_target = ctk.CTkEntry(form, 
                                       placeholder_text="bath",
                                       fg_color="white",
                                       border_color="white")
        entry(self.ent_target, 3)

        label("Duration", 4, top=14)
        self.opt_duration = ctk.CTkOptionMenu(
            form,
            values=["1 month", "2 months", "3 months", "6 months", "12 months"],
            width=FORM_W,
            height=34,
            corner_radius=6,
            fg_color="#FFFFFF",
            button_color="#FFFFFF",
            button_hover_color="#FFFFFF",
            text_color="black",
        )
        self.opt_duration.set("1 month")
        self.opt_duration.grid(row=5, column=0, sticky="w")

        label("Priority", 6, top=14)
        self.opt_priority = ctk.CTkOptionMenu(
            form,
            values=["1", "2", "3", "4", "5"],
            width=FORM_W,
            height=34,
            corner_radius=6,
            fg_color="#FFFFFF",
            button_color="#FFFFFF",
            button_hover_color="#FFFFFF",
            text_color="black",
        )
        self.opt_priority.set("1")
        self.opt_priority.grid(row=7, column=0, sticky="w")

        self.err = ctk.CTkLabel(form, text="", text_color="red", font=("Arial", 12))
        self.err.grid(row=8, column=0, sticky="w", pady=(10, 0))

        self.btn_done = ctk.CTkButton(
            content,
            text="Save",
            width=160,
            height=44,
            corner_radius=12,
            fg_color="#0A1E4A",
            hover_color="#0A1E4A",
            text_color="white",
            font=("Arial", 18, "bold"),
            command=self.on_save
        )
        self.btn_done.grid(row=1, column=0, pady=(26, 0))

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

        duration_text = self.opt_duration.get()   
        priority_text = self.opt_priority.get()  

        if not name:
            self.err.configure(text="กรุณากรอกชื่อแผน")
            return

        try:
            target_val = float(target) if target else 0.0
        except ValueError:
            self.err.configure(text="กรุณากรอก Price เป็นตัวเลข")
            return

        try:
            duration_val = int(duration_text.split()[0])
        except Exception:
            duration_val = 0

        try:
            priority_val = int(priority_text)
        except Exception:
            priority_val = 1

        new_id = len(getattr(self.controller, "plans", [])) + 1
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
        self.err.configure(text="")

        self.showPage("home")


if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Test New Plan")
    root.geometry("390x740")
    root.resizable(False, False)

    class DummyController:
        def __init__(self):
            self.plans = []

    controller = DummyController()

    def showPage(name):
        print("go to page:", name)
        print("plans now:", controller.plans)

    page = pageNewplan(root, showPage, controller)
    page.pack(fill="both", expand=True)

    root.mainloop()