from datetime import datetime

def get_days_from_today(date):
    today = datetime.today()
    date_to_string = datetime.strptime(date, "%Y-%m-%d")
    date_difference = (today - date_to_string)
    return date_difference.days

print(get_days_from_today("2010-10-09"))