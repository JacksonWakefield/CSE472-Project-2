

import DataHelper

data = DataHelper.read_data('./test.csv')

count = {}

for index, row in data.iterrows():
    if(row['Source'] not in count.keys()):
        count[row['Source']] = 1
    else:
        count[row['Source']] += 1
