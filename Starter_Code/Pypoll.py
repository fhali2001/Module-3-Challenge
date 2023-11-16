import csv
import os

def analyze_election_data(file_path):
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
    winner = max(candidate_votes, key=candidate_votes.get)

    # Print results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidate_votes.items():
        print(f"{candidate}: {percentages[candidate]:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

# Example usage
file_path = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")
analyze_election_data(file_path)