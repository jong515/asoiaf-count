import datetime

dwd_date = datetime.date(2011,7,12) 
current_date = datetime.date.today()


total_days_since = (current_date-dwd_date).days 
# calculates the number of days since its release

years = total_days_since // 365
months = (total_days_since - years * 365) // 30
days = (total_days_since - years * 365 - months * 30)
# converts the number of days into years, months, days

msg = ( f"It has been {total_days_since} days since A Dance With Dragons was released. \n\n" 
        f"OR \n\n{years} years, {months} months, {days} days since A Dance With Dragons was released.")

""" Creates a string message to print out, then checks if its a single month or day and changes the message 
accordingly """

if months == 1:
    msg = ( f"It has been {total_days_since} days since A Dance With Dragons was released. \n\n" 
        f"OR \n{years} years, {months} month, {days} days since A Dance With Dragons was released.")
if days == 1:
    msg = ( f"It has been {total_days_since} days since A Dance With Dragons was released. \n\n" 
        f"OR \n\n{years} years, {months} months, {days} day since A Dance With Dragons was released.")
if months == 1 and days == 1:
    msg = ( f"It has been {total_days_since} days since A Dance With Dragons was released. \n\n" 
        f"OR \n\n{years} years, {months} month, {days} day since A Dance With Dragons was released.")

print(f'Dear GRRM {msg}')
