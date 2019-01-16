
# Profitable App Profiles for the App Store and Google Play Markets

Mobile Apps usage are on the rise and people nowadays are more inclined to use a mobile platform than a web platform. This analysis is to understand more on the type of apps most people use, it's demographics and other important factors.

The goal is to find those app profiles which produce the most revenue based on the analysis we have done.


```python
from csv import reader
opened_file = open('AppleStore.csv')
reader_file = reader(opened_file)
ios_apps_data = list(reader_file)

opened_file = open('googleplaystore.csv')
reader_file = reader(opened_file)
gps_apps_data = list(reader_file)

def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
        
explore_data(ios_apps_data,0,1,True)
print('\n')
explore_data(gps_apps_data,0,1,True)
```

    ['id', 'track_name', 'size_bytes', 'currency', 'price', 'rating_count_tot', 'rating_count_ver', 'user_rating', 'user_rating_ver', 'ver', 'cont_rating', 'prime_genre', 'sup_devices.num', 'ipadSc_urls.num', 'lang.num', 'vpp_lic']
    
    
    Number of rows: 7198
    Number of columns: 16
    
    
    ['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']
    
    
    Number of rows: 10842
    Number of columns: 13


The above shows the coloumns in each of the csv files. The first one shows the coloumns in IOS Apps Data. For more details of the same, you may check the [documentation][1]. The second one shows the coloumns in Google Play Store's Apps Data. For more details of the same, you may check this [documentation][2]

In addition to that, after each list of the coloumns, the no. of coloumns and rows are also shown. From the above we can see, how many apps details from each platform we currently have.

[1]: https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps/home
[2]: https://www.kaggle.com/lava18/google-play-store-apps/home


```python
unique_apps = []
duplicate_apps = []
for apps in gps_apps_data:
    if apps[0] in unique_apps:
        duplicate_apps.append(apps[0])
    unique_apps.append(apps[0])

print('No. of Duplicate Entries in Google Play Store Apps Data:', len(duplicate_apps),'\n')

for apps in gps_apps_data:
    if apps[0] == duplicate_apps[0]:
        print(apps,'\n')
```

    No. of Duplicate Entries in Google Play Store Apps Data: 1181 
    
    ['Quick PDF Scanner + OCR FREE', 'BUSINESS', '4.2', '80805', 'Varies with device', '5,000,000+', 'Free', '0', 'Everyone', 'Business', 'February 26, 2018', 'Varies with device', '4.0.3 and up'] 
    
    ['Quick PDF Scanner + OCR FREE', 'BUSINESS', '4.2', '80805', 'Varies with device', '5,000,000+', 'Free', '0', 'Everyone', 'Business', 'February 26, 2018', 'Varies with device', '4.0.3 and up'] 
    
    ['Quick PDF Scanner + OCR FREE', 'BUSINESS', '4.2', '80804', 'Varies with device', '5,000,000+', 'Free', '0', 'Everyone', 'Business', 'February 26, 2018', 'Varies with device', '4.0.3 and up'] 
    


As you can see from above, the no. of duplicate entries is really huge, thus before going further with the analysis, we should first clean the data, and then do our analysis on the same.

As the data is taken on different time, the main difference in the duplicate entries is the no. of rating, which we can see from the above data provided. Thus we have to remove all the duplicate ones, except the one which have the highest no. of rating, as it shows the latest data of that particular app.


```python
reviews_max = {}
for apps in gps_apps_data[1:]:
    name = apps[0]
    n_reviews = float(apps[3])
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
    if name not in reviews_max:
        reviews_max[name] = n_reviews
        
print('No. of Unique Apps in reviews_max:', len(reviews_max),'\n')

android_clean = []
already_added = []

for apps in gps_apps_data[1:]:
    name = apps[0]
    n_reviews = float(apps[3])
    if name not in already_added and n_reviews == reviews_max[name]:
        android_clean.append(apps)
        already_added.append(name)
        
print('No. of Unique Apps in android_clean:', len(android_clean),'\n')
```

    No. of Unique Apps in reviews_max: 9659 
    
    No. of Unique Apps in android_clean: 9659 
    


As you can see above, we first made a dictionary `reviews_max` with all the apps name as the key and the **highest** review of that particular app as the value.

Then with the help of two list, we divided the current list of google apps to `android_clean` and `already_added`. One to store our cleaned data set. And the other to help us to keep track of apps that we already added.

This is done with the help of dictionary we created before. We only appended the apps details which have the highest number of reviews among the duplicates using the dictionary.


