"""Tkinter GUI for the scientific calculator.

Run with: python3 gui.py
Uses only the Python standard library (tkinter, math) — no extra installs.
"""
import tkinter as tk
from tkinter import messagebox

from calculator import add, subtract, multiply, divide
from scientific import power, sqrt, log, sin, cos


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.resizable(False, False)

        self.expression = ""
        self.display_var = tk.StringVar()

        self._build_display()
        self._build_buttons()

    def _build_display(self):
        display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Consolas", 20),
            justify="right",
            bd=8,
            relief=tk.RIDGE,
        )
        display.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=6, pady=6)

    def _build_buttons(self):
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("sqrt", 1, 4),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("^", 2, 4),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("log", 3, 4),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3), ("sin", 4, 4),
            ("(", 5, 0), (")", 5, 1), ("=", 5, 2, 2), ("cos", 5, 4),
        ]
        for spec in buttons:
            text, row, col = spec[0], spec[1], spec[2]
            colspan = spec[3] if len(spec) > 3 else 1
            btn = tk.Button(
                self.root,
                text=text,
                width=6,
                height=2,
                font=("Consolas", 12),
                command=lambda t=text: self._on_press(t),
            )
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)

    def _on_press(self, key):
        if key == "C":
            self.expression = ""
        elif key == "=":
            self._evaluate()
            return
        elif key in ("sqrt", "log", "sin", "cos"):
            self.expression += f"{key}("
        elif key == "^":
            self.expression += "**"
        else:
            self.expression += key
        self.display_var.set(self.expression)

    def _evaluate(self):
        safe_names = {
            "sqrt": sqrt,
            "log": log,
            "sin": sin,
            "cos": cos,
        }
        try:
            result = eval(self.expression, {"__builtins__": {}}, safe_names)
            self.display_var.set(str(result))
            self.expression = str(result)
        except Exception:
            messagebox.showerror("Error", "Invalid expression")
            self.expression = ""
            self.display_var.set("")


def main():
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
