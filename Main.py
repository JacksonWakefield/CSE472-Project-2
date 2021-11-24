
import percentage_data
import DataHelper
import test_with_training

p_data_Source = percentage_data.get_percentage_data('Source')
p_data_Country = percentage_data.get_percentage_data('Country (mentioned)')

data = DataHelper.read_data('train.csv')



weight_Source = 0.5
weight_Country = 0.5
threshold_1 = 0.5
threshold_2 = 0.5
threshold_3 = 0.5

value_change = 0.01

min_rnge = 4000
max_rnge = 6300


results = {}

#6390 = max
#PREDICT LABEL

for times in range(1, 50):

    predictions = []
    
    for i in range(min_rnge, max_rnge):
            
        prediction = 0
        
        country = data.loc[i, 'Country (mentioned)']
        source = data.loc[i, 'Source']
        
        percentage_country = p_data_Country[country]
        
        percentage_source = p_data_Source[source]
        
        percentage_combined_1 = percentage_country[1] + percentage_source[1] 
        
        if(percentage_combined_1 > threshold_1):
            prediction = 1
        
        predictions.append(prediction)
    
    too_many = test_with_training.too_many_ones(predictions, min_rnge, max_rnge)
    
    if(too_many == -1):
        print('sub')
        threshold_1 -= value_change
    elif(too_many == 1):
        print('add')
        threshold_1 += value_change
    else:
        print("WE DID IT: CORRECTLY EVALUATED ALL 1s")

print(threshold_1)
    #print("C: " + percentage_country)
    #print("S: " + percentage_source)
    