# PyPoll Script

# Import necessary modules
import csv
from pathlib import Path
from collections import Counter

# Set the file path for the election data CSV
csv_path = Path("Resources/election_data.csv")

# Initialize variables to store our analysis
total_votes = 0
candidates = []

# Open and read the CSV file
with open(csv_path, 'r') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)

    # Skip the header row
    next(csvreader)

    # Iterate through each row in the CSV
    for row in csvreader:
        # Increment the total number of votes
        total_votes += 1

        # Add the candidate's name to our list
        candidates.append(row[2])

# Use Counter to count votes for each candidate
vote_counts = Counter(candidates)

# Prepare the analysis results
analysis = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""

# Calculate percentage of votes for each candidate and add to analysis
for candidate, votes in vote_counts.items():
    percentage = (votes / total_votes) * 100
    analysis += f"{candidate}: {percentage:.3f}% ({votes})\n"

# Find the winner
winner = max(vote_counts, key=vote_counts.get)

# Complete the analysis string
analysis += f"""-------------------------
Winner: {winner}
-------------------------
"""

# Print the analysis to the console
print(analysis)

# Write the analysis to a text file
output_path = Path("analysis/election_results.txt")
with open(output_path, 'w') as file:
    file.write(analysis)

print(f"Analysis has been written to {output_path}")