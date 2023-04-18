# python-challenge
Module 3  
  
PyBank  
The purpose of this project was to create a Python script that would pull and analyze data from a csv that mirrored the financial records of a mock company. This included tracking: 
   
        - The total number of months included in the data set 
        - The net total amount of Profit/Losses over the entire period  
        - The average change in Profit/Losses over the entire period  
        - The month with the greatest increase in profits and its value  
        - The month with the greatest decrease in profits and its value  
    
Futhermore, the script would print results and export them to a text file.  
   
Assistance was gathered from AskBCS to assist with storing the first value row using the next command:  
        -  csv_datapoint = next(csvreader)  
  
Assistance was gathered from Pythonhow on information on how to use round function  
       - print(f"Average Change: ${round(average_difference,2)}")  
  
  
PyPoll  
The purpose of this project was to create a Python script that would count and track votes for candidates in an election. The script tracks:  
  
        - The total number of votes  
        - A list of candidates who received votes  
        - the total number of votes each candidates received  
        - The percentage of votes each cadndidate received  
        - The winner of the election according to popular vote  
  
Furthermore, the script would print results and export them to a text file within a different folder.   
  
Assistance was gathered from Stack overflow on how to print percentage values   
        - print(f"Charles Casper Stockham: {charles_percent:.3%} ({charles_votes})")  