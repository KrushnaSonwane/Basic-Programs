#!/usr/bin/python
import calendar
import time
cal = calendar.month(2022, 3)
print("Here is the calendar:")
print(cal)


localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)