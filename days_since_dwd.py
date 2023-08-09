import datetime

dwd_date = datetime.date(2011,7,12) # finds date of release for ADWD

def check_days_since_dwd():
    current_date = datetime.date.today() # finds current date using datetime
    days_since = (current_date-dwd_date).days # calculates the number of days since its release
    return days_since 


print(f"It has been {check_days_since_dwd()} days since A Dance With Dragons was released.") 


