

import DataHelper

data = DataHelper.read_data('./train.csv')

count = {}

for index, row in data.iterrows():
    if(row['Source'] not in count.keys()):
        count[row['Source']] = {0:0, 1:0, 2:0, 3:0}
        count[row['Source']][row['Label']] += 1
    else:
        count[row['Source']][row['Label']] += 1

count_percentage = {}

for elem in count:
    d = count[elem]
    
    #total = d[1] + d[2] + d[3]
    total = d[0] + d[1] + d[2] + d[3]
    
    #count_percentage[elem] = {1:0, 2:0, 3:0}
    count_percentage[elem] = {0:0, 1:0, 2:0, 3:0}
    
    for i in range(0, 3):
        count_percentage[elem][i] = d[i] / total
    
