# Jour 6 — UI lit/écrit config.txt
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

cfg = Path("../jour3/config.txt")
if not cfg.exists():
    cfg.write_text("username=Alex
", encoding="utf-8")

def load_username():
    text = cfg.read_text(encoding="utf-8").strip()
    return text.split("=",1)[1] if "=" in text else ""

def save_username():
    name = entry.get().strip() or "Alex"
    cfg.write_text(f"username={name}\n", encoding="utf-8")
    messagebox.showinfo("OK", "Sauvegardé.")

root = tk.Tk()
root.title("Config simple")

tk.Label(root, text="Username").pack()
entry = tk.Entry(root)
entry.insert(0, load_username())
entry.pack(padx=10, pady=5)

tk.Button(root, text="Sauvegarder", command=save_username).pack(pady=8)

root.mainloop()