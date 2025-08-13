# Jour 7 — Afficher une image et changer
import tkinter as tk

root = tk.Tk()
root.title("Image swap")

# PPM support natif pour PhotoImage
img1 = tk.PhotoImage(file="../assets/logo1.ppm")
img2 = tk.PhotoImage(file="../assets/logo2.ppm")
current = [img1]

label = tk.Label(root, image=current[0])
label.pack(padx=10, pady=10)

def toggle():
    current[0] = img2 if current[0] == img1 else img1
    label.configure(image=current[0])

tk.Button(root, text="Changer image", command=toggle).pack(pady=8)

root.mainloop()