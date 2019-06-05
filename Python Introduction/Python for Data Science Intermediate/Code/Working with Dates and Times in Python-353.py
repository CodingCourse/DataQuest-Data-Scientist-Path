## 1. Introduction ##

from csv import reader
potus = list(reader(open('potus_visitors_2015.csv')))
potus = potus[1:]

## 3. The Datetime Class ##

import datetime as dt
ibm_founded = dt.datetime(1911,6,16)
microsoft_founded = dt.datetime(1975,4,4)
man_on_moon = dt.datetime(1969,7,20,20,17)
jfk_shot = dt.datetime(1963,11,22,12,30)

## 4. Using Strptime to Parse Strings as Dates ##

import datetime as dt

for visitors in potus:
    appt_start_date = visitors[2]
    visitors[2] = dt.datetime.strptime(appt_start_date, "%m/%d/%y %H:%M")

## 5. Using Strftime to format dates ##

visitors_per_month = {}
for visitors in potus:
    appt_start_date = visitors[2]
    string = appt_start_date.strftime("%B, %Y")
    if string in visitors_per_month:
        visitors_per_month[string] += 1
    else:
        visitors_per_month[string] = 1

## 6. The Time Class ##

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

## 7. The Date Class ##

date_freq = {}
max_v_date = ""
max_v_num = 0

for visitors in potus:
    date = visitors[2].date()
    if date in date_freq:
        date_freq[date] += 1
    else:
        date_freq[date] = 1

for element in date_freq:
    if date_freq[element] > max_v_num:
        max_v_num = date_freq[element]
        max_v_date = element

## 8. Calculations with Dates and Times ##

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

## 9. Challenge: How far ahead are appointments made ##

lead_times = []

for v in potus:
    lead_time = dt.datetime.strptime(v[1], "%Y-%m-%dT%H:%M:%S")
    lead_times.append(v[2]-lead_time)

max_time = lead_times[0]
min_time = lead_times[0]
avg_time = lead_times[0]

for elements in lead_times[1:]:
    if max_time < elements:
        max_time = elements
    if min_time > elements:
        min_time = elements
    avg_time += elements

avg_time /= len(lead_times)

## 10. Challenge: Create an Appointment Summary Function ##

def appt_summary(year, month, day):
    template = "Appointments for {:%A %B %d, %Y}:\n".format(dt.datetime(year,month,day))
    template_1 = "{} at {:%-I:%M %p}."
    print(template)
    for v in potus:
        if v[2].date() == dt.date(year, month, day):
            print(template_1.format(v[0].title(),v[2]))

appt_summary(2015, 5, 20)

## 11. Epoch Time ##

epochs = [
           ['first', 1139444034],
           ['second', 1430583565],
           ['third', 1318037820],
           ['fourth', 751652064]
         ]

for e in epochs:
    e[1] = dt.datetime.fromtimestamp(e[1])