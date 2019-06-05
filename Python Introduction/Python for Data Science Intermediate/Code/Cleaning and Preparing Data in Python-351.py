## 1. Introducing Data Cleaning ##

import csv

f = open('artworks.csv')
moma = list(csv.reader(f))
# remove the header row
moma = moma[1:]

# Write your code here
num_rows = len(moma)


## 2. Reading our MoMA Data Set ##

# import the reader function from the csv module
from csv import reader

# use the python built-in function open()
# to open the children.csv file
opened_file = open('children.csv')

# use csv.reader() to parse the data from
# the opened file
read_file = reader(opened_file)

# use list() to convert the read file
# into a list of lists format
children = list(read_file)

# remove the first row of the data, which
# contains the column names
children = children[1:]

# Write your code here
opened_file = open('artworks.csv')
read_file = reader(opened_file)
moma = list(read_file)
moma = moma[1:]

## 3. Replacing Substrings with the replace Method ##

age1 = "I am thirty-one years old"
age2 = age1.replace("one","two")

## 5. String Capitalization ##

def clean_unknown(dataset,column,unknown_text):
    for row in dataset:
        value = row[column].title()
        if not value:
            value = unknown_text
        row[column] = value

clean_unknown(moma,5,"Gender Unknown/Other")
        
def create_frequencies(dataset,column):
    value_counts = {}    
    for row in dataset:
        value = row[2]
        if (value == "") or ("known" in value):
            if value in value_counts:
                value_counts[value] += 1
            else:
                value_counts[value] = 1
    return value_counts

nationality_freq = create_frequencies(moma,2)
print(nationality_freq)
clean_unknown(moma,2,"Nationality Unknown")
nationality_freq = create_frequencies(moma,2)
print(nationality_freq)


## 7. Parsing Numbers from Complex Strings, Part One ##

test_data = ["1912", "1870-79", "1929",
             "1913\\-1923", "(1951)", "1994",
             "1934", "c. 1915", "2009", "1978",
             "1947", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "1964\\-65", "c. 1955.",
             "c. 1970's", "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","\\","s","'"]

def strip_characters(string):
    for data in bad_chars:
        string = string.replace(data,"")
    string = string.strip()
    return string

stripped_test_data = []

for data in test_data:
    stripped_test_data.append(strip_characters(data))
    
print(test_data)
print(stripped_test_data)

## 8. Parsing Numbers from Complex Strings, Part Two ##

bad_chars = ["(",")","c","C",".","\\","s","'"]

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    string = string.strip()
    return string

stripped_test_data = ['1912', '1870-79', '1929',
                      '1913-1923', '1951', '1994', 
                      '1934', '1915', '2009', '1978',
                      '1947', '1995', '1912', '1988',
                      '2002', '1957-1959', '1964-65',
                      '1955', '1970', '1990-1999']
    
def process_dates(string):
    if "-" in string:
        before, after = string.split("-")
        if len(after) == 2:
            after = before[:2] + after
        string = (int(before) + int(after)) / 2
        string = round(string)
    return int(string)

processed_test_data = []

for data in stripped_test_data:
    processed_test_data.append(process_dates(data))

for data in moma:
    date = data[6]
    date = strip_characters(date)
    date = process_dates(date)
    data[6] = date