```python
def english_or_not(string):
    check = 0
    for letter in string:
        if ord(letter) > 127:
            check += 1
            if check == 3:
                return False
    return True

print('Is Instagram proper/almost English:',english_or_not('Instagram'))
print('Is 爱奇艺PPS -《欢乐颂2》电视剧热播 proper/almost English:',english_or_not('爱奇艺PPS -《欢乐颂2》电视剧热播'))
print('Is Docs To Go™ Free Office Suite proper/almost English:',english_or_not('Docs To Go™ Free Office Suite'))
print('Is Instachat 😜 proper/almost English:',english_or_not('Instachat 😜'))
```

    Is Instagram proper/almost English: True
    Is 爱奇艺PPS -《欢乐颂2》电视剧热播 proper/almost English: False
    Is Docs To Go™ Free Office Suite proper/almost English: True
    Is Instachat 😜 proper/almost English: True


The above function `english_or_not` is a code to check whether a particular string is English or not. As some character might have been omited due to it's inclusion of characters like `™ and 😜`, we have added a leniency that, the function will only call that name not English if there are more than 3 non english character.


```python
english_gps_apps_data = []
english_ios_apps_data = []

def check_english_apps(old_dataset,name_column):
    new_dataset = []
    for apps in old_dataset:
        if english_or_not(apps[name_column]):
            new_dataset.append(apps)
    return new_dataset

english_gps_apps_data = check_english_apps(android_clean,0)
english_ios_apps_data = check_english_apps(ios_apps_data[1:],1)

print('No. of Unique English Google Play Store Apps: ',len(english_gps_apps_data))
print('No. of Unique English IOS Apps: ',len(english_ios_apps_data))
```

    No. of Unique English Google Play Store Apps:  9597
    No. of Unique English IOS Apps:  6155


With the previous implemented function `english_or_not` we checked all the entries in Google Play Store Apps and iOS apps and removed those which are not English as our target market is English speaking audience.


```python
free_gps_apps = []
free_ios_apps = []

def take_free_apps(old_dataset,price_column,price_value):
    new_dataset=[]
    for apps in old_dataset:
        if apps[price_column] == price_value:
            new_dataset.append(apps)
    return new_dataset

free_gps_apps = take_free_apps(english_gps_apps_data,7,'0')
free_ios_apps = take_free_apps(english_ios_apps_data,4,'0.0')

print(len(free_gps_apps))
print(len(free_ios_apps))
```

    8848
    3203


As we mentioned, we only build apps that are free to download and install, and our main source of revenue consists of in-app ads. Our data sets contain both free and non-free apps, and we'll need to isolate only the free apps for our analysis.

Thus we use the above method `take_free_apps` to remove all the paid apps from the list.

## Validation Strategy

Our validation strategy for an app idea is comprised of three steps:

1. Build a minimal Android version of the app, and add it to Google Play.
2. If the app has a good response from users, we then develop it further.
3. If the app is profitable after six months, we also build an iOS version of the app and add it to the App Store.

Because our end goal is to add the app on both the App Store and Google Play, we need to find app profiles that are successful on both markets. For instance, a profile that might work well for both markets might be a productivity app that makes use of gamification.


