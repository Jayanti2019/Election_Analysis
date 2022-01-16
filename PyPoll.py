#Read the Dataset
#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = 'election_results.csv'

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    #for row in file_reader:
    #    print(row)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:
