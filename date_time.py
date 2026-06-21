import datetime

print(datetime.date(2024, 1, 2))
print(datetime.date.today())
print(datetime.time(12, 30, 45))
now = datetime.datetime.now()
now = now.strftime("%H:%M:%S %m/%d/%Y")
print(now)

print()
target_date = datetime.datetime(2030, 1, 2, 12, 30, 00)
current_date = datetime.datetime.now()

if target_date < current_date:
    print("The target date has already passed.")
elif target_date > current_date:
    print("The target date is in the future.")
else:
    print("The target date is today!")