```python
common_gps_category = {}
common_gps_genre = {}
common_ios_genre = {}

def column_frequency_dictionary_maker(dataset,column_num):
    common_genre = {}
    for apps in dataset:
        genre = apps[column_num]
        if genre in common_genre:
            common_genre[genre] += 1
        else:
            common_genre[genre] = 1
    return common_genre

def dictionary_display(dictionary):
    for element in dictionary:
        print(element,':',dictionary[element])

common_gps_category = column_frequency_dictionary_maker(free_gps_apps,1)
common_gps_genre = column_frequency_dictionary_maker(free_gps_apps,9)
common_ios_genre = column_frequency_dictionary_maker(free_ios_apps,11)

print('Common Category in Google Play Stores are:\n\n')
dictionary_display(common_gps_category)
print('\n\nCommon Genre in Google Play Stores are:\n\n')
dictionary_display(common_gps_genre)
print('\n\nCommon Genre in iOS are:\n\n')
dictionary_display(common_ios_genre)
```

    Common Category in Google Play Stores are:
    
    
    COMICS : 54
    EDUCATION : 103
    AUTO_AND_VEHICLES : 82
    VIDEO_PLAYERS : 159
    DATING : 165
    LIFESTYLE : 344
    SHOPPING : 199
    ART_AND_DESIGN : 57
    PERSONALIZATION : 294
    SOCIAL : 236
    TOOLS : 748
    MEDICAL : 313
    FAMILY : 1676
    WEATHER : 70
    HEALTH_AND_FITNESS : 273
    PHOTOGRAPHY : 261
    ENTERTAINMENT : 85
    COMMUNICATION : 286
    MAPS_AND_NAVIGATION : 123
    EVENTS : 63
    SPORTS : 300
    NEWS_AND_MAGAZINES : 248
    HOUSE_AND_HOME : 71
    GAME : 858
    TRAVEL_AND_LOCAL : 207
    LIBRARIES_AND_DEMO : 83
    BOOKS_AND_REFERENCE : 189
    FOOD_AND_DRINK : 110
    BEAUTY : 53
    FINANCE : 328
    PARENTING : 58
    PRODUCTIVITY : 345
    BUSINESS : 407
    
    
    Common Genre in Google Play Stores are:
    
    
    Casual;Pretend Play : 21
    Arcade;Pretend Play : 1
    Sports : 306
    Travel & Local : 206
    Finance : 328
    Beauty : 53
    Art & Design;Action & Adventure : 1
    Educational;Action & Adventure : 3
    Adventure;Action & Adventure : 3
    Auto & Vehicles : 82
    Education;Creativity : 4
    Comics : 53
    Role Playing;Action & Adventure : 3
    Parenting;Education : 7
    Personalization : 294
    House & Home : 71
    Trivia;Education : 1
    Education;Education : 30
    Art & Design;Pretend Play : 1
    Music : 18
    Entertainment;Brain Games : 7
    Travel & Local;Action & Adventure : 1
    Health & Fitness;Education : 1
    Food & Drink : 110
    Lifestyle;Pretend Play : 1
    Casual;Music & Video : 1
    Art & Design : 53
    Word : 23
    Casual : 156
    Business : 407
    Photography : 261
    Casual;Creativity : 6
    Educational;Creativity : 3
    Tools : 747
    Strategy : 81
    Music;Music & Video : 2
    Video Players & Editors : 157
    Education;Action & Adventure : 3
    Simulation : 181
    Communication;Creativity : 1
    Entertainment;Pretend Play : 2
    Sports;Action & Adventure : 2
    Shopping : 199
    Education;Music & Video : 3
    Role Playing : 83
    Educational;Brain Games : 6
    Trivia : 37
    Maps & Navigation : 123
    Educational;Pretend Play : 8
    Communication : 286
    Entertainment;Music & Video : 15
    Adventure : 59
    Music & Audio;Music & Video : 1
    Strategy;Action & Adventure : 1
    Health & Fitness;Action & Adventure : 1
    Simulation;Pretend Play : 2
    Simulation;Action & Adventure : 7
    Libraries & Demo : 83
    Arcade;Action & Adventure : 11
    Art & Design;Creativity : 6
    Casual;Brain Games : 12
    Racing : 88
    Education : 474
    Books & Reference;Education : 1
    Entertainment;Education : 1
    Entertainment;Action & Adventure : 3
    Strategy;Education : 1
    Casino : 37
    Board;Brain Games : 7
    Tools;Education : 1
    Dating : 165
    Education;Pretend Play : 5
    Education;Brain Games : 3
    Adventure;Education : 1
    Parenting : 44
    Puzzle;Brain Games : 15
    Parenting;Music & Video : 6
    Card;Action & Adventure : 1
    Puzzle;Creativity : 2
    Video Players & Editors;Music & Video : 2
    Entertainment;Creativity : 3
    Educational : 33
    Health & Fitness : 273
    Lifestyle;Education : 1
    Casual;Education : 2
    Role Playing;Pretend Play : 4
    Medical : 313
    Puzzle : 100
    Productivity : 345
    Role Playing;Brain Games : 1
    Casual;Action & Adventure : 12
    Puzzle;Education : 1
    Puzzle;Action & Adventure : 3
    Educational;Education : 35
    Action;Action & Adventure : 9
    Comics;Creativity : 1
    Entertainment : 538
    Racing;Pretend Play : 1
    Board;Action & Adventure : 2
    News & Magazines : 248
    Books & Reference : 189
    Action : 274
    Video Players & Editors;Creativity : 1
    Arcade : 163
    Social : 236
    Card : 40
    Events : 63
    Strategy;Creativity : 1
    Weather : 70
    Lifestyle : 343
    Simulation;Education : 1
    Parenting;Brain Games : 1
    Board : 34
    Racing;Action & Adventure : 15
    
    
    Common Genre in iOS are:
    
    
    News : 43
    Education : 118
    Sports : 69
    Business : 17
    Finance : 35
    Entertainment : 251
    Photo & Video : 160
    Book : 12
    Games : 1866
    Catalogs : 4
    Social Networking : 106
    Shopping : 83
    Utilities : 79
    Reference : 17
    Music : 66
    Health & Fitness : 65
    Food & Drink : 26
    Medical : 6
    Lifestyle : 50
    Productivity : 56
    Navigation : 6
    Travel : 40
    Weather : 28


