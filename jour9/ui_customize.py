# Jour 9 — Personnalisation via config (taille, titre, couleur)
import tkinter as tk
from pathlib import Path

cfg = Path("../jour3/config.txt")
settings = {"title":"Mon App", "bg":"#222", "w":400, "h":250}

# Lire lignes optionnelles supplémentaires du config :
if cfg.exists():
    for line in cfg.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            k,v = line.split("=",1)
            if k in ("title","bg"):
                settings[k] = v
            elif k in ("w","h"):
                try: settings[k] = int(v)
                except: pass

root = tk.Tk()
root.title(settings["title"])
root.geometry(f'{settings["w"]}x{settings["h"]}')
root.configure(bg=settings["bg"])

tk.Label(root, text="Personnalise dans config.txt :", bg=settings["bg"], fg="white").pack(pady=10)
tk.Label(root, text="title=Mon App
bg=#334455
w=500
h=300", bg=settings["bg"], fg="white", justify="left").pack()

root.mainloop()