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

    # Add columns for calculations
    Months_count = []
    Balance = []
    Average_Change = []
    Change = []

    # Read each row of data after the header
    for row in csvreader:
    #Add new elements to the list
        Months_count.append(row[0])
        Balance.append(row[1])
    
    # Calculate the total number of months included in the dataset
    print(len(Months_count))

    # Calculate the net total amount of "Profit/Losses" over the entire period
    Balance_int = map(int, Balance)
    Total = (sum(Balance_int))
    print (Total)

    # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    x = 0
    for x in range(len(Balance) - 1):
        New_value = int(Balance[x + 1])
        Old_value = int(Balance[x])
        Monthly_change = int(New_value - Old_value)
        Change.append(Monthly_change)
    Change_total = sum(Change)
    Average_Change = Change_total / len(Change)
    print(Average_Change)

    # Calculate the greatest increase in profits (date and amount) over the entire period

    # Calculate he greatest decrease in losses (date and amount) over the entire period  