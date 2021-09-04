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
    #read and analyze the data
    file_reader = csv.reader(election_data)

    #read the header row:
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

#save results to text file.
with open(file_to_save, "w") as txt_file:
    #print final vote count to terminal:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #save final vote count to the text file.
    txt_file.write(election_results)

    #determine percentage of votes for each candidate with looping
    for candidate_name in candidate_votes:
        #retrieve vote count for each candidate
        votes = candidate_votes[candidate_name]
        #calculate percentage of votes per candidate
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}: received {vote_percentage}% of the vote.")
        #print name, count and percentage of votes per candidate
        print(candidate_results)
        #save candidate results to text file
        txt_file.write(candidate_results)

        #determine winning vote count and candidates
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
            #print winning candidate's results to terminal
            #winning candidate summary
    winning_candidate_summary = (
    f"-------------------------\n"
    f"The Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    #save winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)