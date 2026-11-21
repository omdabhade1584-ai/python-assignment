#Q7. Generator and Datetime Module (3 Marks)
#Create a generator function that generates dates for the next 7 days starting f
from datetime import date,timedelta
def next_7_days():
  today=date.today()
  for i in range(7):
     yield today+timedelta(days=i)
for day in next_7_days():
 print(day)