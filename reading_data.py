import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

train = pd.read_csv('data/train.csv')

print(train.shape)
# (913000, 4)
print(train.columns)
# ['date', 'store', 'item', 'sales']

print(train.head())


train['date'] = pd.to_datetime(train['date'])

train_filtered = train[train['store'] == 1]

print(train_filtered.shape)
