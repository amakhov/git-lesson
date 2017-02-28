from datetime import datetime
from datetime import timedelta

def days_ny():
    now = datetime.today()
    newyear = datetime(now.year+1, 1, 1, 0, 0, 0)
    delta = (newyear - now).days
    return delta

full_days = days_ny()
print('До нового года осталось',format(full_days),' дней')
