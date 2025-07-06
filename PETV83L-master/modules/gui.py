import tkinter as tk
from tkinter import ttk
from modules.attack_engine import start_attack
from modules.logger import Logger

class WiFiSimGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("WiFi Attack Simulator Pro")
        self.root.geometry("800x600")

        self.logger = Logger()

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        self.create_tabs()

    def create_tabs(self):
        tabs = {
            "Rogue AP": self.simulate_rogue_ap,
            "Deauth Attack": self.simulate_deauth,
            "Password Crack": self.simulate_crack,
            "Live Terminal": self.show_logs
        }

        for name, func in tabs.items():
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=name)
            func(frame)

    def simulate_rogue_ap(self, frame):
        tk.Label(frame, text="Rogue AP Simulation").pack()
        tk.Button(frame, text="Start", command=lambda: start_attack("rogue", self.logger)).pack()

    def simulate_deauth(self, frame):
        tk.Label(frame, text="Deauthentication Attack").pack()
        tk.Button(frame, text="Start", command=lambda: start_attack("deauth", self.logger)).pack()

    def simulate_crack(self, frame):
        tk.Label(frame, text="Password Cracking Simulation").pack()
        tk.Button(frame, text="Start", command=lambda: start_attack("crack", self.logger)).pack()

    def show_logs(self, frame):
        text = tk.Text(frame, bg="black", fg="lime", insertbackground="lime")
        text.pack(expand=True, fill="both")
        self.logger.bind_to_text_widget(text)
