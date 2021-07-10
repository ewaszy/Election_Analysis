# Add our Dependencies 
import csv
import os

# Assign a variable to load a file from a path
# File assignment variable
#file_to_load = 'Resources\election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save a file from a path
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

    # To do: Read and Analyze the data here
    #print(election_data)
    
    # Read the file object with the reader function 
        # this allows us to read the CSV file using the csv module with the reader function
    file_reader = csv.reader(election_data)

    # Print each row in the csv file
    #for row in file_reader:
        #print(row)

    # Print the header row
        # Confirmed we have skipped header row, can now iterate througheach row
        # to gather data for analysis 
    headers = next(file_reader)
    print(headers)

# Close the file.
#election_data.close()

# Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")
with open(file_to_save, "w") as txt_file:

# Write some data to the file
#outfile.write("Hello World")
    #txt_file.write("Hello World")
    
    # Write three counties to the file
    # Add comma and space to separate the names
    # Can do three separate lines, or combine into one line:
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")
    #txt_file.write("Arapahoe, Denver, Jefferson")
    # Add newline escape sequence to end of first 2 counties
    # anything after \n will start on a new line 
    txt_file.write("Arapahoe\nDenver\nJefferson")
    

# Close the file 
#outfile.close()


# The data we need to retrieve
# 1. The total number of votes cast 
# 2. A complete list of candidates who recived votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won 
# 5. The winner of the election based on popular vote