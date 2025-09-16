import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Scientific Calculator")
        self.master.geometry('500x800')  # Set window size
        self.master.configure(bg='lightblue')  # Set background color
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(self.master, text="Scientific Calculator", font=('Arial', 30, 'bold'), bg='lightblue', fg='white')
        title_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Update display area font size and styling
        self.display = tk.Entry(self.master, textvariable=self.result_var, font=('Arial', 28), justify='right', bg='white', fg='black')
        self.display.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='ew')

        # Bind keyboard input
        self.master.bind('<Key>', self.on_key_press)

        # Create a grid layout for buttons
        self.button_frame = tk.Frame(self.master)
        self.button_frame.grid(row=2, column=0, columnspan=4)

        # Define button layout
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('C', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('sin', 4, 0), ('cos', 4, 1), ('tan', 4, 2), ('sqrt', 4, 3),
            ('exp', 5, 0), ('ln', 5, 1), ('log10', 5, 2), ('^', 5, 3),
            ('.', 6, 0)
        ]

        # Update button styling for readability
        for (text, row, column) in buttons:
            button = tk.Button(self.button_frame, text=text, width=6, height=3,
                               bg='lightgreen', fg='black', font=('Arial', 16), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, padx=10, pady=10)

        self.button_frame.grid_columnconfigure(0, weight=1)
        self.button_frame.grid_columnconfigure(1, weight=1)
        self.button_frame.grid_columnconfigure(2, weight=1)
        self.button_frame.grid_columnconfigure(3, weight=1)
        for i in range(7):
            self.button_frame.grid_rowconfigure(i, weight=1)

    def on_key_press(self, event):
        key = event.char
        if key in '0123456789+-*/.':
            self.result_var.set(self.result_var.get() + key)
        elif key == 'C':
            self.result_var.set('')
        elif key == '\r':  # Enter key
            self.calculate_result()
        elif key == '\b':  # Backspace key
            current_text = self.result_var.get()
            self.result_var.set(current_text[:-1])

    def on_button_click(self, char):
        if char == 'C':
            self.result_var.set('')
        elif char == '=':
            self.calculate_result()
        elif char in ['sin', 'cos', 'tan']:
            current_text = self.result_var.get()
            try:
                angle = float(current_text)
                if char == 'sin':
                    result = math.sin(math.radians(angle))
                elif char == 'cos':
                    result = math.cos(math.radians(angle))
                elif char == 'tan':
                    result = math.tan(math.radians(angle))

                self.result_var.set(result)
            except ValueError:
                messagebox.showerror("Error", "Invalid angle input")
                self.result_var.set('')
        elif char == 'sqrt':
            current_text = self.result_var.get()
            try:
                result = math.sqrt(float(current_text))
                self.result_var.set(result)
            except ValueError:
                messagebox.showerror("Error", "Invalid input for square root")
                self.result_var.set('')
        elif char == 'exp':
            current_text = self.result_var.get()
            try:
                result = math.exp(float(current_text))
                self.result_var.set(result)
            except ValueError:
                messagebox.showerror("Error", "Invalid input for exponential")
                self.result_var.set('')
        elif char == 'ln':
            current_text = self.result_var.get()
            try:
                result = math.log(float(current_text))
                self.result_var.set(result)
            except ValueError:
                messagebox.showerror("Error", "Invalid input for natural logarithm")
                self.result_var.set('')
        elif char == 'log10':
            current_text = self.result_var.get()
            try:
                result = math.log10(float(current_text))
                self.result_var.set(result)
            except ValueError:
                messagebox.showerror("Error", "Invalid input for base-10 logarithm")
                self.result_var.set('')
        elif char == '^':
            current_text = self.result_var.get()
            self.result_var.set(current_text + '^')
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + char)

    def calculate_result(self):
        try:
            expression = self.result_var.get()
            if '^' in expression:
                base, exponent = expression.split('^')
                result = float(base) ** float(exponent)
            else:
                result = eval(expression)
            self.result_var.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid input")
            self.result_var.set('')

current_puzzle = None
level = 1

def start_game():
    global current_puzzle
    global level
    current_puzzle = generate_math_puzzle(level)
    puzzle_label.config(text=current_puzzle)
    answer_entry.delete(0, 'end')  # Clear previous answer
    answer_entry.focus()  # Set focus on answer entry

def game_loop():
    global current_puzzle
    global level
    answer = answer_entry.get()
    if check_answer(current_puzzle, answer):
        result_label.config(text="Correct! Moving to the next level.")
        level += 1
        start_game()
    else:
        result_label.config(text="Incorrect. Try again.")

def generate_math_puzzle(level):
    # Example of generating a math problem based on the level
    if level == 1:
        return "What is 2 + 2?"
    elif level == 2:
        return "What is 3 * 3?"
    elif level == 3:
        return "What is 10 - 4?"
    else:
        return f"Solve this math problem for level {level}: {level} + {level}"  # Placeholder for higher levels

def check_answer(puzzle, answer):
    # Example answer checking
    correct_answers = {"What is 2 + 2?": "4", "What is 3 * 3?": "9", "What is 10 - 4?": "6"}
    return answer == correct_answers.get(puzzle, "")

if __name__ == '__main__':
    root = tk.Tk()
    calculator = Calculator(root)

    puzzle_label = tk.Label(root, text="")
    puzzle_label.grid(row=8, column=0, columnspan=4)

    answer_entry = tk.Entry(root)
    answer_entry.grid(row=9, column=0, columnspan=4)

    submit_button = tk.Button(root, text="Submit", command=game_loop)
    submit_button.grid(row=10, column=0, columnspan=4)

    result_label = tk.Label(root, text="")
    result_label.grid(row=11, column=0, columnspan=4)

    start_game()
    root.mainloop()
