
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

file_path = 'Resources/election_data.csv'
file_to_output = 'analysis/election_results.txt'


with open (file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader) # to read the header

    total_votes = 0
    candidates = set() 
    candidate_votes = {}
    for row in csv_reader:
        total_votes += 1    
        candidate_name = row[2]  # Candidate column is at index 2
        candidates.add(candidate_name)
        if candidate_name in candidate_votes:
                candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

    output =f"The total number of votes cast is {total_votes}.\n"
    output += f"The complete list of candidates who received votes:\n"


    for candidate in candidates:
        output += f"- {candidate}\n"

    output += '\nPercentage of votes each candidate won:\n'
        
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        output += f"- {candidate}: {percentage:.2f}% ({votes} votes)\n"


output +=  '\nTotal number of votes each candidate won:\n'
for candidate, votes in candidate_votes.items():
        output += f"\n- {candidate}: {votes} votes\n"

winner = max(candidate_votes, key=candidate_votes.get)
winner_votes = candidate_votes[winner]
output += f"\nThe winner of the election is {winner} with {winner_votes} votes.\n"

print(f"Results written to {file_to_output}")
print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)