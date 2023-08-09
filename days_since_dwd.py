import datetime

current_date=datetime.date.today()

dwd_date=datetime.date(2011,7,12)

days_since=(current_date-dwd_date).days

print(days_since)


