
# TIME MODULE

# This module provides various time-related functions.
import time

for i in range(5, 0, -1):
    print(i, end=" - ", flush=True)
    time.sleep(1)
print("Put Something here:")

# flush is optional

countdown: int = input("Enter Time Countdown: ")

for x in range(int(countdown), 0, -1):
    hours = int(x / 3600)
    minutes = int(x / 60) % 60
    seconds = x % 60
    print(f"{minutes:02}: {seconds:02}")
    time.sleep(1)
print("BOOM!")

# explore more about here