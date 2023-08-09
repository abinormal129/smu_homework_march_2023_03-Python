import csv

csv_path = "Starter_Code/Submissions/PyPoll/Resources/election_data.csv"

# calculate ttl number of votes cast
# complete list of candidates who received votes
# calculate percentage of votes each candidate won
# calculate ttl number of votes each candidate won
# winner of election based on popular votes

votes = 0

candidates = {}

with open(csv_path) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
       
        votes += 1

        # get the candidate
        # if the candidate is in the dictionary, we want to add 1 to the value
        # else, init with a vote of one

        candidate = row[2]
        if candidate in candidates.keys():
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
winner = max(candidates, key=candidates.get)

# print the results to screen
output = f"""Election Results
-----------------
Total Votes: {votes}
-----------------\n"""

for key in candidates.keys():
    perc = round(100*candidates[key]/votes, 3)
    newline = f"{key}: {perc}% ({candidates[key]})\n"
    output += newline
lastline = f"""
-----------------
Winner: {winner}
-----------------"""
output += lastline
print(output)

# print the results to text file
with open("Starter_Code\Submissions\PyPoll\ResultsPyPoll.txt", "w") as txt_file:
    txt_file.write(output)
