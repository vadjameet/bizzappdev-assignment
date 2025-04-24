"""
Problem: Date Difference Calculator
Approach: Use datetime module for date parsing and calculation.
"""
from datetime import datetime

def date_diff(start_date, end_date):
    fmt = "%d-%m-%Y"
    date1 = datetime.strptime(start_date, fmt)
    date2 = datetime.strptime(end_date, fmt)
    delta = date2 - date1
    return abs(delta.days)

# Example usage:
if __name__ == "__main__":
    birth_date = input("Enter birthdate (dd-mm-yyyy): ")
    today_date = input("Enter today's date (dd-mm-yyyy): ")
    print("Days lived:", date_diff(birth_date, today_date))