The above shows the genre/category and the number of apps in each genre/category.


```python
common_gps_category_percentage = {}
common_gps_genre_percentage = {}
common_ios_genre_percentage = {}

def total_of_dict_values(dictionary):
    total = 0
    for element in dictionary:
        total += dictionary[element]
    return total

def dictionary_percentage_finder(dictionary):
    new_dictionary = {}
    total = total_of_dict_values(dictionary)
    for element in dictionary:
        new_dictionary[element] = (dictionary[element]/total) * 100
    return new_dictionary

common_gps_category_percentage = dictionary_percentage_finder(common_gps_category)
common_gps_genre_percentage = dictionary_percentage_finder(common_gps_genre)
common_ios_genre_percentage = dictionary_percentage_finder(common_ios_genre)

print('Common Category Percentage in Google Play Stores are:\n\n')
dictionary_display(common_gps_category_percentage)
print('\n\nCommon Genre Percentage in Google Play Stores are:\n\n')
dictionary_display(common_gps_genre_percentage)
print('\n\nCommon Genre Percentage in iOS are:\n\n')
dictionary_display(common_ios_genre_percentage)
```

    Common Category Percentage in Google Play Stores are:
    
    
    COMICS : 0.6103074141048824
    EDUCATION : 1.164104882459313
    AUTO_AND_VEHICLES : 0.9267631103074141
    DATING : 1.8648282097649187
    LIFESTYLE : 3.887884267631103
    SHOPPING : 2.2490958408679926
    ART_AND_DESIGN : 0.6442133815551537
    BEAUTY : 0.599005424954792
    SOCIAL : 2.667269439421338
    COMMUNICATION : 3.2323688969258586
    MEDICAL : 3.5375226039783
    SPORTS : 3.390596745027125
    WEATHER : 0.7911392405063291
    HEALTH_AND_FITNESS : 3.0854430379746836
    PHOTOGRAPHY : 2.949819168173599
    ENTERTAINMENT : 0.9606690777576853
    TOOLS : 8.453887884267631
    MAPS_AND_NAVIGATION : 1.3901446654611211
    EVENTS : 0.7120253164556962
    BUSINESS : 4.599909584086799
    FAMILY : 18.942133815551536
    NEWS_AND_MAGAZINES : 2.802893309222423
    HOUSE_AND_HOME : 0.8024412296564195
    GAME : 9.697106690777577
    TRAVEL_AND_LOCAL : 2.3395117540687163
    LIBRARIES_AND_DEMO : 0.9380650994575045
    BOOKS_AND_REFERENCE : 2.1360759493670884
    FOOD_AND_DRINK : 1.2432188065099457
    PERSONALIZATION : 3.322784810126582
    FINANCE : 3.7070524412296564
    PARENTING : 0.6555153707052441
    PRODUCTIVITY : 3.899186256781193
    VIDEO_PLAYERS : 1.7970162748643763
    
    
    Common Genre Percentage in Google Play Stores are:
    
    
    Casual;Pretend Play : 0.23734177215189875
    Arcade;Pretend Play : 0.011301989150090416
    Sports : 3.4584086799276674
    Travel & Local : 2.328209764918626
    Finance : 3.7070524412296564
    Beauty : 0.599005424954792
    Art & Design;Action & Adventure : 0.011301989150090416
    Educational;Action & Adventure : 0.033905967450271246
    Adventure;Action & Adventure : 0.033905967450271246
    Auto & Vehicles : 0.9267631103074141
    Sports;Action & Adventure : 0.022603978300180832
    Comics : 0.599005424954792
    Role Playing;Action & Adventure : 0.033905967450271246
    Parenting;Education : 0.07911392405063292
    Personalization : 3.322784810126582
    House & Home : 0.8024412296564195
    Trivia;Education : 0.011301989150090416
    Education;Education : 0.33905967450271246
    Role Playing;Pretend Play : 0.045207956600361664
    Music : 0.2034358047016275
    Entertainment;Brain Games : 0.07911392405063292
    Medical : 3.5375226039783
    Health & Fitness;Education : 0.011301989150090416
    Strategy : 0.9154611211573236
    Shopping : 2.2490958408679926
    Casual;Music & Video : 0.011301989150090416
    Art & Design : 0.599005424954792
    Word : 0.25994575045207957
    Casual : 1.763110307414105
    Business : 4.599909584086799
    Photography : 2.949819168173599
    Lifestyle;Pretend Play : 0.011301989150090416
    Food & Drink : 1.2432188065099457
    Music;Music & Video : 0.022603978300180832
    Arcade : 1.842224231464738
    Education;Action & Adventure : 0.033905967450271246
    Simulation : 2.0456600361663653
    Role Playing;Brain Games : 0.011301989150090416
    Entertainment;Pretend Play : 0.022603978300180832
    Education;Creativity : 0.045207956600361664
    Strategy;Action & Adventure : 0.011301989150090416
    Education;Music & Video : 0.033905967450271246
    Dating : 1.8648282097649187
    Educational;Brain Games : 0.06781193490054249
    Trivia : 0.4181735985533454
    Maps & Navigation : 1.3901446654611211
    Educational;Pretend Play : 0.09041591320072333
    Books & Reference;Education : 0.011301989150090416
    Entertainment;Music & Video : 0.16952983725135623
    Casino : 0.4181735985533454
    Music & Audio;Music & Video : 0.011301989150090416
    Education;Brain Games : 0.033905967450271246
    Health & Fitness;Action & Adventure : 0.011301989150090416
    Simulation;Pretend Play : 0.022603978300180832
    Events : 0.7120253164556962
    Libraries & Demo : 0.9380650994575045
    Arcade;Action & Adventure : 0.12432188065099457
    Art & Design;Creativity : 0.06781193490054249
    Casual;Brain Games : 0.13562386980108498
    Tools : 8.44258589511754
    Education : 5.357142857142857
    Communication : 3.2323688969258586
    Casual;Creativity : 0.06781193490054249
    Travel & Local;Action & Adventure : 0.011301989150090416
    Strategy;Education : 0.011301989150090416
    Board;Brain Games : 0.07911392405063292
    Tools;Education : 0.011301989150090416
    Role Playing : 0.9380650994575045
    Education;Pretend Play : 0.05650994575045208
    Adventure;Education : 0.011301989150090416
    Parenting : 0.4972875226039783
    Puzzle;Brain Games : 0.16952983725135623
    Parenting;Music & Video : 0.06781193490054249
    Card;Action & Adventure : 0.011301989150090416
    Puzzle;Creativity : 0.022603978300180832
    Video Players & Editors;Music & Video : 0.022603978300180832
    Entertainment;Creativity : 0.033905967450271246
    Educational : 0.3729656419529837
    Health & Fitness : 3.0854430379746836
    Lifestyle;Education : 0.011301989150090416
    Casual;Education : 0.022603978300180832
    Art & Design;Pretend Play : 0.011301989150090416
    Adventure : 0.6668173598553345
    Puzzle : 1.1301989150090417
    Productivity : 3.899186256781193
    Communication;Creativity : 0.011301989150090416
    Casual;Action & Adventure : 0.13562386980108498
    Puzzle;Education : 0.011301989150090416
    Puzzle;Action & Adventure : 0.033905967450271246
    Social : 2.667269439421338
    Action;Action & Adventure : 0.10171790235081375
    Entertainment;Action & Adventure : 0.033905967450271246
    Comics;Creativity : 0.011301989150090416
    Entertainment : 6.080470162748644
    Entertainment;Education : 0.011301989150090416
    Racing;Pretend Play : 0.011301989150090416
    Board;Action & Adventure : 0.022603978300180832
    News & Magazines : 2.802893309222423
    Books & Reference : 2.1360759493670884
    Educational;Creativity : 0.033905967450271246
    Video Players & Editors;Creativity : 0.011301989150090416
    Video Players & Editors : 1.7744122965641953
    Educational;Education : 0.39556962025316456
    Action : 3.096745027124774
    Card : 0.45207956600361665
    Simulation;Action & Adventure : 0.07911392405063292
    Strategy;Creativity : 0.011301989150090416
    Racing;Action & Adventure : 0.16952983725135623
    Racing : 0.9945750452079566
    Lifestyle : 3.8765822784810124
    Simulation;Education : 0.011301989150090416
    Parenting;Brain Games : 0.011301989150090416
    Board : 0.3842676311030741
    Weather : 0.7911392405063291
    
    
    Common Genre Percentage in iOS are:
    
    
    News : 1.3424914142990947
    Education : 3.6840462066812365
    Sports : 2.1542304089915705
    Business : 0.5307524196066188
    Finance : 1.0927255697783327
    Entertainment : 7.836403371838902
    Photo & Video : 4.995316890415236
    Book : 0.3746487667811427
    Productivity : 1.7483609116453322
    Games : 58.25788323446769
    Catalogs : 0.1248829222603809
    Social Networking : 3.3093974399000934
    Travel : 1.248829222603809
    Utilities : 2.466437714642523
    Reference : 0.5307524196066188
    Navigation : 0.18732438339057134
    Health & Fitness : 2.0293474867311896
    Medical : 0.18732438339057134
    Lifestyle : 1.5610365282547611
    Music : 2.0605682172962845
    Food & Drink : 0.8117389946924758
    Shopping : 2.5913206369029034
    Weather : 0.8741804558226661


