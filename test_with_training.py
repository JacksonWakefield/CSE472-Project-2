
submission_name = './submission.csv'
training_name = './train.csv'

import DataHelper

def test_with_training(predictions, min_rnge, max_rnge):
    
    training_data = DataHelper.read_data(training_name)
    
    table = []
    
    for i in range(min_rnge, max_rnge):
        if(predictions[i - min_rnge] == training_data.loc[i, 'Label']):
            table.append(1)
        else:
            table.append(0)            
    
    print(table)

def too_many_ones(predictions, min_rnge, max_rnge, value):
    
    training_data = DataHelper.read_data(training_name)
    
    expected_ones = 0
    retrieved_ones = 0
    
    for i in range(min_rnge, max_rnge):
        
        if(predictions[i-min_rnge] == value):
            retrieved_ones += 1
        
        if(training_data.loc[i, 'Label'] == value):
            expected_ones += 1
    
    if(retrieved_ones > expected_ones):
        return 1
    elif (retrieved_ones < expected_ones):
        return -1
    else:
        return 0 #In the wild case that we predict every 1 correctly
    