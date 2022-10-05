#Time data type used for code work with time and date

import datetime

datetime_object = datetime.datetime.now()
print('\n--- Time Now ---')
print(datetime_object)

date_object = datetime.datetime.today()
print('\n--- Time Today ---')
print(date_object)

d = datetime.date(1999, 3, 19)
print('\n--- Just Date ---')
print(d)



from datetime import date
# date object of today's date
today = date.today()
print('\n--- Date Separate ---')
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

#Time Delta

from datetime import datetime, date
t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)
t3 = t1 - t2
print('\n--- Time Delta ---')
print("t3 =", t3)
t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9,
second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55,
second = 13)
t6 = t4 - t5
print("t6 =", t6)
print("type of t3 =", type(t3))
print("type of t6 =", type(t6))


#strftime

from datetime import datetime
# current date and time
now = datetime.now()
print('\n--- strftime ---')
t = now.strftime("%H:%M:%S")
print("time:", t)
s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)
s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

#strptime

from datetime import datetime
date_string = "21 June, 2018"
print('\n--- strptime ---')
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

#Timezone

from datetime import datetime
import pytz
local = datetime.now()
print('\n--- Change Timezone ---')
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))
tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))
tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))
