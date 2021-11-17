'''

BAG OF WORDS IMPLEMENTATION (BASIC)

 -- Creates the BOW vector from training data
 -- Grabs the BOW feature vector from testing data
 -- Uses KNN with a few distance metrics to determine closes neighbors

'''

import pandas as pd
import string
import re
from nltk.corpus import stopwords
import numpy as np

import DataHelper #DATAHELPER is an external script -> ./DataHelper

tr_data_raw = DataHelper.read_data('train.csv')

def get_training_vector(data_raw):
    
    data_mod = data_raw[['Claim', 'Label']].copy()
    
    big_string = ""
    
    for claim in data_mod['Claim']:
        big_string += ' ' + claim
    
    big_string = big_string.lower()
    big_string = re.sub(r'\W', ' ', big_string)
    big_string = re.sub(r'\s+', ' ', big_string)
    
    string_split = big_string.split(' ')
    
    string_freq = {}
    
    for word in string_split:
        
        if(word in set(stopwords.words('english'))):
            continue
        
        if word in string_freq.keys():
            string_freq[word] += 1
        else:
            string_freq[word] = 1
        
    highest_freq = {}
    
    for key in string_freq:
        if(string_freq[key] > 40):
            highest_freq[key] = string_freq[key]
    
    training_vector = pd.DataFrame(highest_freq, index = [0])
    
    index = 0
    
    for claim in data_mod:
        
        claim_mod = claim
        claim_mod = claim_mod.lower()
        claim_mod = re.sub(r'\W', ' ', claim_mod)
        claim_mod = re.sub(r'\s+', ' ', claim_mod)
        
        claim_split = claim_mod.split(' ')
        
        training_vector[index] = np.zeros([1, len(training_vector.index)])
        
        '''for word in claim_split:
            try:
                training_vector.at[index, word]
            except:
                '''''''''
        
        index = index + 1
        
    
    return training_vector
        
tr_vector = get_training_vector(tr_data_raw)    