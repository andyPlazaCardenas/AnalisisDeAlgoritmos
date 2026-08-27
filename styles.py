import tkinter as tk
from tkinter import ttk

class Theme:
    PALETTE = {
        "base": "#24273a",
        "mantle": "#1e2030",
        "crust": "#181926",
        "surface0": "#363a4f",
        "surface1": "#494d64",
        "surface2": "#5b6078",
        "text": "#cad3f5",
        "subtext": "#a5adce",
        "mauve": "#cba6f7",
        "pink": "#f5bde6",
        "red": "#ed8796",
        "peach": "#f5a97f",
        "yellow": "#eed49f",
        "green": "#a6da95",
        "teal": "#8bd5ca",
        "blue": "#8aadf4",
        "sky": "#91d7e3",
        "lavender": "#babbf1",
    }

    def __init__(self, root: tk.Tk, font_family: str = "Menlo"):
        self.root = root
        self.font = font_family
        self.style = ttk.Style()
        self.apply()

    def apply(self):
        c = self.PALETTE
        
        self.root.config(bg=c["base"])
        self.style.theme_use("clam")
        
        self.style.configure(
            ".",
            background=c["base"],
            foreground=c["text"],
            font=(self.font, 10),
            troughcolor=c["mantle"],
            focuscolor=c["mauve"],
        )

        self.style.configure("TFrame", background=c["base"])
        self.style.configure("Mantle.TFrame", background=c["mantle"])
        self.style.configure("TLabelframe", background=c["base"], bordercolor=c["surface0"])
        self.style.configure("TLabelframe.Label", background=c["base"], foreground=c["mauve"], font=(self.font, 10, "bold"))

        self.style.configure("TLabel", background=c["base"], foreground=c["text"])
        self.style.configure("Title.TLabel", foreground=c["yellow"], font=(self.font, 16, "bold"))
        self.style.configure("Header.TLabel", foreground=c["blue"], font=(self.font, 12, "bold"))
        self.style.configure("Sub.TLabel", foreground=c["subtext"], font=(self.font, 9, "italic"))
        self.style.configure("Success.TLabel", foreground=c["green"])
        self.style.configure("Danger.TLabel", foreground=c["red"])

        self.style.configure(
            "TButton",
            background=c["surface0"],
            foreground=c["text"],
            font=(self.font, 10),
            borderwidth=0,
            padding=(10, 6),
        )
        self.style.map(
            "TButton",
            background=[("active", c["surface1"]), ("disabled", c["mantle"])],
            foreground=[("disabled", c["surface2"])],
        )

        self.style.configure("Primary.TButton", background=c["blue"], foreground=c["base"])
        self.style.map("Primary.TButton", background=[("active", c["mauve"])])

        self.style.configure("Danger.TButton", background=c["red"], foreground=c["base"])
        self.style.map("Danger.TButton", background=[("active", c["peach"])])

        self.style.configure("Success.TButton", background=c["green"], foreground=c["base"])
        self.style.map("Success.TButton", background=[("active", c["teal"])])

        self.style.configure(
            "TEntry",
            fieldbackground=c["mantle"],
            foreground=c["text"],
            insertcolor=c["text"],
            bordercolor=c["surface0"],
            padding=5,
        )
        self.style.map("TEntry", bordercolor=[("focus", c["mauve"])])

        self.style.configure(
            "TCombobox",
            fieldbackground=c["mantle"],
            background=c["surface0"],
            foreground=c["text"],
            darkcolor=c["base"],
            lightcolor=c["base"],
            arrowcolor=c["text"],
            padding=4,
        )
        self.style.map("TCombobox", fieldbackground=[("readonly", c["mantle"])])

        for widget in ("TCheckbutton", "TRadiobutton"):
            self.style.configure(widget, background=c["base"], foreground=c["text"])
            self.style.map(
                widget,
                indicatorbackground=[("selected", c["mauve"]), ("active", c["surface0"])],
                foreground=[("active", c["mauve"])],
            )

        self.style.configure("TNotebook", background=c["base"], borderwidth=0)
        self.style.configure(
            "TNotebook.Tab",
            background=c["mantle"],
            foreground=c["subtext"],
            padding=(12, 6),
            borderwidth=0,
        )
        self.style.map(
            "TNotebook.Tab",
            background=[("selected", c["surface0"]), ("active", c["surface1"])],
            foreground=[("selected", c["mauve"]), ("active", c["text"])],
        )

        self.style.configure(
            "Treeview",
            background=c["base"],
            foreground=c["text"],
            fieldbackground=c["base"],
            rowheight=26,
            borderwidth=0,
        )
        self.style.map("Treeview", background=[("selected", c["surface0"])], foreground=[("selected", c["mauve"])])

        self.style.configure(
            "Treeview.Heading",
            background=c["mantle"],
            foreground=c["yellow"],
            font=(self.font, 10, "bold"),
            borderwidth=0,
            padding=4,
        )
        self.style.map("Treeview.Heading", background=[("active", c["surface0"])])

        self.style.configure(
            "TScrollbar",
            background=c["surface0"],
            troughcolor=c["mantle"],
            borderwidth=0,
            arrowcolor=c["text"],
            darkcolor=c["surface0"],
            lightcolor=c["surface0"]
        )
        self.style.map(
            "TScrollbar",
            background=[("active", c["surface1"]), ("disabled", c["mantle"])]
        )

        self.style.configure(
            "Vertical.TScrollbar",
            background=c["surface0"],
            troughcolor=c["mantle"],
            borderwidth=0,
            arrowcolor=c["text"],
            gripcount=0,
            darkcolor=c["surface0"],
            lightcolor=c["surface0"]
        )
        self.style.map(
            "Vertical.TScrollbar",
            background=[("active", c["surface1"]), ("disabled", c["mantle"])],
            arrowcolor=[("active", c["mauve"])]
        )