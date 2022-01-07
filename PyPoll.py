# Import modules
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize vote counter
total_votes = 0

# Initialize candidate list
candidate_options = []

# Declare candidate votes dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
   
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        #Add the candidate name to the candidate list if it doesn't match a name already on the list.
        if candidate_name not in candidate_options:

            #Add candidate name to candidate list
            candidate_options.append(candidate_name)

            #Add candidate name to dictionary
            candidate_votes[candidate_name] = 0

        #Increase candidate vote count
        candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:

        # 2. Retrieve the vote count of a candidate.
        votes = candidate_votes[candidate_name]

        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        # Print each candidate's name, vote count, and percentage of votes
        print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
        
        # Determine if vote count that was calculated is greater than winning count
        if(votes > winning_count) and vote_percentage > winning_percentage:
        
        #If vote count is greater than winning_count AND the percentage is greater than winning_percentage,
        #set the winning_count equal to the votes and set the winning_percentage equal to the vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            
        # Set winning_count equal to candidate_name
            winning_candidate = candidate_name
        
# Print winning candidate, vote count, and percentage

winning_candidate_summary = (
    f'--------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    f'--------------------\n')

print(winning_candidate_summary)




