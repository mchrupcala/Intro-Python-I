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
import time
import calendar
from datetime import datetime

userinput = sys.argv
monthdict = {
  "Jan": 1,
"Feb": 2,
"Mar": 3,
"Apr": 4,
"May": 5,
"Jun": 6,
"Jul": 7,
"Aug": 8,
"Sep": 9,
"Oct": 10,
"Nov": 11,
"Dec": 12
}
# userinput = str(input("Please enter a filename, month, and year: "))
# def calfunc(file, month=datetime.date.month, year=datetime.date.year):
def calfunc(args):

  if len(args) == 1:
    print(calendar.TextCalendar().formatmonth(datetime.now().year, datetime.now().month))
  elif len(args) == 2:
    print(calendar.TextCalendar().formatmonth(datetime.now().year, monthdict[args[1]]))
  elif len(args) == 3:
    print(calendar.TextCalendar().formatmonth(int(args[2]), monthdict[args[1]]))
  else:
    print("Please enter info in the following format: file_name [month] [year]")

calfunc(userinput)