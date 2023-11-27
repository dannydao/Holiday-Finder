import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import holidays

# Fetch US holidays
us_holidays = holidays.US()

# Function to check if the date entered is a US holiday
def check_holiday():
    # Getting input from the entry field
    date_string = date_var.get()
    try:
        # Parsing input date string into a datetime object (Month and Day only)
        input_date = datetime.strptime(date_string, "%m/%d")

        # Validating if the date entered is a US holiday
        if input_date in us_holidays:
            # If the date entered is a holiday, this pop up message will appear
            messagebox.showinfo("This date is a holiday", f"Holiday: {us_holidays[input_date]}")
        else:
            # If the date entered is not a holiday, this pop up message will appear
            messagebox.showinfo("This date is not a holiday", "Try a different date")
    except ValueError:
        # Invalid date entries will return this popup message
        messagebox.showerror("Invalid Date", "Enter a valid date (Format: MM/DD)")


# Creating GUI
window = tk.Tk()
window.title("Is it a U.S. Holiday?")
window.geometry("275x150")

# Sets window to non-resizables
window.resizable(False, False)

# StringVar to hold the date input
date_var = tk.StringVar()

# Label telling user to enter a date
date_label = tk.Label(window, text="Enter date (MM/DD): ")
# Entry field for inputing the date
entry1 = tk.Entry(window, textvariable=date_var)

# Button to check the input for US holidays
check_button = tk.Button(window, text="Is it a holiday?", command=check_holiday)

# Placing and positioning for labels, entry field, and button using grid layout
date_label.grid(row=0,column=0, pady=10)
entry1.grid(row=0, column=1, pady=10)
check_button.grid(row=2,column=0,columnspan=2, pady=15)

# Run the main event loop
window.mainloop()