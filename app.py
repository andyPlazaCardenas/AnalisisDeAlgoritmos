import tkinter as tk

root = tk.Tk()
root.title("GUI Test")
root.geometry("400x200")

label = tk.Label(root, text="Hello world.", font=("monospace", 16))
label.pack(pady=20)

def onClick():
    label.config(text="Button Clicked!")

button = tk.Button(root, text="Click Me", command=onClick)
button.pack()

root.mainloop()