
import datetime

# dob = datetime.datetime(2004, 10, 5)
# formatted = dob.strftime( %b )
# print (formatted)

user_input_date = "12 December 2025"
date_object = datetime.datetime.strptime(user_input_date, "%d %B %Y")

five_year_later = date_object + datetime.timedelta(5 * 365)
print(five_year_later)
