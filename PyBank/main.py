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
    Average_Change = round(Change_total / len(Change), 2)
    print(Average_Change)

    # Calculate the greatest increase in profits (date and amount) over the entire period
    Greatest_increase = max(Change)
    print(Greatest_increase)
    i = Change.index(Greatest_increase)
    GI_month = Months_count [i + 1]

    # Calculate he greatest decrease in losses (date and amount) over the entire period  
    Greatest_decrease = min(Change)
    print(Greatest_decrease)
    d = Change.index(Greatest_decrease)
    GD_month = Months_count [d + 1]

    #Print the analysis to the terminal
    print ('')
    print('Financial Analysis')
    print('-----------------------------')
    print(f'Total Months: {len(Months_count)}')
    print(f'Total: ${Total}')
    print(f'Average Change: ${Average_Change}')
    print(f'Greatest Increase in Profits:')
    print(f'{GI_month} (${Greatest_increase})')
    print(f'Greatest Decrease in Profits:')
    print(f'{GD_month} (${Greatest_decrease})')    

    #Export a text file with the results
