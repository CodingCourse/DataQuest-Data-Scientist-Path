## 2. Understanding Vectorization ##

import numpy as np
data_ndarray = np.array([10,20,30])


## 3. NYC Taxi-Airport Data ##

import csv
import numpy as np

# import nyc_taxi.csv as a list of lists
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))

# remove the header row
taxi_list = taxi_list[1:]

# convert all values to floats
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

# start writing your code below this comment
taxi = np.array(converted_taxi_list)

## 4. Array Shapes ##

taxi_shape = taxi.shape
print(taxi_shape)

## 5. Selecting and Slicing Rows and Items from ndarrays ##

row_0 = taxi[0]
rows_391_to_500 = taxi[391:501]
row_21_column_5 = taxi[21,5]

## 6. Selecting Columns and Custom Slicing ndarrays ##

columns_1_4_7 = taxi[:,[1,4,7]]
row_99_columns_5_to_8 = taxi[99,5:9]
rows_100_to_200_column_14 = taxi[100:201,14]

## 7. Vector Math ##

fare_amount = taxi[:,9]
fees_amount = taxi[:,10]

fare_and_fees = fare_amount + fees_amount

## 8. Vector Math Continued ##

trip_distance_miles = taxi[:,7]
trip_length_seconds = taxi[:,8]

trip_length_hours = trip_length_seconds / 3600 # 3600 seconds is one hour

trip_mph = trip_distance_miles / trip_length_hours

## 9. Calculating Statistics For 1D ndarrays ##

mph_min = trip_mph.min()

mph_max = trip_mph.max()
mph_mean = trip_mph.mean()

## 11. Calculating Statistics For 2D ndarrays ##

fare_sums = fare_components.sum(axis = 1)
fare_totals = taxi_first_five[:,13]
print(fare_totals, fare_sums, sep = "\n")