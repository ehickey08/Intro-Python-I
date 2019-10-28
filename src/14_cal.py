"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime


def getmonth ( input ):
    if len(input) > 1:
        x = int(input[1])
        if x <= 12 and x >= 1:
            return x
        else:
            print("Month input needs to be between 1 and 12.")
            return datetime.today().month
    else:
        return datetime.today().month


def getyear(input):
    if(len(input) >2):
        x = int(input[2])
        return x
    else:
        return datetime.today().year

month = getmonth(sys.argv)
year = getyear(sys.argv)

if len(sys.argv) > 3:
    print(f"Only two arguments will be accepted: month and year(optional). "
          f"Month should be between 1 and 12. Year should be the four digit "
          f"year.")
else:
    print(calendar.month(year, month))
