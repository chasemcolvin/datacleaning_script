import pandas as pd 
import os 

#specify your input/output file paths 
input_file = 'input_data.csv'
output_file = 'cleaned_data.csv'

#verify that the input file exists
#if not, exit script
if not os.path.isfile(input_file):
    print(f"Input file '{input_file}' does not exist!")
    exit()

#read data input file & analyze the data 
data = pd.read_csv(input_file)

#modify 'column_names' according to your dataset/cleaning requirements

#basic data cleaning operations 
#removing duplicates
data = data.drop_duplicates()
#removing null values
data = data.dropna()
#.str.strip() method to trim whitespace & ensure data consistency 
data['text_column'] = data['text_column'].str.strip() 

#converting data types 
#.astype() method to convert numerical data from an object to int
data['num_column'] = data['num_column'].astype(int) 

#boolean indexing to filter rows and remove values <= 0
data = data[data['column_name'] > 0]

#rank() method sort the data in 'column_name' asc, False = desc
#stored in new asc_rank column within the 'df'
data['asc_rank'] = data['column_name'].rank(ascending=True)

#filtering rows based on a specific date range
#convert 'date_column' to datetime format for the year 2022
data['date_column'] = pd.to_datetime(data['date_column']) 
start_date = pd.to_datetime('2022-01-01')
end_date = pd.to_datetime('2022-12-31')
data = data[(data['date_column'] >= start_date) & (data['date_column'] <= end_date)]

#save cleaned data to your output file
data.to_csv(output_file, index=False)

print(f"Data cleaning is complete. Your cleaned data is saved to '{output_file}'.")
