# Import dependencies
import os
import csv
import math

#import .csv file and export a text file (.txt) with the results
csvpath = os.path.join("Resources", "election_data.csv")
# print(csvpath)
csvpathout = os.path.join("analysis","PyPollResoults.txt")
# print(csvpathout)
# Create lists to read file
data = []
voter_id= []
county=[]
candidate=[]
#* The total number of voters included in the dataset
total_voters = 0
#* The net total amount of "Profit/Losses" over the entire period
total_net_profit_losses = 0
#* The average of the changes in "Profit/Losses" over the entire period
avg_change_profit_losses = 0
#* The greatest increase in profits (date and amount) over the entire period
max_increase_profit_amount = 0
max_increase_profit_date = 0
#* The greatest decrease in losses (date and amount) over the entire period
max_decrease_losses_amount = 0
max_decrease_losses_date = 0
with open(csvpath, 'r') as csvfile:
#     CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    for row  in csvreader:
        try:
            data.append([int(row[0]), str(row[1]), str(row[2])])
        except:
            pass
    row=0
# print("Here is the Data ")
    # for item in data:
    #     print(item)
# item = 0
# Data to Columns
for row  in data:
    voter_id.append(int(row[0]))
    county.append(row[1])
    candidate.append(row[2])
row=0
# for item in range(4):
#     print(voter_id[item], county[item], candidate[item])
