# DATETIME MODULE

# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
# The datetime module has many methods to return information about the date object.
# The output in date contains year, month, day, hour, minute, second, and microsecond.

import datetime

display_now = datetime.datetime.now()

print(f"Year: {display_now.year}")
print(f"Month: {display_now.month}")
print(f"Day: {display_now.day}")
print(f"Hour: {display_now.hour}")
print(f"Minute: {display_now.minute}")
print(f"Second: {display_now.second}")

# The strftime() is a method for formatting date objects into readable strings.
# It takes one parameter, format, to specify the format of the returned string.

print(display_now.strftime("%B"))

# Explore more legal format codes for strftime{}
