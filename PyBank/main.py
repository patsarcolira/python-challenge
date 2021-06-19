# Import dependencies
import os
import csv
import math

#import .csv file and export a text file (.txt) with the results
csvpath = os.path.join("Resources", "budget_data.csv")
print(csvpath)
csvpathout = os.path.join("analysis","PyBankResoults.txt")
print(csvpathout)
# Create lists to read file
data = []
dates = []
profit_losses=[]
change_amounts=[]
#* The total number of months included in the dataset
total_months = 0
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
print("Financial Analysis")
print("----------------------------")
print("total_months = " + str(total_months))
print("total_net_profit_losses = " + str(total_net_profit_losses))
print("avg_change_profit_losses = " + str(avg_change_profit_losses))
print("max_increase_profit_amount = " + str(max_increase_profit_amount))
print("max_increase_profit_date = " + str(max_increase_profit_date))
print("max_decrease_losses_amount = " + str(max_decrease_losses_amount))
print("max_decrease_losses_date = " +  str(max_decrease_losses_date))

with open(csvpath, 'r') as csvfile:
#     CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    for row  in csvreader:
        try:
            data.append([row[0], float(row[1])])
        except:
            pass
    row=0
    print("Here is the Data")
    for item in data:
        print(item)
    item = 0
    # Data to Columns
    for row  in data:
        dates.append(row[0])
    row=0
    print("Show only dates")
    for item in dates:
        print(item)
    item = 0
    for row  in data:
        profit_losses.append(row[1])
        change_amounts.append(row[1])
    row = 0
    print("Show only losses and profits")
    for item in profit_losses:
        print(item)
    item = 0

# * The total number of months included in the dataset
print('Financial Analysis')
print('----------------------------')
print(f"Total Months: ", len(dates))

# * The net total amount of "Profit/Losses" over the entire period
total_net_profit_losses = sum(profit_losses)
print(f"Total: $", total_net_profit_losses)

# * The average of the changes in "Profit/Losses" over the entire period
# Create a list of change in profit and losses -- total_net_profit_losses -- avg_change_profit_losses
previous_amount= profit_losses[0]
row = 0
row_change = 0
#print(previous_amount, profit_losses[0])  len(profit_losses) len(change_amounts)
for row in range(3):
    change_amounts[row_change] = (profit_losses[row]-previous_amount)
    #print(f"", change_amounts[row_change], " = ", profit_losses[row], " - ", previous_amount)
    previous_amount = profit_losses[row]
    row_change=row_change + 1
row=0
row_change=0
print("------------------------")
for row_change in range(3):
    print(change_amounts[row_change])
sum = sum(change_amounts)
avg_change_profit_losses = sum/len(profit_losses)
#print (avg_change_profit_losses)
        
        
#change_amount=[]

#avg_change_profit_losses
# * The greatest increase in profits (date and amount) over the entire period

# * The greatest decrease in losses (date and amount) over the entire period