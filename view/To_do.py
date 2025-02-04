import customtkinter as ctk
from customtkinter import *


class Todo(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("TODO_LIST")
        self.geometry("300x300")
