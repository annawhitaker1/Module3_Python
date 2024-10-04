# PyBank Script

# Import necessary modules
import csv
from pathlib import Path

# Set the file path for the budget data CSV
# Using Path from pathlib for better cross-platform compatibility
csv_path = Path("Resources/budget_data.csv")

# Initialize variables to store our analysis
total_months = 0
net_total = 0
previous_profit = 0
changes = []
greatest_increase = {"date": "", "amount": float('-inf')}
greatest_decrease = {"date": "", "amount": float('inf')}

# Open and read the CSV file
with open(csv_path, 'r') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)

    # Skip the header row
    next(csvreader)

    # Iterate through each row in the CSV
    for row in csvreader:
        # Extract date and profit/loss from the current row
        date = row[0]
        profit = int(row[1])  # Convert string to integer

        # Increment the total number of months
        total_months += 1

        # Add the current profit/loss to the net total
        net_total += profit

        # Calculate change in profit (skip for the first month)
        if total_months > 1:
            change = profit - previous_profit
            changes.append(change)

            # Check for greatest increase
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change

            # Check for greatest decrease
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        # Set current profit as previous profit for next iteration
        previous_profit = profit

# Calculate average change
average_change = sum(changes) / len(changes)

# Prepare the analysis results
analysis = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]})
Greatest Decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["amount"]})
"""

# Print the analysis to the console
print(analysis)

# Write the analysis to a text file
output_path = Path("analysis/financial_analysis.txt")
with open(output_path, 'w') as file:
    file.write(analysis)

print(f"Analysis has been written to {output_path}")