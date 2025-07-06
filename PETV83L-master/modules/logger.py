from rich.console import Console
import tkinter as tk

class Logger:
    def __init__(self):
        self.console = Console()
        self.widget = None

    def log(self, message):
        self.console.print(message)
        if self.widget:
            self.widget.insert(tk.END, message + "\n")
            self.widget.see(tk.END)

    def bind_to_text_widget(self, widget):
        self.widget = widget

