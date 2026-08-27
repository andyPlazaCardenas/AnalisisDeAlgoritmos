import tkinter as tk
from tkinter import ttk
from styles import Theme 

root = tk.Tk()
root.title("GUI Test")
root.geometry("400x450")

theme = Theme(root, font_family="Menlo")

frame = ttk.Frame(root, style="TFrame")
frame.pack(fill="both", expand=True)

label = ttk.Label(frame, text="Escribe tu nombre.", style="Title.TLabel")
label.pack(pady=40)

entry = ttk.Entry(frame)
entry.pack(pady=10)

def onClick():
    nombre = entry.get().strip()
    if not nombre:
        nombre = "Andy"
    label.config(text=f"Hola, {nombre}")

button = ttk.Button(frame, text="Saludar", command=onClick, style="Primary.TButton")
button.pack(pady=20)

root.mainloop()