import datetime

# Creating time object
mytime = datetime.time(hour=13, minute=20, second=1, microsecond=30)
print(mytime.minute)
print(mytime.hour)
print(mytime)
print(type(mytime))

# Creating datetime object
mydatetime = datetime.datetime(year=2021, month=10, day=3, hour=14, minute=20, second=1)
print(mydatetime)
mydatetime = mydatetime.replace(year=1999)
print(mydatetime)

# Datetime arithmetic
date1 = datetime.date(2021, 11, 3)
date2 = datetime.date(2020, 11, 3)
result = date1 - date2
print(result.days)

datetime1 = datetime.datetime(2021, 11, 3, 22, 0)
datetime2 = datetime.datetime(2020, 11, 3, 12, 0)
result = datetime1 - datetime2
print(result)
