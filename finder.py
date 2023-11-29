from datetime import datetime
import holidays

# Fetch US holidays
us_holidays = holidays.US()

# Function to check if the date entered is a US holiday
def check_holiday(date_string):
    try:
        # Parsing input date string into a datetime object (Month and Day only)
        input_date = datetime.strptime(date_string, "%m/%d")

        # Validating if the date entered is a US holiday
        if input_date in us_holidays:
            # If the date entered is a holiday, return this message
            return f"This date is a holiday: {us_holidays[input_date]}."
        else:
            # If the date entered is not a holiday, return this message 
            return "This date is not a holiday. Try a different date."
    except ValueError:
        # Invalid date entries will return this message
        return "Enter a valid date. (Format: MM/DD)"