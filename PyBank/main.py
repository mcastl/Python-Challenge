# Import the os Module
import os

# Import Module for reading CSV files
import csv

csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Improved CSV file
with open (csvpath) as csvfile:

    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader (csvfile, delimiter = ',')
    print (csvreader)

    #Read the header row first
    csv_header = next (csvreader)
    print(f'CSV Header: \n{csv_header}')
    print('CSV contents:\n')

    #Read each row after the heading
    for row in csvreader:
        print (row)