# Jour 8 — Animation simple (simulation drone)
import tkinter as tk

root = tk.Tk()
root.title("Drone Sim")

canvas = tk.Canvas(root, width=300, height=150)
canvas.pack(padx=10, pady=10)
drone = canvas.create_oval(10, 60, 40, 90)

vx = 3
flying = [False]

def takeoff():
    flying[0] = True
    animate()

def land():
    flying[0] = False

def animate():
    if flying[0]:
        canvas.move(drone, vx, 0)
        x1, y1, x2, y2 = canvas.coords(drone)
        if x2 > 300 or x1 < 0:
            nonlocal_vx[0] *= -1
        root.after(30, animate)

nonlocal_vx = [vx]

tk.Button(root, text="Décoller", command=takeoff).pack(side="left", padx=10)
tk.Button(root, text="Atterrir", command=land).pack(side="left", padx=10)

root.mainloop()