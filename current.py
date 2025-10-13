from datetime import date, time, datetime

today = date.today()
now = datetime.now()

print(f"Today is {today}")
print(f"Current time is {now}")
print(f"The date components are year: {today.year}, month: {today.month}, day: {today.day} ")