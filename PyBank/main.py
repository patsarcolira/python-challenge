# Import dependencies
import os
import csv
#import .csv file and export a text file (.tx) with the results
csvpath = os.path.join("Resources", "budget_data.csv")
print(csvpath)
csvpathout = os.path.join("analysis","PyBankResoults.txt")
print(csvpathout)
# Import dependencies
import os
import csv
#import .csv file and export a text file (.tx) with the results
csvpath = os.path.join("Resources", "budget_data.csv")
print(csvpath)
csvpathout = os.path.join("analysis","PyBankResoults.txt")
print(csvpathout)
# Create lists to read the file
data = []
dates = []
profit_losses=[]
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
    row = 0
    print("Show only losses and profits")
    for item in profit_losses:
        print(item)
    item = 0

   