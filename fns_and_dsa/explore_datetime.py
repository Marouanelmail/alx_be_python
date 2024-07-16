#!/usr/bin/python3
from datetime import datetime, timedelta
# d = datetime.date.today()
# print(d.day)
# print(d.year)
# print(d.month)
# # def display_current_datetime():
# dt = datetime.datetime.today()
# print(dt)
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
display_current_datetime()
number_of_days = int(input("Enter the number of days to add to the current date: "))
# print(f"Number of days to add: {number_of_days}")
def calculate_future_date(days_to_add):
    current_date = datetime.now()
    future_date = current_date + timedelta(days = days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    return formatted_future_date
future_date = calculate_future_date(number_of_days)
print(f"Future date: {future_date}")
# calculate_future_date(number_of_days)