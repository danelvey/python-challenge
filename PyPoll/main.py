## import dependencies
import os
import csv

## initialise variables
sumVote = 0
listCandidate = []
maxVotes = 0

## load csv file
csvpath = os.path.join(".", "Resources", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    ## read the header
    csv_header = next(csvreader)
    ##print(f"CSV Header: {csv_header}")

    #put the first candidate and vote in list
    firstRow = next(csvreader)
    firstCandidate = firstRow[2]
    countVote = 1
    listCandidate.append([firstCandidate,countVote])
    sumVote = 1

    ## go through each row   
    for row in csvreader:
        currentVoterID = row[0]
        currentCounty = row[1]
        currentCandidate = row[2]
        foundCandidate = False

        for detailsCandidate in listCandidate:
            if detailsCandidate[0] == currentCandidate:
                foundCandidate = True

                ## increase the vote count for the candidate
                detailsCandidate[1] = detailsCandidate[1] + 1
                sumVote = sumVote + 1          

        ## add the new candidate to the list
        if foundCandidate == False:
            countVote = 1
            listCandidate.append([currentCandidate,countVote])
            sumVote = sumVote + 1

    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {sumVote}")
    print("-----------------------------")

    for detailsCandidate in listCandidate:
        nameCandidate = detailsCandidate[0]
        votesWon = detailsCandidate[1]
        percentWon = votesWon / sumVote * 100
        
        ## calculate winner
        if votesWon > maxVotes:
            maxVotes = votesWon
            nameWinner = nameCandidate

        ## print results for each candidate
        print(f"{nameCandidate}: {percentWon:.3f}% ({votesWon})")
        
    print("-----------------------------")
    print(f"Winner: {nameWinner}")
    print("-----------------------------")

    ## write results in file
    outputPath = os.path.join(".","analysis","VoteAnalysis.txt")
    with open(outputPath, 'w') as txtFile:
        txtFile.write("Election Results")
        txtFile.write("\n")
        txtFile.write("-----------------------------")
        txtFile.write("\n")
        txtFile.write(f"Total Votes: {sumVote}")
        txtFile.write("\n")
        txtFile.write("-----------------------------")
        txtFile.write("\n")

        for detailsCandidate in listCandidate:
            nameCandidate = detailsCandidate[0]
            votesWon = detailsCandidate[1]
            percentWon = votesWon / sumVote * 100
        
            ## print results for each candidate
            txtFile.write(f"{nameCandidate}: {percentWon:.3f}% ({votesWon})")
            txtFile.write("\n")

        txtFile.write("-----------------------------")
        txtFile.write("\n")
        txtFile.write(f"Winner: {nameWinner}")
        txtFile.write("\n")
        txtFile.write("-----------------------------")
