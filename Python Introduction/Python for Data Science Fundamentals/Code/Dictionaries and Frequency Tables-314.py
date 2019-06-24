## 1. Storing Data ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
over_4 = content_ratings['4+']
over_9 = content_ratings['9+']
over_12 = content_ratings['12+']
over_17 = content_ratings['17+']
top_genres = {'Games':3862, 'Entertainment':535, 'Education':453, 'Photo & Video':349, 'Utilities':248}
number_of_gaming_apps = top_genres['Games']

## 4. Alternative Way of Creating a Dictionary ##

content_ratings = {}
content_ratings['4+'] = 4433
content_ratings['9+'] = 987
content_ratings['12+'] = 1155
content_ratings['17+'] = 622
over_12_n_apps = content_ratings['12+']
top_genres = {}
top_genres['Games'] = 3862
top_genres['Entertainment'] = 535
top_genres['Education'] = 453
top_genres['Photo & Video'] = 349
top_genres['Utilities'] = 248
n_apps_education = top_genres['Education']

## 6. Checking for Membership ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
is_in_dictionary_1 = '4+' in content_ratings
is_in_dictionary_2 = '20+' in content_ratings
is_in_dictionary_3 = 4433 in content_ratings
is_in_dictionary_4 = 987 in content_ratings
if '17+' in content_ratings:
    result = "'17+' exists in content_ratings"
    print(result)

## 7. Counting with Dictionaries ##

from csv import reader

opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {}
for apps in apps_data[1:]:
    if apps[10] in content_ratings:
        content_ratings[apps[10]] += 1
    else:
        content_ratings[apps[10]] = 1

print(content_ratings)

## 8. Finding the Unique Values ##

from csv import reader

opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {}
for apps in apps_data[1:]:
    if apps[10] in content_ratings:
        content_ratings[apps[10]] += 1
    else:
        content_ratings[apps[10]] = 1

print(content_ratings)

genre_counting = {}
for apps in apps_data[1:]:
    if apps[11] in genre_counting:
        genre_counting[apps[11]] += 1
    else:
        genre_counting[apps[11]] = 1
        
most_common_genre = 'Games'

## 10. Looping over Dictionaries ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
genre_counting = {'Social Networking': 167, 'Photo & Video': 349, 'Games': 3862, 'Music': 138, 'Reference': 64, 'Health & Fitness': 180, 'Weather': 72, 'Utilities': 248, 'Travel': 81, 'Shopping': 122, 'News': 75, 'Navigation': 46, 'Lifestyle': 144, 'Entertainment': 535, 'Food & Drink': 63, 'Sports': 114, 'Book': 112, 'Finance': 104, 'Education': 453, 'Productivity': 178, 'Business': 57, 'Catalogs': 10, 'Medical': 23}

total_number_of_apps = 7197

for content in content_ratings:
    content_ratings[content] /= total_number_of_apps
    content_ratings[content] *= 100

percentage_17_plus = content_ratings['17+']
percentage_15_allowed = 100 - percentage_17_plus

for genre in genre_counting:
    genre_counting[genre] /= total_number_of_apps
    genre_counting[genre] *= 100
    
percentage_games = genre_counting['Games']
percentage_non_games = 100 - percentage_games

## 11. Keeping the Dictionaries Separate ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
genre_counting = {'Social Networking': 167, 'Photo & Video': 349, 'Games': 3862, 'Music': 138, 'Reference': 64, 'Health & Fitness': 180, 'Weather': 72, 'Utilities': 248, 'Travel': 81, 'Shopping': 122, 'News': 75, 'Navigation': 46, 'Lifestyle': 144, 'Entertainment': 535, 'Food & Drink': 63, 'Sports': 114, 'Book': 112, 'Finance': 104, 'Education': 453, 'Productivity': 178, 'Business': 57, 'Catalogs': 10, 'Medical': 23}

total_number_of_apps = 7197
c_ratings_percentages = {}
c_ratings_proportions = {}
genre_percentages = {}
genre_proportions = {}

for content in content_ratings:
    c_ratings_proportions[content] = content_ratings[content]/total_number_of_apps
    c_ratings_percentages[content] = c_ratings_proportions[content]*100

for genre in genre_counting:
    genre_proportions[genre] = genre_counting[genre]/total_number_of_apps
    genre_percentages[genre] = genre_proportions[genre]*100

## 12. Frequency Tables for Numerical Columns ##

data_sizes = []
for apps in apps_data[1:]:
    size = float(apps[2])
    data_sizes.append(size)

min_size = min(data_sizes)
max_size = max(data_sizes)

## 13. Filtering for the Intervals ##

rating_count = []
for rating in apps_data[1:]:
    rating_count.append(int(rating[5]))
    
ratings_max = max(rating_count)
ratings_min = min(rating_count)

rating_count_dict = {'2000000+': 0, '1000000+': 0, '500000+': 0, '100000+': 0, '50000+': 0, '10000+': 0, '5000+': 0, '1000+': 0, '500+': 0, '100+': 0, '0 - 100': 0}

for rating in apps_data[1:]:
    rate = int(rating[5])
    if rate > 2000000:
        rating_count_dict['2000000+'] += 1
    elif rate > 1000000:
        rating_count_dict['1000000+'] += 1
    elif rate > 500000:
        rating_count_dict['500000+'] += 1
    elif rate > 100000:
        rating_count_dict['100000+'] += 1
    elif rate > 50000:
        rating_count_dict['50000+'] += 1
    elif rate > 10000:
        rating_count_dict['10000+'] += 1
    elif rate > 5000:
        rating_count_dict['5000+'] += 1
    elif rate > 1000:
        rating_count_dict['1000+'] += 1
    elif rate > 500:
        rating_count_dict['500+'] += 1
    elif rate > 100:
        rating_count_dict['100+'] += 1
    else:
        rating_count_dict['0 - 100'] += 1
        
print(rating_count_dict)