import pandas as pd
import json

train = pd.read_csv('dataset/train.csv')
only_location = train[train.location.notnull()]
only_keywords = train[train.keyword.notnull()]

total_records = train.shape[0]
total_location = only_location.shape[0]
total_keywords = only_keywords.shape[0]

print('\nTotal records:\t\t\t{}'.format(total_records))
print('Records with locations:\t\t{}'.format(total_location))
print('Records with keywords:\t\t{}\n'.format(total_keywords))

print('Unique locations:\t\t{}'.format(len(pd.unique(train.location))))
print('Unique keywords:\t\t{}\n'.format(len(pd.unique(train.keyword))))

# Checking dictionaries
with open('dicts/disaster_dictionary.json') as dict_file:
    disaster_dictionary = json.load(dict_file)

with open('dicts/urban_dictionary.json') as dict_file:
    urban_dictionary = json.load(dict_file)

for word in disaster_dictionary:
    sample = train[train['text'].str.contains(word)]
    target_groups = sample.groupby('target').groups
    print('\n{}'.format(word))
    if 1 in target_groups:
        print('class 1: {}'.format(len(target_groups[1])))
    if 0 in target_groups:
        print('class 0: {}'.format(len(target_groups[0])))

for word in urban_dictionary:
    words = [' ' + word +' ', '#' + word]
    sample = train[train['text'].str.contains('|'.join(words))]
    target_groups = sample.groupby('target').groups
    print('\n{}'.format(word))
    if 1 in target_groups:
        print('class 1: {}'.format(len(target_groups[1])))
    if 0 in target_groups:
        print('class 0: {}'.format(len(target_groups[0])))