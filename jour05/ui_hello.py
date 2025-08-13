# Jour 5 — Fenêtre Tkinter + boutons
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Bonjour")

def say_hi():
    messagebox.showinfo("Salut", "Hello 👋")

tk.Button(root, text="Dire bonjour", command=say_hi).pack(padx=10, pady=10)
tk.Button(root, text="Quitter", command=root.destroy).pack(padx=10, pady=10)

root.mainloop()