The above shows the genre/category and the percentage of apps in each category.


```python
def sort_dict(dictionary):
    table_display = []
    for key in dictionary:
        key_val_as_tuple = (dictionary[key], key)
        table_display.append(key_val_as_tuple)

    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])
        
print('Sorted Common Category Percentage in Google Play Stores are:\n\n')
sort_dict(common_gps_category_percentage)
print('\n\nSorted Common Genre Percentage in Google Play Stores are:\n\n')
sort_dict(common_gps_genre_percentage)
print('\n\nSorted Common Genre Percentage in iOS are:\n\n')
sort_dict(common_ios_genre_percentage)
```

    Sorted Common Category Percentage in Google Play Stores are:
    
    
    FAMILY : 18.942133815551536
    GAME : 9.697106690777577
    TOOLS : 8.453887884267631
    BUSINESS : 4.599909584086799
    PRODUCTIVITY : 3.899186256781193
    LIFESTYLE : 3.887884267631103
    FINANCE : 3.7070524412296564
    MEDICAL : 3.5375226039783
    SPORTS : 3.390596745027125
    PERSONALIZATION : 3.322784810126582
    COMMUNICATION : 3.2323688969258586
    HEALTH_AND_FITNESS : 3.0854430379746836
    PHOTOGRAPHY : 2.949819168173599
    NEWS_AND_MAGAZINES : 2.802893309222423
    SOCIAL : 2.667269439421338
    TRAVEL_AND_LOCAL : 2.3395117540687163
    SHOPPING : 2.2490958408679926
    BOOKS_AND_REFERENCE : 2.1360759493670884
    DATING : 1.8648282097649187
    VIDEO_PLAYERS : 1.7970162748643763
    MAPS_AND_NAVIGATION : 1.3901446654611211
    FOOD_AND_DRINK : 1.2432188065099457
    EDUCATION : 1.164104882459313
    ENTERTAINMENT : 0.9606690777576853
    LIBRARIES_AND_DEMO : 0.9380650994575045
    AUTO_AND_VEHICLES : 0.9267631103074141
    HOUSE_AND_HOME : 0.8024412296564195
    WEATHER : 0.7911392405063291
    EVENTS : 0.7120253164556962
    PARENTING : 0.6555153707052441
    ART_AND_DESIGN : 0.6442133815551537
    COMICS : 0.6103074141048824
    BEAUTY : 0.599005424954792
    
    
    Sorted Common Genre Percentage in Google Play Stores are:
    
    
    Tools : 8.44258589511754
    Entertainment : 6.080470162748644
    Education : 5.357142857142857
    Business : 4.599909584086799
    Productivity : 3.899186256781193
    Lifestyle : 3.8765822784810124
    Finance : 3.7070524412296564
    Medical : 3.5375226039783
    Sports : 3.4584086799276674
    Personalization : 3.322784810126582
    Communication : 3.2323688969258586
    Action : 3.096745027124774
    Health & Fitness : 3.0854430379746836
    Photography : 2.949819168173599
    News & Magazines : 2.802893309222423
    Social : 2.667269439421338
    Travel & Local : 2.328209764918626
    Shopping : 2.2490958408679926
    Books & Reference : 2.1360759493670884
    Simulation : 2.0456600361663653
    Dating : 1.8648282097649187
    Arcade : 1.842224231464738
    Video Players & Editors : 1.7744122965641953
    Casual : 1.763110307414105
    Maps & Navigation : 1.3901446654611211
    Food & Drink : 1.2432188065099457
    Puzzle : 1.1301989150090417
    Racing : 0.9945750452079566
    Role Playing : 0.9380650994575045
    Libraries & Demo : 0.9380650994575045
    Auto & Vehicles : 0.9267631103074141
    Strategy : 0.9154611211573236
    House & Home : 0.8024412296564195
    Weather : 0.7911392405063291
    Events : 0.7120253164556962
    Adventure : 0.6668173598553345
    Comics : 0.599005424954792
    Beauty : 0.599005424954792
    Art & Design : 0.599005424954792
    Parenting : 0.4972875226039783
    Card : 0.45207956600361665
    Trivia : 0.4181735985533454
    Casino : 0.4181735985533454
    Educational;Education : 0.39556962025316456
    Board : 0.3842676311030741
    Educational : 0.3729656419529837
    Education;Education : 0.33905967450271246
    Word : 0.25994575045207957
    Casual;Pretend Play : 0.23734177215189875
    Music : 0.2034358047016275
    Racing;Action & Adventure : 0.16952983725135623
    Puzzle;Brain Games : 0.16952983725135623
    Entertainment;Music & Video : 0.16952983725135623
    Casual;Brain Games : 0.13562386980108498
    Casual;Action & Adventure : 0.13562386980108498
    Arcade;Action & Adventure : 0.12432188065099457
    Action;Action & Adventure : 0.10171790235081375
    Educational;Pretend Play : 0.09041591320072333
    Simulation;Action & Adventure : 0.07911392405063292
    Parenting;Education : 0.07911392405063292
    Entertainment;Brain Games : 0.07911392405063292
    Board;Brain Games : 0.07911392405063292
    Parenting;Music & Video : 0.06781193490054249
    Educational;Brain Games : 0.06781193490054249
    Casual;Creativity : 0.06781193490054249
    Art & Design;Creativity : 0.06781193490054249
    Education;Pretend Play : 0.05650994575045208
    Role Playing;Pretend Play : 0.045207956600361664
    Education;Creativity : 0.045207956600361664
    Role Playing;Action & Adventure : 0.033905967450271246
    Puzzle;Action & Adventure : 0.033905967450271246
    Entertainment;Creativity : 0.033905967450271246
    Entertainment;Action & Adventure : 0.033905967450271246
    Educational;Creativity : 0.033905967450271246
    Educational;Action & Adventure : 0.033905967450271246
    Education;Music & Video : 0.033905967450271246
    Education;Brain Games : 0.033905967450271246
    Education;Action & Adventure : 0.033905967450271246
    Adventure;Action & Adventure : 0.033905967450271246
    Video Players & Editors;Music & Video : 0.022603978300180832
    Sports;Action & Adventure : 0.022603978300180832
    Simulation;Pretend Play : 0.022603978300180832
    Puzzle;Creativity : 0.022603978300180832
    Music;Music & Video : 0.022603978300180832
    Entertainment;Pretend Play : 0.022603978300180832
    Casual;Education : 0.022603978300180832
    Board;Action & Adventure : 0.022603978300180832
    Video Players & Editors;Creativity : 0.011301989150090416
    Trivia;Education : 0.011301989150090416
    Travel & Local;Action & Adventure : 0.011301989150090416
    Tools;Education : 0.011301989150090416
    Strategy;Education : 0.011301989150090416
    Strategy;Creativity : 0.011301989150090416
    Strategy;Action & Adventure : 0.011301989150090416
    Simulation;Education : 0.011301989150090416
    Role Playing;Brain Games : 0.011301989150090416
    Racing;Pretend Play : 0.011301989150090416
    Puzzle;Education : 0.011301989150090416
    Parenting;Brain Games : 0.011301989150090416
    Music & Audio;Music & Video : 0.011301989150090416
    Lifestyle;Pretend Play : 0.011301989150090416
    Lifestyle;Education : 0.011301989150090416
    Health & Fitness;Education : 0.011301989150090416
    Health & Fitness;Action & Adventure : 0.011301989150090416
    Entertainment;Education : 0.011301989150090416
    Communication;Creativity : 0.011301989150090416
    Comics;Creativity : 0.011301989150090416
    Casual;Music & Video : 0.011301989150090416
    Card;Action & Adventure : 0.011301989150090416
    Books & Reference;Education : 0.011301989150090416
    Art & Design;Pretend Play : 0.011301989150090416
    Art & Design;Action & Adventure : 0.011301989150090416
    Arcade;Pretend Play : 0.011301989150090416
    Adventure;Education : 0.011301989150090416
    
    
    Sorted Common Genre Percentage in iOS are:
    
    
    Games : 58.25788323446769
    Entertainment : 7.836403371838902
    Photo & Video : 4.995316890415236
    Education : 3.6840462066812365
    Social Networking : 3.3093974399000934
    Shopping : 2.5913206369029034
    Utilities : 2.466437714642523
    Sports : 2.1542304089915705
    Music : 2.0605682172962845
    Health & Fitness : 2.0293474867311896
    Productivity : 1.7483609116453322
    Lifestyle : 1.5610365282547611
    News : 1.3424914142990947
    Travel : 1.248829222603809
    Finance : 1.0927255697783327
    Weather : 0.8741804558226661
    Food & Drink : 0.8117389946924758
    Reference : 0.5307524196066188
    Business : 0.5307524196066188
    Book : 0.3746487667811427
    Navigation : 0.18732438339057134
    Medical : 0.18732438339057134
    Catalogs : 0.1248829222603809


