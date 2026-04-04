from datetime import date, time, datetime, timedelta,timezone
"""
Python has two main standard modules for dates:
from datetime import date, time, datetime, timedelta
"""

"""
| Type       | Represents  | Example             |
| ---------- | ----------- | ------------------- |
| `date`     | Date only   | 2026-02-26          |
| `time`     | Time only   | 14:30:00            |
| `datetime` | Date + Time | 2026-02-26 14:30:00 |

"""

# Create Dates

d = date(2026,2,26)
print(d)

# Create Times
t = time(10,26,30)
print(t)

# Create DateTime
dt = datetime(2026,2,26,10,26,30)
print(dt)

# Get Current Date & Time (Very Common)
now = datetime.now() # datetime.now() uses local server time — dangerous in production if not controlled.
today_date = date.today()

print(now)
print(today_date)


# Working with Timezones (CRITICAL)
# Never rely on naive datetimes in production.

now_utc = datetime.now(timezone.utc)
print(now_utc) # ✅ Always store UTC in databases.

# Parsing Dates from Strings

dt = datetime.strptime('2026-02-26 10:26:30','%Y-%m-%d %H:%M:%S')
print(dt)


"""
| Format | Meaning    |
| ------ | ---------- |
| `%Y`   | Year       |
| `%m`   | Month      |
| `%d`   | Day        |
| `%H`   | Hour (24h) |
| `%M`   | Minute     |
| `%S`   | Second     |

"""

# Formatting Dates to Strings

date_str = dt.strftime('%d %b, %Y ' '%H %M')
print(date_str)


# Date Arithmetic (Very Important)
today = datetime.now(timezone.utc)
next_week =  today + timedelta(days=7)
tomorrow = today + timedelta(days=1)
formatted = tomorrow.strftime("%d %b")
print('tomorrow is', formatted)
print(next_week)

# Add hours/minutes
future = today + timedelta(hours=3,minutes=60)

print(future)

# Difference Between Two Dates

diff = next_week - today
print(diff)
print('In days: ',diff.days)
print('In seconds: ',diff.total_seconds())


#  Comparing Dates

dt1 = datetime.now(timezone.utc)
dt2 = dt1 + timedelta(days=7)

if dt1 == dt2:
    print('It is today')
else:
    print('Not today')

if dt1.today() == date.today():
    print('Yes, it is today')


datetime.now(timezone.utc)      # current UTC time
datetime.strptime()            # string → datetime
datetime.strftime()            # datetime → string
timedelta(days=7)              # date math
dt1 > dt2                      # comparison
dt.isoformat()                 # API-friendly format


# creating token expiration logic


def expireJWT(current_date):
    created_at = datetime(2026,1,26,20,40,30,tzinfo=timezone.utc)
    expires_at = created_at + timedelta(days=7)
    if current_date > expires_at:
        print('TOKEN EXPIRED!')
    else:
        print('TOKEN VALID!')
    
expireJWT(dt1)

"""
1️⃣1️⃣ Common Mistakes (Avoid These)

❌ Using datetime.now() without timezone
❌ Mixing naive and timezone-aware datetimes
❌ Storing local time in database
❌ Manually calculating months/years with timedelta

"""



# ❌ 1. Using datetime.now() without timezone
# ❌ Bad (naive datetime)

from datetime import datetime

created_at = datetime.now()   # NO timezone
"""
Why this is bad

You don’t know which timezone this represents

Breaks when server timezone changes

Causes bugs when compared with UTC values
"""

from datetime import datetime, timezone

created_at = datetime.now(timezone.utc)

# ❌ 2. Mixing naive and timezone-aware datetimes
# ❌ Bad (will crash)

from datetime import datetime, timezone

dt1 = datetime.now()                # naive
dt2 = datetime.now(timezone.utc)    # aware

dt1 > dt2   # ❌ TypeError

# ✅ Best Practice (make everything aware)

from datetime import datetime, timezone

dt1 = datetime.now(timezone.utc)
dt2 = datetime.now(timezone.utc)

dt1 > dt2  # ✅ safe

# ⚠️ Only do this if you know the naive datetime was meant to be UTC.

# ❌ 3. Storing local time in the database
# ❌ Bad (local time)
created_at = datetime.now()  # server local time

"""
Problems

Server location changes → broken data

Daylight Saving Time shifts

Impossible to reliably compare across regions
"""

# ✅ Best Practice (store UTC only)

created_at = datetime.now(timezone.utc)
"""
Frontend

Convert to user’s timezone (Flutter / JS)
"""

# ❌ 4. Manually calculating months or years with timedelta
# ❌ Bad (months ≠ 30 days)

from datetime import timedelta

next_month = today + timedelta(days=30)  # ❌ wrong

from datetime import timedelta

next_month = today + timedelta(days=30)  # ❌ wrong
"""
Why this is wrong

Months have 28–31 days

Leap years exist

Causes silent, dangerous date drift
"""

# ✅ Best Practice (use dateutil.relativedelta)

from dateutil.relativedelta import relativedelta

next_month = today + relativedelta(months=1)
next_year = today + relativedelta(years=1)

"""
This correctly handles:

Month length

Leap years

End-of-month edge cases
"""

# 🧠 Real-World Example (Subscription Expiry)
# ❌ Wrong

expires_at = created_at + timedelta(days=365)
from dateutil.relativedelta import relativedelta

expires_at = created_at + relativedelta(years=1)

"""
✅ Golden Rules (Memorize These)

Backend always uses UTC

Never compare naive and aware datetimes

Database stores UTC only

Frontend handles localization

Use relativedelta for months/years
"""

# Production-Ready Template
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta

created_at = datetime.now(timezone.utc)
expires_at = created_at + relativedelta(months=1)




    



