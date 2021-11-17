'''

ALL THINGS RELATED TO GENERAL DATA FUNCTIONS

'''

import pandas as pd

punctuation = []

#just returns a pandas dataframe with all the data from either doc
def read_data(path):
    
    with open(path, newline ='\n', encoding='utf8') as training_file:
        
        tr_data_raw = pd.read_csv(training_file)
        
        return tr_data_raw