### Points we can infer from the above data about iOS:

1. The most common genre in iOS is Games which constitutes more than half of the entire apps. And the next genre below is it Entertainment.

2. If you check the top three apps, which constitutes around 71% of the entire apps is mostly based on fun (games, entertainment, photo & video) than utility.

3. From the above two, we can clearly say that, most of the current developers are focused on developing apps in fun genre, rather than utility. And possibly, that captures the most amount of audience as well.

### Points we can infer from the above data about Google Play Store:

1. The most common apps are related to Family & Tools

2. The number of apps of the utility is more than the fun apps.

3. If we compare iOS with Google Play Store Apps, iOS have more apps in the fun section, while Google Play Store has more apps on the utility section.

4. Based on the above details, creating a utility app on the Google Play Store seems much better.


```python
total_rating = column_frequency_dictionary_maker(free_ios_apps,5)

def avg_user_rating_finder(dictionary, dataset, type_col, amount_col):
    for types in dictionary:
        total = 0
        len_type = 0
        for apps in dataset:
            type_app = apps[type_col]
            if type_app == types:
                user_rating = float(apps[amount_col].replace('+','').replace(',',''))
                total += user_rating
                len_type += 1
        avg_user_rating = total / len_type
        print(types,':',avg_user_rating)

avg_user_rating_finder(common_ios_genre, free_ios_apps, 11, 5)
```

    News : 21248.023255813954
    Education : 7003.983050847458
    Sports : 23008.898550724636
    Business : 7491.117647058823
    Finance : 32367.02857142857
    Entertainment : 14195.358565737051
    Photo & Video : 28441.54375
    Book : 46384.916666666664
    Games : 22886.36709539121
    Catalogs : 4004.0
    Social Networking : 71548.34905660378
    Shopping : 27230.734939759037
    Utilities : 19156.493670886077
    Reference : 79350.4705882353
    Music : 57326.530303030304
    Health & Fitness : 23298.015384615384
    Food & Drink : 33333.92307692308
    Medical : 612.0
    Lifestyle : 16815.48
    Productivity : 21028.410714285714
    Navigation : 86090.33333333333
    Travel : 28243.8
    Weather : 52279.892857142855


