## 1. Opening Files ##

f = open("crime_rates.csv", "r")
#print(f)

## 2. Reading In Files ##

f = open("crime_rates.csv", "r")
data = f.read()

## 3. Splitting ##

# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
#print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
#print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split("\n")
print(rows)

## 5. Practice - Loops ##

ten_rows = rows[0:10]
for row in ten_rows:
    print(row)

## 6. List of Lists ##

three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []
for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)
print(final_list[0])
print(final_list[1])
print(final_list[2])

## 7. Practice - Splitting Elements in a List ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
final_data=[]
for row in rows:
    final_data.append(row.split(','))
print(final_data[0:5])

## 8. Accessing Elements in a List of Lists: The Manual Way ##

cities_list=[]
for city in five_elements[0:5]:
    cities_list.append(city[0])

## 9. Looping Through a List of Lists ##

cities_list = []
for row in final_data:
    cities_list.append(row[0])
    


## 10. Challenge ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
int_crime_rates = []
for row in rows:
    rows_split = row.split(",")
    int_crime_rates.append(int(rows_split[1]))