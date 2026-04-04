from datetime import datetime,timedelta,timezone
from dateutil.relativedelta import relativedelta


def calculate_age():
    birthday = '1994-04-21'
    dt =  datetime.strptime(birthday, '%Y-%m-%d').astimezone(timezone.utc)
    now = datetime.now(timezone.utc)
    age = now - dt
    what = timedelta(days=age.days)
    
"""
Question 1:
Given the date 2024-01-31, what is the correct result of adding 1 month, and how would you implement it in Python?
"""    
"""
I am not sure if the year is leap year or not, so I will use relativedelta instead of timedelta
"""
def addOneMonth():
    dt_str =  '2024-01-31'
    dt = datetime.strptime(dt_str,'%Y-%m-%d')
    one_month = dt + relativedelta(months=1)
    print(one_month.date())


"""
Question 2:
Given a subscription start date 2023-08-31, generate the next 6 monthly billing dates correctly.
"""
def generate_bills():
    start_date_str = '2023-08-31'
    start_date = datetime.strptime(start_date_str,'%Y-%m-%d').date()

    current_date = start_date
    for i in range(6):
       next_month =  current_date + relativedelta(months=1)
       print(f'{i+1}. {next_month}')
       start_date = next_month

"""
Question 3 — Expiration Check (Very Common)
You are given:

a subscription start date
a duration in months

Write a function that returns True if the subscription is expired, otherwise False.

Assume:

Dates are stored in UTC

Use best practices
Today’s date should be fetched programmatically
"""

"""
my approach is correct because I correctly converted date strings, and compared date objects
"""
def expiration_check():
    subscription_start_date_str = '2023-01-15'
    subscription_start_date = datetime.strptime(subscription_start_date_str,'%Y-%m-%d').date()
    expiry_date = subscription_start_date + relativedelta(months=12)
    todays_date = datetime.now().astimezone(timezone.utc).date()

    if expiry_date < todays_date:
        return True
    else:
        return False
    
"""
🔥 Next Question (Harder)

Question 4:
Given a UTC datetime, round it to:

start of the day (00:00:00)
end of the day (23:59:59)
Return both values.
"""

"""
Basic Age Difference
Given a date of birth and today’s date, calculate the age in years.
"""

def age_in_years(dob_str):
    dob_date = datetime.strptime(dob_str,'%Y-%m-%d').date()
    current_date = datetime.now().date()

    dob_year = dob_date.year
    dob_month = dob_date.month
    dob_day = dob_date.day

    current_year = current_date.year
    current_month = current_date.month
    current_day = current_date.day


    age = current_year - dob_year
    if (dob_month, dob_day) > (current_month,current_day) :
        age -=1
    return age

print(age_in_years('1998-01-19'))








