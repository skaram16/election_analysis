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

#winning candidate as well winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

#determine percentage of votes for each candidate with looping
for candidate_name in candidate_votes:
    #retrieve vote count for each candidate
    votes = candidate_votes[candidate_name]
    #calculate percentage of votes per candidate
    vote_percentage = float(votes) / float(total_votes) * 100
    #print name, count and percentage of votes 
    print(f"{candidate_name}: received {vote_percentage}% of the vote.")

    #determine winning vote count and candidates
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #set winning_candidate to the name of the candidate
        winning_candidate = candidate_name
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
#winning candidate summary
winning_candidate_summary = (
    f"----------------\n"
    f"The Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"----------------\n")
print(winning_candidate_summary)

