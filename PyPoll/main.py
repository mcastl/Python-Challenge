# Import the os Module
import os

# Import Module for reading CSV files
import csv
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# Improved CSV file
with open (csvpath, newline='') as csvfile:

#CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader (csvfile, delimiter = ',')

#Read the header row first
    #csv_header = next(csvreader)
    #print(f'CSV Header: \n{csv_header}')
        
# Add new variables
    Votes_count = 0
    votes = []
    Candidate_names = []
    Voted_candidates = []
    Votes_share = []
    Winner = " "

# Compute the total number of votes cast
    next(csvreader,None)
    for x in csvreader:
        if x[-1] not in Voted_candidates:
            Voted_candidates.append (x[-1])
            votes.append(1)
        else:
            index = Voted_candidates.index(x[-1])
            votes[index] += 1
        Votes_count += 1
    print('TOTAL VOTES')
    print(str(Votes_count))

#List voted candidates
    print('VOTED CANDIDATES')
    print(str(Voted_candidates[0]))
    print(str(Voted_candidates[1]))
    print(str(Voted_candidates[2]))
    print(str(Voted_candidates[3]))