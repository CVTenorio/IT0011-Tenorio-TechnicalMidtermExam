# Carl Vincent Tenorio TW24 Date Program
"""
INSTRUCTIONS:
Create a program that will translate a given date format in mm/dd/yyyy to more human readable
format like January 1, 2023
Example Output
Enter the date (mm/dd/yyyy): 02/02/2023
Date Output: February 2, 2023
"""

from datetime import datetime

def convertMo_date(date_strDaw):
    try:
        date_obj = datetime.strptime(date_strDaw, "%m/%d/%Y")
        formattedDaw_date = date_obj.strftime("%B %d, %Y")
        print(f"Date Output: {formattedDaw_date}")
    except ValueError:
        print("Invalid date format. Please enter the date in mm/dd/yyyy format.")

def main():
    lagayMoDate = input("Enter the date (mm/dd/yyyy): ")
    convertMo_date(lagayMoDate)

if __name__ == "__main__":
    main()