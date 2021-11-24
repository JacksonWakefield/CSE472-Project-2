
import Main
import DataHelper
import csv
import percentage_data

test_data = DataHelper.read_data('./test.csv')

p_data_Source = percentage_data.get_percentage_data('Source')
p_data_Country = percentage_data.get_percentage_data('Country (mentioned)')


threshold = Main.get_threshold() + 0.16


predictions = []

for i in range(0, len(test_data)):
    
    prediction = 0
            
    country = test_data.loc[i, 'Country (mentioned)']
    source = test_data.loc[i, 'Source']
    
    percentage_country = {0:0, 1:0, 2:0, 3:0}
    percentage_source = {0:0, 1:0, 2:0, 3:0}
    
    if(country in p_data_Country.keys()):
        percentage_country = p_data_Country[country]
    
    if(source in p_data_Source.keys()):
        percentage_source = p_data_Source[source]
    
    percentage_combined_1 = 1-(1-percentage_country[1]) * (1-percentage_source[1]) 
    
    if(percentage_combined_1 >= threshold):
        prediction = 1
    
    predictions.append(prediction)


with open('submission.csv', 'w', newline='\n') as csvfile:
    
    writer = csv.writer(csvfile, delimiter=',')
    
    writer.writerow(['Id', 'Predicted'])
    
    ones = 0
    
    for i in range(len(predictions)):
        
        if(predictions[i] == 1):
            ones += 1
        
        writer.writerow([i + 1, predictions[i]])
    print(ones)
    