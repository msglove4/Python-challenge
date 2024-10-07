# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
# List of candidate names
candidates = ["Jefferson", "Casper", "Charles","Stockham" ]

# Dictionary to track vote counts
vote_counts = {candidate: 0 for candidate in candidates}

# Example of adding votes
def add_vote(candidate_name):
    if candidate_name in vote_counts:
        vote_counts[candidate_name] += 1
    else:
        print(f"{candidate_name} is not a valid candidate.")
    # Adding some votes
add_vote("Jefferson")
add_vote("Casper")
add_vote("Charles")
add_vote("Stockham")
add_vote("Bob")

# Print the vote counts
print("Vote Counts:")
for candidate, count in vote_counts.items():
    print(f"{candidate}: {count}")
# Winning Candidate and Winning Count Tracker
# List of candidate names
candidates = ["Alice", "Bob", "Charlie"]

# Dictionary to track vote counts
vote_counts = {candidate: 0 for candidate in candidates}

# Function to add votes
def add_vote(candidate_name):
    if candidate_name in vote_counts:
        vote_counts[candidate_name] += 1
    else:
        print(f"{candidate_name} is not a valid candidate.")

# Function to determine the winning candidate
def find_winner():
    winning_candidate = None
    winning_count = 0
    for candidate, count in vote_counts.items():
        if count > winning_count:
            winning_count = count
            winning_candidate = candidate
            
    return winning_candidate, winning_count

# Simulate voting
add_vote("Jefferson")
add_vote("Bob")
add_vote("Alice")
add_vote("Charles")
add_vote("Casper")
add_vote("Stockham")

# Print the vote counts
print("Vote Counts:")
for candidate, count in vote_counts.items():
    print(f"{candidate}: {count}")

# Determine and print the winner
winner, count = find_winner()
if winner:
    print(f"\nThe winning candidate is {winner} with {count} votes.")
else:
    print("No winner could be determined.")


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
# List of candidate names
candidates = ["Alice", "Bob", "Charlie"]

# Dictionary to track vote counts
vote_counts = {candidate: 0 for candidate in candidates}

# Variable to keep track of total votes
total_votes = 0

# Function to add votes
def add_vote(candidate_name):
    global total_votes  # Use global to modify the total_votes variable
    if candidate_name in vote_counts:
        vote_counts[candidate_name] += 1
        total_votes += 1  # Increment total votes
    else:
        print(f"{candidate_name} is not a valid candidate.")
       # Function to determine the winning candidate
def find_winner():
    winning_candidate = None
    winning_count = 0
    
    for candidate, count in vote_counts.items():
        if count > winning_count:
            winning_count = count
            winning_candidate = candidate
            
    return winning_candidate, winning_count

# Simulate voting
add_vote("Jefferson")
add_vote("Bob")
add_vote("Alice")
add_vote("Charles")
add_vote("Casper")
add_vote("Stockham")

# Print the vote counts
print("Vote Counts:")
for candidate, count in vote_counts.items():
    print(f"{candidate}: {count}")

# Print the total vote count
print(f"\nTotal Votes: {total_votes}")

# Determine and print the winner
winner, count = find_winner()
if winner:
    print(f"The winning candidate is {winner} with {count} votes.")
else:
    print("No winner could be determined." 

        # Get the candidate's name from the row
        candidates = ["Jefferson", "Casper", "Charles","Stockham" ]

            s = pd.Series(['col1','col2','col3','col4','col5'])

# Get the list of valid column names

valid = s[s.isin(df.columns)]

        # If the candidate is not already in the candidate list, add them
        def add_candidate_if_not_exists(row, candidate_list):
    candidate_name = row['name']  
    if candidate_name not in candidate_list:
        candidate_list.append(candidate_name)

candidate_list = ['Jefferson', 'Bob', 'Charles']
row = {'name': 'David', 'age': 30}

add_candidate_if_not_exists(row, candidate_list)
print(candidate_list)

        # Add a vote to the candidate's count
        def add_vote(row, candidate_votes):
    candidate_name = row['name']  # Assuming 'name' is the key for the candidate's name
    if candidate_name in candidate_votes:
        candidate_votes[candidate_name] += 1  # Increment vote count if candidate exists
    else:
        candidate_votes[candidate_name] = 1  # Add candidate with one vote if they don't exist

# Example usage:
candidate_votes = {'Jefferon': 5, 'Bob': 3, 'Charles: 2}
row = {'name': 'David', 'age': 30}

add_vote(row, candidate_votes)
print(candidate_votes)

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)


    # Write the total vote count to the text file


    # Loop through the candidates to determine vote percentages and identify the winner


        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage


    # Generate and print the winning candidate summary


    # Save the winning candidate summary to the text file
