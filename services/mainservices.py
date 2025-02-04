from customtkinter import CTk
from view.To_do import Todo
from view.Shop import Shop


def open_toplevel(self, window: str):
    if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
        if window == "todo":
            self.toplevel_window = Todo(self)

        elif window == "shop":
            # create window if its None or destroyed
            self.toplevel_window = Shop(self)

    else:
        self.toplevel_window.focus()  # if window exists focus it
