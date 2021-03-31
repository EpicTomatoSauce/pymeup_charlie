#import csv file
import os
import csv

dirname = os.path.dirname(__file__)
election_csv = os.path.join(dirname,"..", "Resources", "election_data.csv")

#Define List of Variables
voter_id = []
county = []
candidate = []

with open(election_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)

    #Create Lists
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

        
    #Total Number of Votes
    total_votes_cast = len(voter_id)

print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {total_votes_cast}")
print("-----------------------------------")

#Create sorted list of candidates
candidates_list = list(set(candidate))
candidates_list.sort()

#Votes per Candidate
candidate_votes = []
for candidates in candidates_list:
    candidate_votes.append(candidate.count(candidates))

#printed and nested f-string for the calculation and printing of the candidates, % of votes and # of votes for each candidate [i] in list
for i in range(len(candidates_list)):
    print(f"{candidates_list[i]}: {'{:.2%}'.format(candidate_votes[i]/total_votes_cast)} ({candidate_votes[i]} votes)")
print("-----------------------------------")
print(f"Winner: {candidates_list[candidate_votes.index(max(candidate_votes))]}")
print("---------------------\n")


#Output
output_file = os.path.join(dirname, "election_results.txt")

with open(output_file, "w") as f:
    f.write("Election Results")
    f.write("\n")
    f.write("-----------------------------------")
    f.write("\n")
    f.write(f"Total Votes: {total_votes_cast}")
    f.write("\n")
    f.write("-----------------------------------")
    f.write("\n")
    for i in range(len(candidates_list)):
        f.write(f"{candidates_list[i]}: {'{:.2%}'.format(candidate_votes[i]/total_votes_cast)} ({candidate_votes[i]} votes)")
        f.write("\n")
    f.write("-----------------------------------")
    f.write("\n")
    f.write(f"Winner: {candidates_list[candidate_votes.index(max(candidate_votes))]}")
    f.write("\n")
    f.close()


