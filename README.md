# calculator.py

This module provides a minimal calculator backend and a small Tkinter-based GUI app. This module including this readme was completed with the help of AI tool (github copilot) using various
prompts. The way it was accomplish was - first I created calculator.py file in vs code. Then I imported math module, created calculator class and wrote a function to add, then ran my python
script, but it did not work. Then I asked copilot what I was trying to do and that it was not working. It generated codes and asked me either accept or reject. I accepted it, ran it and asked 
copilot again until I was satisfied with the final product.
Examples of prompt used: " I want to make a simple calculator, but looks like it is not working. Can you look into it?"

Contents
- `Calculator` — a minimal backend class with basic arithmetic methods:
  - `add(a, b)`
  - `subtract(a, b)`
  - `multiply(a, b)`
  - `divide(a, b)` — raises `ValueError` when dividing by zero.
- `CalculatorApp` — a simple Tkinter GUI that uses the `Calculator` backend.

Link to source: https://github.com/dipakaryal-msaai/dev-env/blob/b337872977c555c4ea027085d9f33a1de7405c4b/calculator.py

Requirements
- Python 3.7+
- tkinter (usually included with standard Python on Windows/macOS; on some Linux distributions install via package manager, e.g. `sudo apt install python3-tk`)
- A graphical display (or X forwarding / virtual framebuffer for headless environments)

Quick usage

1) Use the backend programmatically
```python
from calculator import Calculator

calc = Calculator()
print(calc.add(2, 3))        # 5
print(calc.subtract(7, 4))   # 3
print(calc.multiply(3, 5))   # 15
print(calc.divide(10, 2))    # 5.0

# division by zero raises ValueError
try:
    calc.divide(1, 0)
except ValueError as e:
    print("Error:", e)
```

2) Run the GUI from a Python script or interactive session
```python
import tkinter as tk
from calculator import CalculatorApp

root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()
```

If you prefer to run it from the command line, create a small launcher script (e.g. `run_calculator.py`) containing the snippet above and run:
```bash
python run_calculator.py
```

Notes & Behavior
- The `Calculator` class performs arithmetic on the provided numeric inputs (expects numbers). It does not coerce strings or non-numeric types — pass numeric values or convert inputs first.
- `divide(a, b)` raises `ValueError("Cannot divide by zero")` when `b == 0`.
- The GUI is intentionally minimal and intended for demonstration or as a starting point — feel free to extend with memory buttons, keyboard support, history, or improved input validation.

Testing ideas
- Unit tests for `Calculator` (e.g., using `pytest`):
  - Normal cases for each operation
  - Division by zero raises `ValueError`
  - Behavior with floats and negative numbers
- GUI tests can be manual or use a GUI automation tool for basic interactions.

Contributing
- Open a PR with enhancements or fixes.
- For GUI changes, keep accessibility and keyboard support in mind.
- If adding tests, include them in a `tests/` directory and document how to run them (e.g., `pytest`).

License
- No license is specified in this README. Add a LICENSE file to make usage/redistribution terms explicit.
