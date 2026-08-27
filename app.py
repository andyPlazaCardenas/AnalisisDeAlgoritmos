import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')  # Tell Matplotlib to use Tkinter's engine
import matplotlib.pyplot as plt

x = [3]
y = [10]

plt.plot(x,y)
plt.scatter(x,y)
plt.title("Grafica")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

root = tk.Tk()
root.title("GUI Test")
root.geometry("400x200")

label = tk.Label(root, text="Escribe tu nombre.", font=("Menlo", 16))
label.pack(pady=20)

entry = tk.Entry(root)
entry.pack(pady=20)

def onClick():
    nombre = entry.get().strip()
    if not nombre:
        nombre = "mundo"
    label.config(text=f"Hola, {nombre}")

button = tk.Button(root, text="Saludar", command=onClick)
button.pack()

root.mainloop()