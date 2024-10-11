
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change
    total_months = 1
    total_net += int(first_row[1])  # Add the first month's profit/loss
    prev_net = int(first_row[1])  # Store the first month's profit/loss for comparison
    profits = []


    # Initialize variables
    previous_profit_loss = None
    greatest_increase_value = float('-inf')
    greatest_increase_date = None

    greatest_decrease_value = float('inf')
    greatest_decrease_date = None
    change = 0
    # Process each row of data
    for row in reader: 

        # Track the total
        total_months += 1  # Increment the total month count
        total_net += int(row[1])  # Add the current month's profit/loss to the total
        # Track the net change

        net_change = int(row[1]) - prev_net  # Calculate month-over-month change
        prev_net = int(row[1])  # Update previous month's profit/loss for the next iteration
        net_change_list.append(net_change)  # Add this month's change to the list
        

        # Check if the current change is the greatest increase
        if net_change > greatest_increase_value:
            greatest_increase_value = net_change
            greatest_increase_date = row[0]

        # Check if the current change is the greatest decrease
        if net_change < greatest_decrease_value:
            greatest_decrease_value = net_change
            greatest_decrease_date = row[0]


net_monthly_avg = sum(net_change_list) / len(net_change_list)       

output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)
print (output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)