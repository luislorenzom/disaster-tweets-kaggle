import pandas as pd

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

