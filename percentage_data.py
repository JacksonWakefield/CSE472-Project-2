

import DataHelper


#left_index = either Source or Country (mentioned)
def get_percentage_data(left_index):

    data = DataHelper.read_data('./train.csv')

    count = {}
    all_values = {}
    
    for index, row in data.iterrows():
        if(row[left_index] not in count.keys()):
            count[row[left_index]] = {0:0, 1:0, 2:0, 3:0}
            count[row[left_index]][row['Label']] += 1
        else:
            count[row[left_index]][row['Label']] += 1
    
    count_percentage = {}
    
    for elem in count:
        d = count[elem]
        
        #total = d[1] + d[2] + d[3]
        total = d[0] + d[1] + d[2] + d[3]
        
        #count_percentage[elem] = {1:0, 2:0, 3:0}
        count_percentage[elem] = {0:0, 1:0, 2:0, 3:0}
        
        for i in range(0, 3):
            count_percentage[elem][i] = d[i] / total
        
    return count_percentage

    
