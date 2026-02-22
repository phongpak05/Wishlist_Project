import customtkinter as ctk

class planCard(ctk.CTkFrame):
    def __init__(self, master, name: str, percent: int, bar_color: str, command=None):
        super().__init__(master, corner_radius=12, fg_color="#D9D9D9")
        self.grid_columnconfigure(1, weight=1)

        color_box = ctk.CTkFrame(self, width=26, height=26, corner_radius=6, fg_color=bar_color)
        color_box.grid(row=0, column=0, padx=(12, 10), pady=12)
        color_box.grid_propagate(False)

        ctk.CTkLabel(self, 
                     text=name, 
                     text_color="black", 
                     font=("Arial", 14, "bold")
                     ).grid(row=0, column=1, sticky="w")

        ctk.CTkLabel(self, 
                     text=f"{percent}%", 
                     text_color="black", 
                     font=("Arial", 12)
                     ).grid(row=0, column=2, padx=(0, 10), sticky="e")

        ctk.CTkButton(self, text=">", 
                      width=28, 
                      height=28, 
                      corner_radius=8,
                      fg_color="#BFBFBF", 
                      text_color="black",
                      command=command
                      ).grid(row=0, column=3, padx=(0, 12))

        prog = ctk.CTkProgressBar(self, height=10)
        prog.grid(row=1, column=0, columnspan=4, padx=12, pady=(0, 12), sticky="ew")
        prog.set(max(0, min(percent, 100)) / 100)