## 1. Introduction ##

from csv import reader
hn = list(reader(open('hacker_news.csv')))
hn = hn[1:]
hn_num_rows = len(hn)

## 2. The Regular Expression Module ##

import re
python_mentions = 0
pattern = "[Pp]ython"
for post in hn:
    if re.search(pattern,post[1]):
        python_mentions += 1

## 3. Character Classes and Quantifiers ##

tag_count = 0
pattern = "\[\w+\]"

for row in hn:
    if re.search(pattern,row[1]):
        tag_count += 1

## 4. Accessing the Matching Text ##

pattern = r"\[\w+\]"
tag_freq = {}

for row in hn:
    re_obj = re.search(pattern,row[1])
    if re_obj:
        re_obj_group = re_obj.group()
        if re_obj_group in tag_freq:
            tag_freq[re_obj_group] += 1
        else:
            tag_freq[re_obj_group] = 1

## 5. Using Capture Groups to Extract Data ##

py_versions = {}
pattern = r'[Pp]ython (\d\.*\d*\.*\d*)'

for row in hn:
    title = row[1]
    re_obj = re.search(pattern,title)
    if re_obj:
        re_obj_group = re_obj.group(1)
        if re_obj_group in py_versions:
            py_versions[re_obj_group] += 1
        else:
            py_versions[re_obj_group] = 1

## 6. Negative Character Classes and Word Boundaries ##

def first_10_matches(pattern):
    matches = []
    for story in hn:
        title = story[1]
        if re.search(pattern, title):
            matches.append(title)
        if len(matches) == 10:
            return matches
    return matches

java_mentions = 0
pattern = r'\b[Jj]ava\b'

for row in hn:
    title = row[1]
    if re.search(pattern,title):
        java_mentions += 1

## 7. Matching at the Start and End of Strings ##

beginning_count = 0
ending_count = 0

start_ex = r'^\[\w+\]'
end_ex = r'\[\w+\]$'

for row in hn:
    title = row[1]
    if re.search(start_ex,title):
        beginning_count += 1
    if re.search(end_ex,title):
        ending_count += 1


## 8. Using Lookarounds to Control Matches Based on Surrounding Text ##

c_mentions = 0

pattern = r'(?<!Series\s)\b[Cc]\b(?![\.\+])'

for row in hn:
    if re.search(pattern,row[1]):
        c_mentions += 1

## 9. BackReferences: Using Capture Groups in a RegEx Pattern ##

repeated_words = []

pattern = r'\b(\w+) \1\b'

for row in hn:
    if re.search(pattern,row[1]):
        repeated_words.append(row[1])

## 10. Using Flags to Modify Regex Patterns ##

test_cases = ['email', 'Email', 'e Mail', 'e mail', 'E-mail',
              'e-mail', 'eMail', 'E-Mail', 'EMAIL']

def test_pattern(pattern, flags):
    for tc in test_cases:
        print(re.search(pattern, tc, flags))

email_mentions = 0

pattern = r'e[ \-]?mail'

for row in hn:
    if re.search(pattern,row[1],re.I):
        email_mentions += 1

## 11. Substituting Regular Expression Matches ##

for row in hn:
    row[1] = re.sub('sql', 'SQL', row[1], flags=re.I)


## 12. Challenge: Extracting Domains From URLs ##

test_cases = [
 'http://www.interactivedynamicvideo.com/',
 'http://www.thewire.com/entertainment/2013/04/florida-djs-april-fools-water-joke/63798/',
 'https://www.amazon.com/Technology-Ventures-Enterprise-Thomas-Byers/dp/0073523429',
 'http://www.nytimes.com/2007/11/07/movies/07stein.html?_r=0',
 'http://arstechnica.com/business/2015/10/comcast-and-other-isps-boost-network-investment-despite-net-neutrality/',
 '',
 'http://firstround.com/review/shims-jigs-and-other-woodworking-concepts-to-conquer-technical-debt/',
 'http://evonomics.com/advertising-cannot-maintain-internet-heres-solution/',
 'HTTPS://github.com/keppel/pinn',
 'Http://phys.org/news/2015-09-scale-solar-youve.html',
 'https://iot.seeed.cc',
 'http://www.bfilipek.com/2016/04/custom-deleters-for-c-smart-pointers.html',
 '',
 'http://beta.crowdfireapp.com/?beta=agnipath',
 '',
 'https://www.bostonglobe.com/magazine/2015/12/29/years-later-did-big-dig-deliver/tSb8PIMS4QJUETsMpA7SpI/story.html',
 'https://www.valid.ly'
]

domains = {}
top_domains = {}

pattern = r'(https?://)([\w\.]+)'

for row in hn:
    re_obj = re.search(pattern,row[2],re.I)
    if re_obj:
        re_obj_group = re_obj.group(2)
        if re_obj_group in domains:
            domains[re_obj_group] += 1
        else:
            domains[re_obj_group] = 1

for d, count in domains.items():
    if count > 50:
        top_domains[d] = count