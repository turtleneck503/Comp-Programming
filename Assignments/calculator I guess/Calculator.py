import tkinter as tk
from sympy import symbols, diff, sympify

window = tk.Tk()
window.title("Calculator")
window.geometry("400x600")

display = tk.Entry(window, width=20, font=('Arial', 24), borderwidth=5, justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_press(input):
    display.insert(tk.END, input)

def operation():
    try:      
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        display.delete(0, tk.END)
        display.insert(0, "SYNTAX ERROR")

def calculate_derivative():
    try:
        x = symbols('x')
        expression = display.get()
        expr = sympify(expression)
        derivative = diff(expr, x)
        display.delete(0, tk.END)
        display.insert(0, str(derivative))
    except:
        display.delete(0, tk.END)
        display.insert(0, "ERROR")

num_width = 10
operator_width = 15
height = 3

button_7 = tk.Button(window, text="7", width=num_width, height=height, command=lambda: button_press(7))
button_7.grid(row=1, column=0)

button_8 = tk.Button(window, text="8", width=num_width, height=height, command=lambda: button_press(8))
button_8.grid(row=1, column=1)

button_9 = tk.Button(window, text="9", width=num_width, height=height, command=lambda: button_press(9))
button_9.grid(row=1, column=2)

button_add = tk.Button(window, text="+", width=operator_width, height=height, command=lambda: button_press(" + "))
button_add.grid(row=1, column=3)

button_4 = tk.Button(window, text="4", width=num_width, height=height, command=lambda: button_press(4))
button_4.grid(row=2, column=0)

button_5 = tk.Button(window, text="5", width=num_width, height=height, command=lambda: button_press(5))
button_5.grid(row=2, column=1)

button_6 = tk.Button(window, text="6", width=num_width, height=height, command=lambda: button_press(6))
button_6.grid(row=2, column=2)

button_subtract = tk.Button(window, text="-", width=operator_width, height=height, command=lambda: button_press(" - "))
button_subtract.grid(row=2, column=3)

button_1 = tk.Button(window, text="1", width=num_width, height=height, command=lambda: button_press(1))
button_1.grid(row=3, column=0)

button_2 = tk.Button(window, text="2", width=num_width, height=height, command=lambda: button_press(2))
button_2.grid(row=3, column=1)

button_3 = tk.Button(window, text="3", width=num_width, height=height, command=lambda: button_press(3))
button_3.grid(row=3, column=2)

button_multiply = tk.Button(window, text="×", width=operator_width, height=height, command=lambda: button_press("*"))
button_multiply.grid(row=3, column=3)

button_decimal = tk.Button(window, text=".", width=num_width, height=height, command=lambda: button_press("."))
button_decimal.grid(row=4, column=0)

button_0 = tk.Button(window, text="0", width=num_width, height=height, command=lambda: button_press(0))
button_0.grid(row=4, column=1)

button_x = tk.Button(window, text="x", width=num_width, height=height, command=lambda: button_press("x"))
button_x.grid(row=4, column=2)

button_divide = tk.Button(window, text="÷", width=operator_width, height=height, command=lambda: button_press("/"))
button_divide.grid(row=4, column=3)

button_power = tk.Button(window, text="^", width=num_width, height=height, command=lambda: button_press("**"))
button_power.grid(row=5, column=0)

button_y = tk.Button(window, text="y", width=num_width, height=height, command=lambda: button_press("y"))
button_y.grid(row=5, column=1)

button_clear = tk.Button(window, text="C", width=num_width, height=height, command=lambda: display.delete(0, tk.END))
button_clear.grid(row=5, column=2)

button_equal = tk.Button(window, text="=", width=operator_width, height=height, command=operation)
button_equal.grid(row=5, column=3)

button_derivative = tk.Button(window, text="d/dx", width=operator_width, height=height, command=calculate_derivative)
button_derivative.grid(row=6, column=0, columnspan=2)

window.mainloop()