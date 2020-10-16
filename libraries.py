
#printing two weeks date
from datetime import datetime , timedelta 
now = datetime.today(
add_twoweeks = now + timedelta(days = 14)
now = add_twoweeks
print(add_twoweeks.strftime("%y-%m-%d"))







