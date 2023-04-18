# import the osc and csv modules to allow us to read csv files independent of os
import os
import csv

# define csvpath for python to pull the data from
csvpath = os.path.join("Resources", "budget_data.csv")

# define variable to count the total months, total dollars, and total difference 
total_months = 0 
total_dollars = 0
total_difference = 0

# define a list to store the month and larget increase and decrease
min_value = [0,0]
max_value = [0,0]

# open the csv file
with open(csvpath) as csvfile:
    
    # define the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    # save the header row
    csv_header = next(csvreader)

    # save the first row of data 
    csv_datapoint = next(csvreader)

    # add one to the total months because the first row already read
    total_months += 1
    
    # add the month's value because the first value row is already read
    total_dollars = int(csv_datapoint[1])

    # save the row's current value in a variable for later calculations
    previous_month = int(csv_datapoint[1])

    # for loop to track the total months, total dollars and total difference 
    for row in csvreader:
        
        # save the row's current value as an integer
        current_month = int(row[1])

        # calculate the difference between the current row and the previous row
        difference = current_month - previous_month

        # add the difference to the total difference for each loop
        total_difference = difference + total_difference

        # add one to the total months for each loop
        total_months += 1

        # add the current month's dollars for each loop
        total_dollars = (current_month) + total_dollars

        # change the current month's value to the previous month's value to allow the loop to progress
        previous_month = current_month
    
        # conditional that saves the current month and difference if it is smaller than the current saved difference
        if min_value[1] > difference:
            min_value[0] = row[0]
            min_value[1] = difference

        # conditional that saves the current month and difference it if is larger than the current saved difference
        if max_value[1] < difference:
            max_value[0] = row[0]
            max_value[1] = difference
        
    average_difference = total_difference/(total_months - 1)

    

# print financial results using previous variables in f-strings for legibility
print(f"Financial Analysis")
print(f"------------------------------------------ ")
print(f'Total Months: {total_months}')
print(f"Total: ${total_dollars}")
print(f"Average Change: ${round(average_difference,2)}")
print(f"Greatest Increase in Profits: {max_value[0]} (${max_value[1]})")
print(f"Greatest Decrease in Profits: {min_value[0]} (${min_value[1]})")

# create an output path for the text file to hold the results
output_path = os.path.join("Analysis", "results.txt")

# open the output path in write mode
with open(output_path, "w") as textfile:    

    # write each row according the results (Add \n to include line break)
    textfile.write(f"Financial Analysis\n")
    textfile.write(f"------------------------------------------ \n")
    textfile.write(f'Total Months: {total_months}\n')
    textfile.write(f"Total: ${total_dollars}\n")
    textfile.write(f"Average Change: ${round(average_difference,2)}\n")
    textfile.write(f"Greatest Increase in Profits: {max_value[0]} (${max_value[1]})\n")
    textfile.write(f"Greatest Decrease in Profits: {min_value[0]} (${min_value[1]})\n")
