import customtkinter as ctk
from customtkinter import *
from services.mainservices import *


class Main(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window Controller
        self.title("Main Page")
        self.geometry("300x300")
        label = CTkLabel(self, text="Main Page", )
        label.pack(padx=50, pady=50)

        self.toplevel_window = None

        # Component
        todo_btn = CTkButton(
            self, 30, 30, 20, text="TODO",  command=lambda: open_toplevel(self=self, window="todo"))
        shop_btn = CTkButton(
            self, 30, 30, 20, text="SHOP", command=lambda: open_toplevel(self=self, window="todo"))
        close_btn = CTkButton(self, 30, 30, 20, text="EXIT",
                              command=lambda: self.destroy())

        component = [
            todo_btn,
            shop_btn,
            close_btn
        ]

        for item in component:
            item.pack(padx=10, pady=50)
