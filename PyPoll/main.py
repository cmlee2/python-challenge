# import the osc and csv modules to allow us to read csv files independent of os
import os
import csv

# define csvpath for python to pull the data from
csvpath = os.path.join("Resources", "election_data.csv")


# define votes received as variables equal to 0
charles_votes = 0
raymon_votes = 0
diana_votes = 0

# define a function that will return the winner depending on who has the most votes total
def electionwinner():
    if charles_votes > diana_votes and raymon_votes:
        winner = "Charles Casper Stockham"
    if diana_votes > charles_votes and raymon_votes:
        winner = "Diana DeGette"
    if raymon_votes > charles_votes and diana_votes:
        winner = "Raymon Anthony Doane"
    return(winner)

# open the csvfile
with open(csvpath) as csvfile:

    # define the delimiter
    csvreader = csv.reader(csvfile,delimiter=",")

    # read and save the header row
    csv_header = next(csvreader)
    
    # add one to each candidate's respective vote total if the row contains the candidates full name
    for row in csvreader:
        if row[2] == "Raymon Anthony Doane":
            raymon_votes += 1
        if row[2] == "Charles Casper Stockham":
            charles_votes += 1
        if row[2] == "Diana DeGette":
            diana_votes += 1

    # define total votes as the combined votes of all 3 candidates
    total_votes = diana_votes + charles_votes + raymon_votes

    # calculate percentages for each candidate by dividing their votes received over total votes received
    charles_percent = charles_votes/total_votes
    diana_percent = diana_votes/total_votes
    raymon_percent = raymon_votes/total_votes

    # print the election results output, using previous functions and variables in f-strings to get most updated value
    print(f"Election Results")
    print(f"-----------------------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"----------------------------------------- ")
    print(f"Charles Casper Stockham: {charles_percent:.3%} ({charles_votes})")
    print(f"Diana DeGette: {diana_percent:.3%} ({diana_votes})")
    print(f"Raymon Anthony Doane: {raymon_percent:.3%} ({raymon_votes})")
    print(f"----------------------------------------- ")
    print(f"Winner: {electionwinner()}")
    print(f"-----------------------------------------")

# create an output path for the text file to hold the results
output_path = os.path.join("Analysis", "results.txt")

# open the output path in write mode
with open(output_path, "w") as textfile: 
    
    # write each row according the results (Add \n to include line break)
    textfile.write(f"Election Results \n")
    textfile.write(f"----------------------------------------- \n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write(f"----------------------------------------- \n")
    textfile.write(f"Charles Casper Stockham: {charles_percent:.3%} ({charles_votes})\n")
    textfile.write(f"Diana DeGette: {diana_percent:.3%} ({diana_votes})\n")
    textfile.write(f"Raymon Anthony Doane: {raymon_percent:.3%} ({raymon_votes})\n")
    textfile.write(f"----------------------------------------- \n")
    textfile.write(f"Winner: {electionwinner()}\n")
    textfile.write(f"-----------------------------------------\n")