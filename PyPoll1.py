#add dependencies
import csv
import os
#assign variable to load file from the path
file_to_load = os.path.join("Resources", "election_results.csv")
#assign variable to save file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter
total_votes = 0

#options for candidates
candidate_options = []
#declare empty dictionary
candidate_votes = {}

#open election results and read file
with open(file_to_load) as election_data:
    #to do - read and analyze the data
    file_reader = csv.reader(election_data)

    #read and print the header row:
    headers = next(file_reader)
    
    #print each row in the CSV file
    for row in file_reader:
        #add to the total vote count:
        total_votes += 1

        #print candidate name for each row
        candidate_name = row[2]

        #if candidate doesn't match an existing candidate:
        if candidate_name not in candidate_options:
            #add candidate name to the candidate list
            candidate_options.append(candidate_name)
            #begin tracking vote count for candidates:
            candidate_votes[candidate_name] = 0
        #add vote to that candidates count
        candidate_votes[candidate_name] += 1

#print the candidate vote dictionary
print(candidate_votes)
