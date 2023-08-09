import datetime

def check_days_since_dwd():
    current_date=datetime.date.today()
    dwd_date=datetime.date(2011,7,12)
    days_since=(current_date-dwd_date).days
    return days_since


print(check_days_since_dwd())


