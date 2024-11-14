import tkinter as tk

def calculate():
    # Get values from entry fields
    try:
        first = float(first_number_entry.get())
        second = float(second_number_entry.get())
        operator = operator_entry.get()

        # Perform the calculation based on the operator
        if operator in ['+', '-', '*', '/']:
            if operator == '+':
                result = first + second
            elif operator == '-':
                result = first - second
            elif operator == '*':
                result = first * second
            elif operator == '/':
                if second != 0:
                    result = first / second
                else:
                    result = "Error: Division by zero is not allowed."
            
            # Display the result
            result_label.config(text=f"Result: {result}")
        else:
            result_label.config(text="Invalid operator! Please enter one of +, -, *, or /.")
    except ValueError:
        result_label.config(text="Invalid input! Please enter valid numbers.")

  # Display result
    result_display.delete(0, tk.END)  # Clear previous result
    result_display.insert(0, str(result))  # Show new result



window = tk.Tk()
window.title("Calculator")
window.geometry("400x300")

# Create input fields
first_number_entry = tk.Entry(window)
second_number_entry = tk.Entry(window)
operator_entry = tk.Entry(window)

# Create a button to perform calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)

# Create a label to display the result
result_label = tk.Label(window, text="Result: ")

# Layout the widgets
first_number_entry.pack(pady=5)
second_number_entry.pack(pady=5)
operator_entry.pack(pady=5)
calculate_button.pack(pady=10)
result_label.pack(pady=5)

# Run the main event loop
window.mainloop()