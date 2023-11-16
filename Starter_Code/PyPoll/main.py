import csv
import os

file_path = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")

total_votes = 0
candidate_votes = {}

# Read CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip header row

    # Iterate through rows
    for row in csvreader:
        candidate = row[1]

        # Count total votes
        total_votes += 1

        # Count votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate percentages
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Find the winner
winner = max(candidate_votes, key = candidate_votes.get)

most = max(candidate_votes)

print(f"The most is: {most}")

lines = [f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n" for candidate, votes in candidate_votes.items()]

candidates = list(candidate_votes.keys())

votes = list(candidate_votes.values())

max_votes = max(votes)

results = list(zip(candidates, votes))
     
print("candidates and votes are: ", candidates, votes)
print("results are: ", results)

for result in results:
    if result[1] == max_votes:
        biggest_loser = result[0]

print(f"The winner is {biggest_loser} with {max_votes}")

# If this is the first the candidate has received a
# vote, the candidate key and the default value, 0
# (given by the second argument in the get() method)
# are added to the dictionary before incrementing the
# candidates vote count by 1
# votes[candidate] = votes.get(candidate, 0) + 1

data = ""
for candidate, votes in candidate_votes.items():
     data += f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n"
    
# Print results
report = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    f"{data}"
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)
print(report)
analysis_path = os.path.join(os.path.dirname(__file__), "Analysis", "election_analysis.txt")
with open(analysis_path, "w") as txtfile:
    txtfile.write(report)