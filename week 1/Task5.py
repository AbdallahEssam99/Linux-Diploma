import calendar

def print_month_calendar():
    # Get user input for year and month
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))

    # Check if the month input is valid
    if 1 <= month <= 12:
        # Print the calendar for the given month and year
        print("\n", calendar.month(year, month))
    else:
        print("Invalid month. Please enter a number between 1 and 12.")


print_month_calendar()