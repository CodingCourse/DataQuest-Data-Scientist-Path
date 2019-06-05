## 1. Introduction ##

import csv

f = open('world_bank_gdp.csv')
gdp = list(csv.reader(f))
gdp = gdp[1:]

ireland = gdp[57][1:]

ireland_int = []

for item in ireland:
    ireland_int.append(int(item))

## 2. Writing List Comprehensions ##

ireland = gdp[57][1:]

# LOOP VERSION
#
# ireland_int = []
# for i in ireland:
#     ireland_int.append(int(i))

ireland_int = [int(i) for i in ireland]

## 3. Common Applications of List Comprehensions ##

jamaica = gdp[62][1:]

jamaica_mil = [int(jam)/1000000 for jam in jamaica]
years = [str(year) for year in range(1970,2018)]
gdp_1970 = [row[1] for row in gdp]

## 4. Nested List Comprehensions ##

def convert(item):
    try:
        value = round(int(item)/1000000)
    except:
        value = item
    return value

gdp = [[convert(i) for i in row] for row in gdp]

## 5. Enumerating Lists ##

china = gdp[22][1:]
germany = gdp[31][1:]
cn_pct_of_de = []

for i, item_1 in enumerate(china):
    item_2 = germany[i]
    cn_pct_of_de.append(item_1/item_2)

## 6. Combining Lists with the Zip Function ##

india = gdp[56][1:]
australia = gdp[4][1:]

ind_pct_of_au = [one/two for one,two in zip(india,australia)]

## 7. The Any and All Functions ##

gdp_clean = [row for row in gdp if all(row)]
print(len(gdp),len(gdp_clean))

## 8. Passing Functions as Arguments ##

def key_func(list_arg):
    return list_arg[1]

gdp_sorted_1970 = sorted(gdp_clean, key = key_func, reverse=True)

top_5_1970 = [row[0] for row in gdp_sorted_1970[:5]]

## 9. Lambda Functions ##

# def multiply(a, b):
#    return a * b

multiply = lambda a, b: a * b

## 10. Using Lambda Functions to Analyze Lists of Lists ##

gdp_sorted_2016 = sorted(gdp_clean, key = lambda row: row[-2], reverse = True)
top_5_2016 = [row[0] for row in gdp_sorted_2016[:5]]

## 11. Dictionary Comprehensions ##

gdp_dict = {i[0]:i[1:] for i in gdp_clean}
bangladesh = gdp_dict["Bangladesh"]

## 12. Challenge: Combining Techniques ##

def n_biggest_increase(start_yr, end_yr, n=5):
    countries = [row[0] for row in gdp]
    start = [row[start_yr - 1969] for row in gdp]
    end = [row[end_yr - 1969] for row in gdp]

    cse = [[country, start[i], end[i]] for i, country in enumerate(countries) if country and start[i] and end[i]]

    increases = [[c, e / s] for c, s, e in cse]

    ordered = sorted(increases, key=lambda row: row[1], reverse=True)

    top_n = ordered[:n]

    return top_n

top_5_1980_to_85 = n_biggest_increase(1980, 1985)
print(top_5_1980_to_85)
top_5_1970s = n_biggest_increase(1970, 1980)