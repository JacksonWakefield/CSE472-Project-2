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
    
    other_stopwords = ['coronavirus', 'corona', 'virus']
    
    for word in string_split:
        
        if(word in set(stopwords.words('english')) or word in other_stopwords):
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
    
    for i in range(len(data_mod)):
        
        claim_mod = data_mod.loc[i, 'Claim']
        claim_mod = claim_mod.lower()
        claim_mod = re.sub(r'\W', ' ', claim_mod)
        claim_mod = re.sub(r'\s+', ' ', claim_mod)
        
        claim_split = claim_mod.split(' ')
        
        vector_individual = {}
        
        for col in training_vector:
            vector_individual[col] = 0
            
        for word in claim_split:
            if(word in vector_individual.keys()):
                vector_individual[word] += 1
            else:
                #print('SKIPPED: ' + word)
                continue
        
        #training_vector = vector_individual
        print(vector_individual)
                
        
        index = index + 1
        
    
    return training_vector
        
tr_vector = get_training_vector(tr_data_raw)    