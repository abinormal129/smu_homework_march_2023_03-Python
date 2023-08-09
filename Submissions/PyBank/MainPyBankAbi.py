import csv

csv_path = "Starter_Code/Submissions/PyBank/Resources/budget_data.csv"

months = 0
total_profit = 0

is_first_row = True
last_month_profit = 0
changes = []

# calculate ttl months included in data set
# calculate net ttl amount of profit/losses over entire period
# calculate changes in profit/losses over entire period, and then avg of those changes
# greatest inc in profit/losses over entire period
# for each row
# add 1 to some month counter
# add column 2 (8) to some profit counter

max_change = -99999999999
max_month = ""

# greatest dec in profit/losses over entire period

min_change = 999999999999999999
min_month = ""


with open(csv_path) as csvfile:

    # CSV reader specifies delimiter and variable
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        row_profit = int(row[1])

        # check if first row (no change in first month but need to init last_month_profit)
        if is_first_row:
            last_month_profit = row_profit
            is_first_row = False
        else:
            change = row_profit - last_month_profit
            changes.append(change)

        # reset row
            last_month_profit = row_profit

        # compared to max/min
            if change > max_change:
                 max_change = change
                 max_month = row[0]

            if change < min_change:
                min_change = change
                min_month = row[0]

        months += 1
        total_profit += int(row[1])
        
   
    # print results
    avg_changes = sum(changes) / len(changes)

    print(" ")
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${round(avg_changes, 2)}")
    print(f"Greatest Increase in Profits: {max_month} ${max_change}")
    print(f"Greatest Decrease in Profits: {min_month} ${min_change}")

    analysispybank = (
    f"Financial Analysis\n"
    f"------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${round(avg_changes, 2)}\n"
    f"Greatest Increase in Profits: {max_month} ${max_change}\n"
    f"Greatest Decrease in Profits: {min_month} ${min_change}\n")

# write to a text file
    with open('Starter_Code\Submissions\PyBank\AnalysisPyBank.txt', 'w') as txt_file:
        txt_file.write(analysispybank)
