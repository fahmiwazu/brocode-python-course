######### Time Module in Python
import time

print(time.ctime(1000000)) # epoch = when your computer thinks time began
print(time.time())   # return current seconds since epoch
print(time.ctime(time.time())) # get current date/time

time_object = time.localtime()
# time_object = time.gmtime()
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S",time_object)
print(local_time)

time_string = "20 February, 1997"
time_object = time.strptime(time_string,"%d %B, %Y")
print(time_object)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)