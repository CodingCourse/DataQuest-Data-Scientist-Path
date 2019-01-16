#!/usr/bin/env python
# coding: utf-8

# # Profitable App Profiles for the App Store and Google Play Markets
# 
# Mobile Apps usage are on the rise and people nowadays are more inclined to use a mobile platform than a web platform. This analysis is to understand more on the type of apps most people use, it's demographics and other important factors.
# 
# The goal is to find those app profiles which produce the most revenue based on the analysis we have done.

# In[8]:


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


# The above shows the coloumns in each of the csv files. The first one shows the coloumns in IOS Apps Data. For more details of the same, you may check the [documentation][1]. The second one shows the coloumns in Google Play Store's Apps Data. For more details of the same, you may check this [documentation][2]
# 
# In addition to that, after each list of the coloumns, the no. of coloumns and rows are also shown. From the above we can see, how many apps details from each platform we currently have.
# 
# [1]: https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps/home
# [2]: https://www.kaggle.com/lava18/google-play-store-apps/home

# In[18]:


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


# As you can see from above, the no. of duplicate entries is really huge, thus before going further with the analysis, we should first clean the data, and then do our analysis on the same.
# 
# As the data is taken on different time, the main difference in the duplicate entries is the no. of rating, which we can see from the above data provided. Thus we have to remove all the duplicate ones, except the one which have the highest no. of rating, as it shows the latest data of that particular app.

# In[34]:


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


# As you can see above, we first made a dictionary `reviews_max` with all the apps name as the key and the **highest** review of that particular app as the value.
# 
# Then with the help of two list, we divided the current list of google apps to `android_clean` and `already_added`. One to store our cleaned data set. And the other to help us to keep track of apps that we already added.
# 
# This is done with the help of dictionary we created before. We only appended the apps details which have the highest number of reviews among the duplicates using the dictionary.

# In[35]:


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


# The above function `english_or_not` is a code to check whether a particular string is English or not. As some character might have been omited due to it's inclusion of characters like `™ and 😜`, we have added a leniency that, the function will only call that name not English if there are more than 3 non english character.

# In[57]:


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


# With the previous implemented function `english_or_not` we checked all the entries in Google Play Store Apps and iOS apps and removed those which are not English as our target market is English speaking audience.

# In[58]:


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


# As we mentioned, we only build apps that are free to download and install, and our main source of revenue consists of in-app ads. Our data sets contain both free and non-free apps, and we'll need to isolate only the free apps for our analysis.
# 
# Thus we use the above method `take_free_apps` to remove all the paid apps from the list.
# 
# ## Validation Strategy
# 
# Our validation strategy for an app idea is comprised of three steps:
# 
# 1. Build a minimal Android version of the app, and add it to Google Play.
# 2. If the app has a good response from users, we then develop it further.
# 3. If the app is profitable after six months, we also build an iOS version of the app and add it to the App Store.
# 
# Because our end goal is to add the app on both the App Store and Google Play, we need to find app profiles that are successful on both markets. For instance, a profile that might work well for both markets might be a productivity app that makes use of gamification.

# In[111]:


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


# The above shows the genre/category and the number of apps in each genre/category.

# In[109]:


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


# The above shows the genre/category and the percentage of apps in each category.

# In[114]:


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


# ### Points we can infer from the above data about iOS:
# 
# 1. The most common genre in iOS is Games which constitutes more than half of the entire apps. And the next genre below is it Entertainment.
# 
# 2. If you check the top three apps, which constitutes around 71% of the entire apps is mostly based on fun (games, entertainment, photo & video) than utility.
# 
# 3. From the above two, we can clearly say that, most of the current developers are focused on developing apps in fun genre, rather than utility. And possibly, that captures the most amount of audience as well.
# 
# ### Points we can infer from the above data about Google Play Store:
# 
# 1. The most common apps are related to Family & Tools
# 
# 2. The number of apps of the utility is more than the fun apps.
# 
# 3. If we compare iOS with Google Play Store Apps, iOS have more apps in the fun section, while Google Play Store has more apps on the utility section.
# 
# 4. Based on the above details, creating a utility app on the Google Play Store seems much better.

# In[123]:


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


# Based on the avg number of rating, we can find out how many active users are there in a particular genre and based on the above values, it now seems like Navigation, Reference and Social Network is the most famous.

# In[125]:


avg_user_rating_finder(common_gps_category, free_gps_apps, 1, 5)


# Based on above values, it now seems like Communication is the clear winner, with closely followed by Video Players & Social.
