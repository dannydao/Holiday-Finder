import tkinter as tk
import finder as hc

# Creating GUI
window = tk.Tk()
window.title("Is it a U.S. Holiday?")
window.geometry("275x150")

# Sets window to non-resizables
window.resizable(False, False)

# Function to check holiday
def check_holiday():
    date_string = date_var.get()
    result = hc.check_holiday(date_string)
    holiday_msg.set(result)

# StringVar to hold the date input and message result
date_var = tk.StringVar()
holiday_msg = tk.StringVar()

# Label telling user to enter a date
date_label = tk.Label(window, text="Enter date (MM/DD): ")
# Entry field for inputing the date
entry1 = tk.Entry(window, textvariable=date_var)

# Button to check the input for US holidays
check_button = tk.Button(window, text="Is it a holiday?", command=check_holiday)

# Label to display holiday result
result = tk.Label(window, textvariable=holiday_msg, wraplength=250)

# Placing and positioning for labels, entry field, and button using grid layout
date_label.grid(row=0, column=0, pady=15, padx=7)
entry1.grid(row=0, column=1, pady=15)
check_button.grid(row=2, column=0, columnspan=2, pady=15)
result.grid(row=3, column=0, columnspan=2, pady=10)

# Run the main event loop
window.mainloop()