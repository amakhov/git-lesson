from datetime import datetime
from datetime import timedelta

def daysyear():
    now = datetime.today()
    NY = datetime(now.year+1, 1, 1, 0, 0, 0)
    delta = (NY - now).days
    return delta

full_days = daysyear()
print('До нового года осталось {} дней'.format(full_days))
