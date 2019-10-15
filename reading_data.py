import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

train = pd.read_csv('data/train.csv')

print(train.shape)
# (913000, 4)
print(train.columns)
# ['date', 'store', 'item', 'sales']

print(train.head())

# convert string to datetime object
train['date'] = pd.to_datetime(train['date'])

# subset data to store 1 and item 1
train_filtered = train[(train.store == 2) & (train.item == 1)].copy()







plt.plot(train_filtered.date, train_filtered.sales, 'red')
plt.show()