
submission_name = './submission.csv'
training_name = './train.csv'

import DataHelper

def test_with_training():
    
    #data = DataHelper.read_data(submission_name)
    
    training_data = DataHelper.read_data(training_name)
    
    table = {}
    
    for i in range(len(data)):
        try:
            if(data.loc[i, 'Predicted'] == training_data.loc[i, 'Label']):
                table[i] = 1
            else:
                table[i] = 0
        except:
            print('SOMETHING WENT WRONG WHEN TESTING')
            
        table_df = pandas.DataFrame(table)
        
        
        

correctness_table = test_with_training()
    