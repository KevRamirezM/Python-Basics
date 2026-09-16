# Date and time
import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()
print(date)
print(today)

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()
print(time)
print(now)

full = now.strftime("%H:%M:%S %d %m %Y")
print(full)

target_time = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_time = datetime.datetime(now)

if target_time < current_time:
    print("Target date has passed")
else:
    print("Target date has not passed")