import random
import tkinter as tk
from tkinter import ttk
from styles import Theme

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr 


class SortingApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Generador")
        self.geometry("700x700")
        self.theme = Theme(self, font_family="Menlo")

        self.arrays = []

        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self)
        self.frame.pack(fill="x", padx=15, pady=10)

        self.title_lbl = ttk.Label(
            self.frame,
            text="Generador de Arreglos Ordenados",
            style="Title.TLabel",
        )
        self.title_lbl.grid(row=0, column=0, columnspan=2, pady=15, padx=5)

        self.lblStart = ttk.Label(
            self.frame,
            text="Arreglo Inicial: ",
            anchor="w",
            width=15,
            style="Header.TLabel",
        )
        self.lblStart.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.startEntry = ttk.Entry(self.frame)
        self.startEntry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.lblIncrement = ttk.Label(
            self.frame,
            text="Incremento:",
            anchor="w",
            width=15,
            style="Header.TLabel",
        )
        self.lblIncrement.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.incEntry = ttk.Entry(self.frame)
        self.incEntry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.lblLimit = ttk.Label(
            self.frame, text="Limite:", anchor="w", width=15, style="Header.TLabel"
        )
        self.lblLimit.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.limitEntry = ttk.Entry(self.frame)
        self.limitEntry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.generatorBtn = ttk.Button(
            self.frame,
            text="Generar Arreglos",
            command=self.GenerateArrays,
            style="Primary.TButton",
        )
        self.generatorBtn.grid(
            row=4, column=0, columnspan=2, padx=5, pady=15, sticky="w"
        )

        self.sorterBtn = ttk.Button(
            self.frame,
            text="Ordenar Arreglos",
            command=self.SortArrays,
            style="Primary.TButton",
        )
        self.sorterBtn.grid(
            row=4, column=1, columnspan=2, padx=5, pady=15, sticky="e"
        )

        self.frame.columnconfigure(1, weight=1)

        self.containerFrame = ttk.Frame(self, style="Mantle.TFrame")
        self.containerFrame.pack(
            fill="both", expand=True, padx=15, pady=(0, 15)
        )

        self.scrollbar = ttk.Scrollbar(self.containerFrame, orient="vertical", style="TScrollbar")
        self.scrollbar.pack(side="right", fill="y")

        self.canvas = tk.Canvas(
            self.containerFrame,
            highlightthickness=0,
            bg=Theme.PALETTE["mantle"],
            yscrollcommand=self.scrollbar.set,
        )
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.config(command=self.canvas.yview)

        self.unorderedArrayFrame = ttk.Frame(
            self.canvas, style="Mantle.TFrame"
        )
        self.canvas_window = self.canvas.create_window(
            (0, 0), window=self.unorderedArrayFrame, anchor="nw"
        )

    def ClearDisplay(self):
        for child in self.unorderedArrayFrame.winfo_children():
            child.destroy()

    def RenderArrays(self):
        self.ClearDisplay()

        for i, array in enumerate(self.arrays):
            lbl = ttk.Label(
                self.unorderedArrayFrame,
                text=f"{array}",
                anchor="w",
                style="Sub.TLabel",
                wraplength=650,
            )
            lbl.grid(row=i, column=0, sticky="ew", padx=10, pady=5)

        self.unorderedArrayFrame.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def GenerateArrays(self):
        try:
            start = int(self.startEntry.get())
            increment = int(self.incEntry.get())
            limit = int(self.limitEntry.get())
        except ValueError:
            return

        self.arrays = [[random.randint(0, 100) for _ in range(size)]for size in range(start, limit + 1, increment)]

        self.RenderArrays()

    def SortArrays(self):
        if not self.arrays:
            return

        for array in self.arrays:
            bubbleSort(array)

        self.RenderArrays()


if __name__ == "__main__":
    app = SortingApp()
    app.mainloop()