import tkinter as tk
from menu import create_bottom_nav

class homePage(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent, bg="#d9d9d9")

        title_font = ("Segoe UI", 26, "bold")
        card_big_font = ("Helvetica", 16, "bold")
        card_small_font = ("Helvetica", 10)

        title_label = tk.Label(self, text="Home",
                               font=title_font,
                               bg="#d9d9d9")
        title_label.place(relx=0.5, rely=0.3, anchor="center")
        
    

        create_bottom_nav(self)
        



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("390x740")
    root.resizable(False,False)
    page = homePage(root)
    page.pack(fill="both", expand=True)
    root.mainloop()