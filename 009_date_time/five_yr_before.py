
import datetime

# dob = datetime.date(2004, 10, 5)
# five_year_before = dob - datetime.timedelta(days=5 * 365)
# print(five_year_before)


# dob = datetime.datetime(2004, 10, 5, 10, 0, 0)
# five_year_before = dob - datetime.timedelta(hours=5)
# print(five_year_before)

dob_hours = datetime.datetime(2004, 5, 10, 10, 30)
ten_hours_back = dob_hours - datetime.timedelta(hours=10)
print(ten_hours_back)

dob = datetime.datetime(2004, 5, 10, 10, 30)
plus = dob + datetime.timedelta(days=5, hours=1, minutes=30, microseconds=50)
print(plus)