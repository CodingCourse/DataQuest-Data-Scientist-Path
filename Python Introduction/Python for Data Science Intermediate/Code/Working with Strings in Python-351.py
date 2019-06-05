## 1. Introduction ##

import csv

f = open('artworks.csv')
moma = list(csv.reader(f))
# remove the header row
moma = moma[1:]

# Write your code here
num_rows = 0
for art in moma:
    num_rows += 1

## 2. Replacing Characters and Substrings ##

for row in moma:
    nationality = row[2]
    nationality = nationality.replace("(","")
    nationality = nationality.replace(")","")
    row[2] = nationality

def print_dataset_col(dataset,column):
    for row in dataset:
        print(row[column])
        
def clean_brackets(dataset,column):
    for elements in dataset:
        elements[column] = elements[column].replace("(","").replace(")","")

print_dataset_col(moma[:5],5)        
clean_brackets(moma,5)
print_dataset_col(moma[:5],5)

## 3. String Capitalization ##

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


## 5. Catching Exceptions with Try/Except ##

def clean_and_convert(date):
    date = date.replace("(", "")
    date = date.replace(")", "")
    date = int(date)
    return date

for row in moma:
    birth_date = row[3]
    death_date = row[4]
    try:
        birth_date = clean_and_convert(birth_date)
    except:
        birth_date = ""
    try:
        death_date = clean_and_convert(death_date)
    except:
        death_date = ""
    row[3] = birth_date
    row[4] = death_date

## 6. Parsing Numbers from Complex Strings, Part One ##

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

## 7. Parsing Numbers from Complex Strings, Part Two ##

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

## 8. Summarizing Numeric Data ##

def calculate_decades(decades):
    decade_ranges = {}
    for d in decades:
        if d in decade_ranges:
            decade_ranges[d] += 1
        else:
            decade_ranges[d] = 1
    return decade_ranges

decades = []
for art in moma:
    year = art[6]
    birth = art[3]
    decade = "Unknown"
    if type(birth) == int:
        age = year - birth
        if age > 19:
            decade = str(age)[:-1]
            decade += "0s"
    else:
        birth = "Unknown"
    decades.append(decade)
    
decade_summary = calculate_decades(decades)

## 9. String Formatting ##

def parse_birth_year(artist):
    for row in moma:
        if row[1] == artist:
            birth_date = row[3]
            if birth_date == "":
                birth_date = "unknown"
            return birth_date
        
def parse_departments(artist):
    departments = []
    for row in moma:
        if row[1] == artist:
            dept = row[7]
            if dept not in departments:
                departments.append(dept)
    return departments

def summary(name):
    birth = parse_birth_year(name)
    department = parse_departments(name)
    str_department = '\n- '.join(department)
    string = "{}'s birth year is {}, and their works are found in the following department(s):\n- {}".format(name,birth,str_department)
    print(string)
    
summary("Louise Bourgeois")

## 10. Formatting Numbers Inside Strings ##

gender_artworks_count = {}
gender_artist_list = {}

for row in moma:
    gender = row[5]
    artist = row[1]
    if gender != "Gender Unknown/Other":
        if gender in gender_artworks_count:
            gender_artworks_count[gender] += 1
            if artist not in gender_artist_list[gender]:
                gender_artist_list[gender].append(artist)
        else:
            gender_artworks_count[gender] = 1
            gender_artist_list[gender] = [artist]

gender_data = []

for gender in gender_artworks_count:
    artworks_count = gender_artworks_count[gender]
    artists_count = len(gender_artist_list[gender])
    average_works = artworks_count / artists_count
    gender_data.append([gender, artworks_count, average_works])

for row in gender_data:
    gender = row[0]
    count = row[1]
    average = row[2]
    template = "There are {:,} artworks by {} artists at an average of {:.1f} each."
    print(template.format(count,gender,average))    
    
for a in gender_data:
    string = "There are {:,} artworks by {} artists at an average of {:.1f} each.".format(a[1],a[0],a[2])
    print(string)

## 11. Creating a Function to Summarize Data ##

def widest_key_value(dictionary):
    max_key_width = 0
    max_val_width = 0

    for key, value in dictionary.items():
        key_width = len(str(key))
        val_width = len(str(value))
        
        if key_width > max_key_width:
            max_key_width = key_width
        
        if val_width > max_val_width:
            max_val_width = val_width

    return max_key_width, max_val_width

def freq_table(column):
    table = {}
    for art in moma:
        temp = art[column]
        if temp in table:
            table[temp] += 1
        else:
            table[temp] = 1
            
        key_width,val_width = widest_key_value(table)
        val_width += 1
    for key,value in sorted(table.items()):
        print("{:<{}} : {:>{},}".format(key,key_width,value,val_width))
            
freq_table(7)