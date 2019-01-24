## 1. Functions ##

list_1 = [1, 8, 10, 9, 7, 5, 9, 1, 8, 4, 5, 3, 3, 2, 0, 9,
          6, 5, 2, 6, 9, 8, 8, 1, 2, 8, 0, 3, 4, 8, 6, 2,
          2, 6, 9, 2, 9, 9, 1, 8, 10, 10, 2, 2, 3, 6, 10,
          9, 8, 7]

list_2 = [678, 685, 870, 927, 176, 893, 366, 780, 261, 815,
          204, 946, 465, 670, 19, 632, 182, 46, 13, 202, 566,
          609, 481, 18, 992, 490, 878, 398, 942, 694, 763,
          986, 825, 843, 798, 658, 426, 613, 14, 369, 638,
          831, 585, 608, 588, 418, 117, 18, 755, 680]

list_3 = [4444, 8897, 6340, 9896, 4835, 4324, 10000, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280, 1318,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 3717,
          5929, 7061, 4214, 5127, 6171, 3782, 3798, 8970,
          3102, 9771, 746, 4974, 7996, 3122, 1362, 8140, 4412,
          1390, 2240, 3063, 4228, 7030, 8479, 5081, 66]

sum_1 = 0
sum_2 = 0
sum_3 = 0

for one in list_1:
    sum_1 += one

for two in list_2:
    sum_2 += two

for three in list_3:
    sum_3 += three
    

## 2. Built-in Functions ##

ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']
content_ratings = {}
for element in ratings:
    if element in content_ratings:
        content_ratings[element] += 1
    else:
        content_ratings[element] = 1

n_unique = len(content_ratings)

## 3. Creating Our Own Functions ##

def square(num):
    return num*num

def square_2(num):
    return num**2

def add_10(num):
    return num+10

squared_10 = square(10)
squared_16 = square(16)

squared_20 = square_2(20)
squared_100 = square_2(100)

add_30 = add_10(30)
add_90 = add_10(90)

## 4. Parameters and Arguments ##

a_list = [2, 1, 'data point', 'five', 89, 1, 'zero', True, 2.332]
a_dictionary = {1: 'Name', 2: True, 3: [1,2,3], 4: 9.2221, 5: 5}

def square(num):
    return num*num

def len_2(iterable):
    length = 0
    for element in iterable:
        length += 1
    return length

squared_6 = square(6)
squared_11 = square(11)

list_length = len_2(a_list)
dictionary_length = len_2(a_dictionary)

## 5. Creating Frequency Tables ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(num):
    extract_col = []
    for element in apps_data[1:]:
        extract_col.append(element[num])
    return extract_col

def freq_table(num_list):
    freq_dict = {}
    for element in num_list:
        if element in freq_dict:
            freq_dict[element] += 1
        else:
            freq_dict[element] = 1
    return freq_dict

content_ratings = extract(10)
content_ratings_ft = freq_table(content_ratings)
ratings = extract(7)
ratings_ft = freq_table(ratings)
genres = extract(11)
genres_ft = freq_table(genres)

## 6. Writing a Single Function ##

def freq_table(num):
    freq_dict = {}
    for element_list in apps_data[1:]:
        element = element_list[num]
        if element in freq_dict:
            freq_dict[element] += 1
        else:
            freq_dict[element] = 1
    return freq_dict

content_ratings_ft = freq_table(10)
ratings_ft = freq_table(7)
genres_ft = freq_table(11)

## 7. Reusability and Multiple Parameters ##

def freq_table(index,apps_data):
    frequency_table = {}
    
    for row in apps_data[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table

content_ratings_ft = freq_table(10,apps_data)
ratings_ft = freq_table(7,apps_data)
genres_ft = freq_table(11,apps_data)

## 8. Keyword and Positional Arguments ##

def freq_table(data_set, index):
    frequency_table = {}
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            

content_ratings_ft = freq_table(apps_data,10)
ratings_ft = freq_table(index = 7, data_set = apps_data)
genres_ft = freq_table(index = 11,data_set = apps_data)

## 9. Combining Functions ##

def extract(data_set, index):
    data_list = []
    for element in data_set[1:]:
        data_list.append(element[index])
    return data_list

def find_sum(data_list):
    element_sum = 0
    for element in data_list:
        element_sum += float(element)
    return element_sum

def find_length(data_list):
    list_length = 0
    for element in data_list:
        list_length += 1
    return list_length

def mean(data_set, index):
    data_list = extract(data_set, index)
    return find_sum(data_list) / find_length(data_list)

avg_price = mean(apps_data, 4)
avg_rating = mean(apps_data, 7)

## 10. Debugging Functions ##

def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    column = extract(data_set, index)
    return find_sum(column) / find_length(column)

avg_price = mean(apps_data, 4)
avg_rating = mean(apps_data, 7)