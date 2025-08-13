# Jour 10 — UI finale (config + image + animation)
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

# --- Config ---
cfg = Path("../jour3/config.txt")
if not cfg.exists():
    cfg.write_text("username=Alex
", encoding="utf-8")

def read_username():
    line = cfg.read_text(encoding="utf-8").splitlines()[0]
    return line.split("=",1)[1] if "=" in line else "Alex"

def save_username():
    name = entry_name.get().strip() or "Alex"
    lines = cfg.read_text(encoding="utf-8").splitlines()
    lines = [l for l in lines if not l.startswith("username=")]
    lines.insert(0, f"username={name}")
    cfg.write_text("\n".join(lines)+"\n", encoding="utf-8")
    messagebox.showinfo("OK", "Username sauvegardé.")

# --- UI ---
root = tk.Tk()
root.title("Projet final")

# Frame config
frame_cfg = tk.LabelFrame(root, text="Config")
frame_cfg.grid(row=0, column=0, padx=10, pady=10, sticky="n")

tk.Label(frame_cfg, text="Username").grid(row=0, column=0, sticky="e")
entry_name = tk.Entry(frame_cfg, width=18)
entry_name.insert(0, read_username())
entry_name.grid(row=0, column=1, padx=4)
tk.Button(frame_cfg, text="Sauver", command=save_username).grid(row=1, column=0, columnspan=2, pady=6)

# Frame image
frame_img = tk.LabelFrame(root, text="Image")
frame_img.grid(row=0, column=1, padx=10, pady=10, sticky="n")

img1 = tk.PhotoImage(file="../assets/logo1.ppm")
img2 = tk.PhotoImage(file="../assets/logo2.ppm")
current = [img1]
lbl_img = tk.Label(frame_img, image=current[0])
lbl_img.pack(padx=6, pady=6)

def toggle_img():
    current[0] = img2 if current[0] == img1 else img1
    lbl_img.configure(image=current[0])

tk.Button(frame_img, text="Changer image", command=toggle_img).pack(pady=4)

# Frame Drone
frame_drone = tk.LabelFrame(root, text="Drone (simulation)")
frame_drone.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

canvas = tk.Canvas(frame_drone, width=320, height=120)
canvas.pack(padx=6, pady=6)
drone = canvas.create_oval(10, 50, 40, 80)
vx = [3]
flying = [False]

def animate():
    if flying[0]:
        canvas.move(drone, vx[0], 0)
        x1,y1,x2,y2 = canvas.coords(drone)
        if x2 > 320 or x1 < 0:
            vx[0] *= -1
        root.after(30, animate)

def takeoff():
    flying[0] = True
    animate()

def land():
    flying[0] = False

tk.Button(frame_drone, text="Décoller", command=takeoff).pack(side="left", padx=6)
tk.Button(frame_drone, text="Atterrir", command=land).pack(side="left", padx=6)

root.mainloop()