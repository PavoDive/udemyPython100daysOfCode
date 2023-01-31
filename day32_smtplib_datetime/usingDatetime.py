import datetime

now = datetime.datetime.now()
# prints a full date:
print(now)

# datetime objects have some useful attributes and methods:
print(now.year)

print(now.weekday()) # prints int starting from 0 == Monday. Method isoweekday() prints starting from 0 == Sunday.

date_of_birth = datetime.datetime(year = 1974, month = 2, day = 10)
print(date_of_birth)
