
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
    total_months += 1
    total_net += int(first_row[1])  # Add the first month's profit/loss
    prev_net = int(first_row[1])  # Store the first month's profit/loss for comparison

    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1  # Increment the total month count
        total_net += int(row[1])  # Add the current month's profit/loss to the total

        # Track the net change
        net_change = int(row[1]) - prev_net  # Calculate month-over-month change
        prev_net = int(row[1])  # Update previous month's profit/loss for the next iteration
        net_change_list += [net_change]  # Add this month's change to the list
        month_of_change += [row[0]]  # Add the month to the change list

        # Calculate the greatest increase in profits (month and amount)
        profits = [1000, 1200, 1100, 1500, 1300, 1800, 2000] 
        def calculate_greatest_increase(profits :
     max_increase = 0
    month_of_increase = None

    for i in range(1, len(profits)):
        increase = profits[i] - profits[i - 1]
        
        if increase > max_increase:
            max_increase = increase
            month_of_increase = i  # Store the index of the month return

         month_of_increase, max_increase

month, amount = calculate_greatest_increase(profits)
                                            



        # Calculate the greatest decrease in losses (month and amount)
        profits = [2000, 1800, 2100, 1500, 1700, 1300, 1200]

def calculate_greatest_decrease(profits):
    max_decrease = 0
    month_of_decrease = None

    for i in range(1, len(profits)):
        decrease = profits[i - 1] - profits[i]
        
        if decrease > max_decrease:
            max_decrease = decrease
            month_of_decrease = i  # Store the index of the month

    return month_of_decrease, max_decrease

month, amount = calculate_greatest_decrease(profits)


# Calculate the average net change across the months

profits = [2000, 1800, 2100, 1500, 1700, 1300, 1200]

def calculate_average_net_change(profits):
    # List to store the monthly changes
    changes = []

    # Calculate the monthly changes
    for i in range(1, len(profits)):
        change = profits[i] - profits[i - 1]
        changes.append(change)

    # Calculate the average change
    if changes:
        average_change = sum(changes) / len(changes)
    else:
        average_change = 0

    return average_change

average_net_change = calculate_average_net_change(profits)

print(f"The average net change in profits is: ${average_net_change:.2f}")
Explanation:

# Generate the output summary
profits = [2000, 1800, 2100, 1500, 1700, 1300, 1200]

def analyze_profits(profits):
    max_increase = 0
    max_decrease = 0
    month_of_increase = None
    month_of_decrease = None
    changes = []

    for i in range(1, len(profits)):
        change = profits[i] - profits[i - 1]
        changes.append(change)
 # Check for greatest increase
        if change > max_increase:
            max_increase = change
            month_of_increase = i

        # Check for greatest decrease
        if change < max_decrease:
            max_decrease = change
            month_of_decrease = i

    # Calculate average net change
    if changes:
        average_change = sum(changes) / len(changes)
    else:
        average_change = 0
     # Prepare summary
    months = ["January", "February", "March", "April", "May", "June", "July"]
    summary = {
        "Greatest Increase": (months[month_of_increase], max_increase),
        "Greatest Decrease": (months[month_of_decrease], max_decrease),
        "Average Net Change": average_change,
    }

    return summary

# Analyze profits and generate summary
summary = analyze_profits(profits)   

# Print the output
print("Profit Analysis Summary:")
print(f"Greatest Increase in Profits: {summary['Greatest Increase'][0]}: ${summary['Greatest Increase'][1]}")
print(f"Greatest Decrease in Profits: {summary['Greatest Decrease'][0]}: ${summary['Greatest Decrease'][1]}")
print(f"Average Net Change in Profits: ${summary['Average Net Change']:.2f}")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)