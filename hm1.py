from datetime import datetime

def get_days_from_today(date):
    today = datetime.today()
    try:
        date_to_string = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Format of the date must be: YYYY-MM-DD")
    date_difference = (today - date_to_string)
    return date_difference.days

print(get_days_from_today("13.14.2000"))