## 1. Interfering with the Built-in Functions ##

a_list = [1, 8, 10, 9, 7]
max_value = max(a_list)
print(max_value)
del max

## 3. Default Arguments ##

from csv import reader

def open_dataset(csv_file_name = 'AppleStore.csv'):
    opened_file = open(csv_file_name)
    read_file = reader(opened_file)
    apps_data = list(read_file)
    return apps_data
    
apps_data = open_dataset()
print(apps_data)

## 4. The Official Python Documentation ##

one_decimal = round(3.43,1)
two_decimals = round(0.23321,2)
five_decimals = round(921.2225227,5)

## 5. Multiple Return Statements ##

def open_dataset(file_name='AppleStore.csv',header=1):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    if header == 1:
        data = data[1:]
    return data

apps_data = open_dataset()

## 6. Returning Multiple Variables ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[0],data[1:]
    else:
        return data
    
all_data = open_dataset()
header = all_data[0]
apps_data = all_data[1]

## 7. More About Tuples ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[0],data[1:]
    else:
        return data
    
header, apps_data = open_dataset()

## 8. Functions — Code Running Quirks ##

def print_constant():
    x = 3.14
    print(x)
    
print_constant()
print(x)

## 9. Scopes — Global and Local ##

e = 'mathematical constant'
a_sum = 1000
length = 50

def exponential(x):
    e = 2.72
    print(e)
    return e**x

result = exponential(5)
print(e)

def divide():
    print(a_sum)
    print(length)
    return a_sum / length

result_2 = divide()

## 10. Scopes — Searching Order ##

def open_iOS_dataset():        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    global apps_data
    apps_data = data[1:]
    global header_row
    header_row = data[0]
    
file_name = 'AppleStore.csv'
open_iOS_dataset()
print(header_row)
first_five = apps_data[:5]