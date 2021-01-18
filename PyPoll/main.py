# Import the os Module
import os

# Import Module for reading CSV files
import csv
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# Improved CSV file
with open (csvpath, newline='') as csvfile:

#CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader (csvfile, delimiter = ',')

# Add new variables
    Votes_count = 0
    votes = []
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
    print('-------------------------------')
    print('TOTAL VOTES')
    print(Votes_count)

#List voted candidates
    print('VOTED CANDIDATES')
    print(Voted_candidates)

# Compute the percentage of votes each candidate got
    for y in votes:
        shares = '{0:.3f}'.format(round((y/Votes_count)*100,2))
        Votes_share.append(shares)
    print('SHARE OF VOTES')
    print(Votes_share)
    print("TOTAL VOTES")
    print(votes)

# Print the winner based on popular vote
    Winner_votes = max(votes)
    z = votes.index(Winner_votes)
    winner=Voted_candidates[z]
    print('WINNER')
    print(winner)

# Print analysis results to terminal
    print('-------------------------------')
    print('')
    print('Election Results')
    print('-------------------------------')
    print(f'Total Votes: {Votes_count}')
    print('-------------------------------')
    print(str(Voted_candidates[0]) + ': ' + str(Votes_share[0]) + '% ' + '(' + str(votes[0]) + ')')
    print(str(Voted_candidates[1]) + ': ' + str(Votes_share[1]) + '% ' + '(' + str(votes[1]) + ')')
    print(str(Voted_candidates[2]) + ': ' + str(Votes_share[2]) + '% ' + '(' + str(votes[2]) + ')')
    print(str(Voted_candidates[3]) + ': ' + str(Votes_share[3]) + '% ' + '(' + str(votes[3]) + ')')
    print('-------------------------------')
    print(f'Winner: {winner}')
    print('-------------------------------')

# Export text file with results
    f = open('PyPoll.txt', 'w')
    f.write('Election Results')
    f.write('-------------------------------')
    f.write(f'Total Votes: {Votes_count}')
    f.write('-------------------------------')
    f.write(str(Voted_candidates[0]) + ': ' + str(Votes_share[0]) + '% ' + '(' + str(votes[0]) + ')')
    f.write(str(Voted_candidates[1]) + ': ' + str(Votes_share[1]) + '% ' + '(' + str(votes[1]) + ')')
    f.write(str(Voted_candidates[2]) + ': ' + str(Votes_share[2]) + '% ' + '(' + str(votes[2]) + ')')
    f.write(str(Voted_candidates[3]) + ': ' + str(Votes_share[3]) + '% ' + '(' + str(votes[3]) + ')')
    f.write('-------------------------------')
    f.write(f'Winner: {winner}')
    f.write('-------------------------------')
    f.close() 