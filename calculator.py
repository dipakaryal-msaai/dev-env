# impoert math module for advanced mathematical operations
import math


# Simple calculator class
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


# Calculator class with basic operations
class CalculatorApp:
    def __init__(self, root):
        import tkinter as tk
        from tkinter import messagebox
        self.tk = tk
        self.messagebox = messagebox
        self.calculator = Calculator()
        self.root = root
        self.root.title("Simple Calculator")
        self.current_input = ""
        self.selected_operation = None

        # Display
        self.display = tk.Entry(root, font=("Arial", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipady=10)

        # Number buttons (0-9)
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
            ("0", 4, 1), (".", 4, 0),
        ]
        
        for (text, row, col) in buttons:
            btn = tk.Button(root, text=text, font=("Arial", 18), 
                           command=lambda t=text: self.on_number_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Operation buttons
        self.add_button = tk.Button(root, text="+", font=("Arial", 18), 
                                   command=lambda: self.on_operation("+"))
        self.add_button.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

        self.subtract_button = tk.Button(root, text="-", font=("Arial", 18), 
                                        command=lambda: self.on_operation("-"))
        self.subtract_button.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

        self.multiply_button = tk.Button(root, text="*", font=("Arial", 18), 
                                        command=lambda: self.on_operation("*"))
        self.multiply_button.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

        self.divide_button = tk.Button(root, text="/", font=("Arial", 18), 
                                      command=lambda: self.on_operation("/"))
        self.divide_button.grid(row=4, column=3, padx=5, pady=5, sticky="nsew")

        # Equals button
        self.equals_button = tk.Button(root, text="=", font=("Arial", 18), 
                                      command=self.on_equals)
        self.equals_button.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

        # Clear button
        self.clear_button = tk.Button(root, text="C", font=("Arial", 18), 
                                     command=self.on_clear)
        self.clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        # Configure grid weights for resizing
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def get_inputs(self):
        try:
            a = float(self.entry1.get())
            b = float(self.entry2.get())
            return a, b
        except ValueError:
            self.messagebox.showerror("Input Error", "Please enter valid numbers.")
            return None, None

    def on_number_click(self, num):
        self.current_input += str(num)
        self.display.delete(0, self.tk.END)
        self.display.insert(0, self.current_input)

    def on_operation(self, op):
        if self.current_input:
            self.selected_operation = op
            self.first_number = float(self.current_input)
            self.current_input = ""
            self.display.delete(0, self.tk.END)
            self.display.insert(0, f"{self.first_number} {op}")

    def on_equals(self):
        if self.selected_operation and self.current_input:
            try:
                second_number = float(self.current_input)
                if self.selected_operation == "+":
                    result = self.calculator.add(self.first_number, second_number)
                elif self.selected_operation == "-":
                    result = self.calculator.subtract(self.first_number, second_number)
                elif self.selected_operation == "*":
                    result = self.calculator.multiply(self.first_number, second_number)
                elif self.selected_operation == "/":
                    result = self.calculator.divide(self.first_number, second_number)
                
                self.display.delete(0, self.tk.END)
                self.display.insert(0, str(result))
                self.current_input = str(result)
                self.selected_operation = None
            except ValueError as e:
                self.messagebox.showerror("Math Error", str(e))
                self.on_clear()

    def on_clear(self):
        self.current_input = ""
        self.selected_operation = None
        self.display.delete(0, self.tk.END)

    def add(self):
        a, b = self.get_inputs()
        if a is not None and b is not None:
            result = self.calculator.add(a, b)
            self.result_label.config(text=f"Result: {result}")

    def subtract(self):
        a, b = self.get_inputs()
        if a is not None and b is not None:
            result = self.calculator.subtract(a, b)
            self.result_label.config(text=f"Result: {result}")

    def multiply(self):
        a, b = self.get_inputs()
        if a is not None and b is not None:
            result = self.calculator.multiply(a, b)
            self.result_label.config(text=f"Result: {result}")

    def divide(self):
        a, b = self.get_inputs()
        if a is not None and b is not None:
            try:
                result = self.calculator.divide(a, b)
                self.result_label.config(text=f"Result: {result}")
            except ValueError as e:
                self.messagebox.showerror("Math Error", str(e))


if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()