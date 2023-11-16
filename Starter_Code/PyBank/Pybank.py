import os
import csv

file_path = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
changes = []
greatest_increase = {"date": "", "amount": float("-inf")}
greatest_decrease = {"date": "", "amount": float("inf")}

# Read CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip header row

    # Iterate through rows
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total months and net total
        total_months += 1
        net_total += profit_loss

        # Track changes in profit/loss
        if total_months > 1:
            change = profit_loss - prev_profit_loss
            changes.append(change)

            # Track greatest increase and decrease
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        # Store current profit/loss for the next iteration
        prev_profit_loss = profit_loss

# Calculate average change
average_change = sum(changes) / len(changes)

# Print results
# print("Budget Analysis")
# print("-----------------------------")
# print(f"Total Months: {total_months}")
# print(f"Net Total: ${net_total}")
# print(f"Average Change: ${average_change:.2f}")
# print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
# print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

report = (
    f"Budget Analysis\n"
    f"-----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

print(report)
analysis_path = os.path.join(os.path.dirname(__file__), "Analysis", "budget_analysis.txt")
with open(analysis_path, "w") as txtfile:
    txtfile.write(report)