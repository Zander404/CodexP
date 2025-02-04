import customtkinter as ctk
from customtkinter import *


class Shop(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Points Shop")
        self.geometry("300x300")
