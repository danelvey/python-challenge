## import dependencies
import os
import csv

## load csv file
csvpath = os.path.join(".", "Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    ## read the header
    csv_header = next(csvreader)
        
    ## initialise variables
    countMonth = 0
    sumAmount = 0
    maxAmount = 0
    minAmount = 0
    maxMonth = ""
    minMonth = ""

    ## go through each row   
    for row in csvreader:
        currentMonth = row[0]
        currentAmount = float(row[1])

        ## count up the months
        countMonth = countMonth + 1

        ## sum up the amounts
        sumAmount = sumAmount + currentAmount

        ## check to see if greatest increase
        if (currentAmount > maxAmount):
            maxAmount = currentAmount
            maxMonth = currentMonth

        ## check to see in greatest decrease
        if (currentAmount < minAmount):
            minAmount = currentAmount
            minMonth = currentMonth

    ## calculate average amounts
    meanAmount = sumAmount / countMonth

    ## print results to terminal
    print("Financial Analysis")
    print("------------------")
    print("Total Months: " + str(countMonth))
    print("Total: $" + "{:.2f}".format(sumAmount))
    print("Average Change: $" + "{:.2f}".format(meanAmount))
    print("Greatest Increase in Profits: " + maxMonth + " ($" + "{:.2f}".format(maxAmount) + ")")
    print("Greatest Decrease in Profits: " + minMonth + " ($" + "{:.2f}".format(minAmount) + ")")

    ## write results in file
    outputPath = os.path.join(".","analysis","FinancialAnalysis.txt")
    with open(outputPath, 'w') as txtFile:
        txtFile.write("Financial Analysis")
        txtFile.write("\n")
        txtFile.write("------------------")
        txtFile.write("\n")
        txtFile.write("Total Months: " + str(countMonth))
        txtFile.write("\n")
        txtFile.write("Total: $" + "{:.2f}".format(sumAmount))
        txtFile.write("\n")
        txtFile.write("Average Change: $" + "{:.2f}".format(meanAmount))
        txtFile.write("\n")
        txtFile.write("Greatest Increase in Profits: " + maxMonth + " ($" + "{:.2f}".format(maxAmount) + ")")
        txtFile.write("\n")
        txtFile.write("Greatest Decrease in Profits: " + minMonth + " ($" + "{:.2f}".format(minAmount) + ")")