Based on the avg number of rating, we can find out how many active users are there in a particular genre and based on the above values, it now seems like Navigation, Reference and Social Network is the most famous.


```python
avg_user_rating_finder(common_gps_category, free_gps_apps, 1, 5)
```

    COMICS : 832613.8888888889
    EDUCATION : 1833495.145631068
    AUTO_AND_VEHICLES : 647317.8170731707
    VIDEO_PLAYERS : 24727872.452830188
    DATING : 854028.8303030303
    LIFESTYLE : 1446158.2238372094
    SHOPPING : 7036877.311557789
    ART_AND_DESIGN : 1986335.0877192982
    PERSONALIZATION : 5201482.6122448975
    SOCIAL : 23253652.127118643
    TOOLS : 10830251.970588235
    MEDICAL : 120550.61980830671
    FAMILY : 3695641.8198090694
    WEATHER : 5145550.285714285
    HEALTH_AND_FITNESS : 4188821.9853479853
    PHOTOGRAPHY : 17840110.40229885
    ENTERTAINMENT : 11640705.88235294
    COMMUNICATION : 38590581.08741259
    MAPS_AND_NAVIGATION : 4049274.6341463416
    EVENTS : 253542.22222222222
    SPORTS : 3650602.276666667
    NEWS_AND_MAGAZINES : 9549178.467741935
    HOUSE_AND_HOME : 1360598.042253521
    GAME : 15544014.51048951
    TRAVEL_AND_LOCAL : 13984077.710144928
    LIBRARIES_AND_DEMO : 638503.734939759
    BOOKS_AND_REFERENCE : 8814199.78835979
    FOOD_AND_DRINK : 1924897.7363636363
    BEAUTY : 513151.88679245283
    FINANCE : 1387692.475609756
    PARENTING : 542603.6206896552
    PRODUCTIVITY : 16787331.344927534
    BUSINESS : 1712290.1474201474


Based on above values, it now seems like Communication is the clear winner, with closely followed by Video Players & Social.
