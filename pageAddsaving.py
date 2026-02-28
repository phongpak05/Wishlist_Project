import customtkinter as ctk
from menu import create_bottom_nav

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class pageAddsaving(ctk.CTkFrame):
    def __init__(self, master, showPage, controller):
        super().__init__(master, fg_color="#F5F5F5")
        self.showPage = showPage
        self.controller = controller

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        header = ctk.CTkFrame(self, height=160, corner_radius=0, fg_color="#F5F5F5")
        header.grid(row=0, column=0, sticky="ew")
        header.grid_propagate(False)


        ctk.CTkButton(
            header,
            text="‹",
            width=36,
            height=36,
            fg_color="transparent",
            hover=False,
            text_color="black",
            font=("Arial", 28, "bold"),
            command=lambda: self.showPage("detailhome"),
        ).place(x=14, y=18)

        ctk.CTkLabel(header, 
                     text="Add Saving", 
                     font=("Arial", 42, "bold"), 
                     text_color="black"
                     ).pack(pady=(18, 10))
        
        content = ctk.CTkFrame(self, fg_color="transparent")
        content.grid(row=1, column=0, sticky="nsew")

        form_frame = ctk.CTkFrame(content, fg_color="transparent")
        form_frame.pack(pady=20)

        income_label = ctk.CTkLabel(
            form_frame,
            text="Income",
            font=("Arial", 12),
            text_color="#444"
        )
        income_label.pack(anchor="w", padx=5)

        self.income_entry = ctk.CTkEntry(
            form_frame,
            font=("Arial", 12),
            width=280,
            fg_color="#DDDDDD",
            border_width=0
        )
        self.income_entry.pack(pady=5, ipady=6)

        save_btn = ctk.CTkButton(
            content,
            text="Save",
            command=self.save,
            font=("Arial", 12, "bold"),
            fg_color="#1E7D22",
            hover_color="#16651A",
            text_color="white",
            width=160,
            height=40
        )
        save_btn.pack(pady=20)

        footer = ctk.CTkFrame(
                self,
                height=80,
                corner_radius=0,
                fg_color="transparent"
                )
        footer.grid(row=2, column=0, sticky="ew")
        footer.grid_propagate(False)

        create_bottom_nav(footer, self.showPage)

    def save(self):
        print("Saved:", self.income_entry.get())


if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Saving App")
    app.geometry("390x740")
    app.resizable(False, False)

    page = pageAddsaving(app, None, None)
    page.pack(fill="both", expand=True)

    app.mainloop()