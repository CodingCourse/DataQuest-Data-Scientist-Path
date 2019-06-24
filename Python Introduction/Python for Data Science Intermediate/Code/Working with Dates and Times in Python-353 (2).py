## 1. Introduction ##

from csv import reader
potus = list(reader(open('potus_visitors_2015.csv')))
potus = potus[1:]

## 4. The Datetime Class ##

import datetime as dt
ibm_founded = dt.datetime(1911,6,16)
microsoft_founded = dt.datetime(1975,4,4)
man_on_moon = dt.datetime(1969,7,20,20,17)
jfk_shot = dt.datetime(1963,11,22,12,30)

## 5. Using Strptime to Parse Strings as Dates ##

import datetime as dt

for visitors in potus:
    appt_start_date = visitors[2]
    visitors[2] = dt.datetime.strptime(appt_start_date, "%m/%d/%y %H:%M")

## 6. Using Strftime to format dates ##

visitors_per_month = {}
for visitors in potus:
    appt_start_date = visitors[2]
    string = appt_start_date.strftime("%B, %Y")
    if string in visitors_per_month:
        visitors_per_month[string] += 1
    else:
        visitors_per_month[string] = 1

## 7. The Time Class ##

appt_times = {}
max_time = potus[0][2].time()
min_time = potus[0][2].time()

for visitors in potus:
    date_time = visitors[2]
    time_obj = date_time.time()
    if time_obj in appt_times:
        appt_times[time_obj] += 1
    else:
        appt_times[time_obj] = 1
    if time_obj > max_time:
        max_time = time_obj
    if time_obj < min_time:
        min_time = time_obj

## 10. Summarizing Appointment Lengths ##

for visitors in potus:
    visitors[3] = dt.datetime.strptime(visitors[3],"%m/%d/%y %H:%M")

appt_lengths = []

for visitors in potus:
    appt_lengths.append(visitors[3] - visitors[2])

min_length = appt_lengths[0]
max_length = appt_lengths[0]
avg_length = appt_lengths[0]

for elements in appt_lengths[1:]:
    if elements > max_length:
        max_length = elements
    if elements < min_length:
        min_length = elements
    avg_length += elements

avg_length /= len(appt_lengths)