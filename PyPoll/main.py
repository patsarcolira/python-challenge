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
name="[]"
who_is_running=[]
candidates_vote_list=[]
votes_khan = 0
votes_correy = 0
votes_li = 0
votes_o_tooley = 0
#     Open a dread CSV reader specifies delimiter and variable that holds contents

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    for row  in csvreader:
        try:
            data.append([int(row[0]), str(row[1]), str(row[2])])
        except:
            pass
    row=0
# Data to Columns
for row  in data:
    voter_id.append(int(row[0]))
    county.append(row[1])
    candidate.append(row[2])
row=0
# for item in range(4):
#     print(voter_id[item], county[item], candidate[item])

# * The total number of votes cast
total_votes = len(voter_id)
print('Election Results')
print('----------------------------')
print(f"Total Votes: ", total_votes)
print('----------------------------')
# * A complete list of candidates who received votes
for row  in candidate:
    name = row
    if name not in who_is_running:
        who_is_running.append(name)
print(f"Who_is_running? , {who_is_running}")




# for row in candidate:

#     for row in csv_reader:
#             #Votes per candidate
#         if candidate in candidates:
#            candidate_index = candidates.index(candidate)
#            vote_count[candidate_index] = vote_count[candidate_index] + 1
#         else:
#            candidates.append(candidate)
#            vote_count.append(1)



#     candidate_cast= str(candidate[row])
#     if candidate_cast == "Khan" :
#         votes_khan = votes_khan + 1
#     elif candidate_cast == "Correy" :
#         votes_correy = votes_correy + 1
#     elif candidate_cast == "Li" :
#         votes_li = votes_li + 1
#     elif candidate_cast == "O\'Tooley" :
#         votes_o_tooley = votes_o_tooley + 1
#     else:
#         pass
# print(f"votes_khan", votes_khan, "votes_correy", votes_correy,"votes_li",votes_li,"votes_o_tooley",votes_o_tooley)
