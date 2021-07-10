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

# 3.5.1 (1) Initialize a total vote counter
    # Set total_votes to zero; t_v must be zero every time we run the file
total_votes = 0 

# 3.5.2 (4) Declare a new list
# Candidate Options
candidate_options = [] 

# Open the election results and read the file.
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:

    # To do: Read and Analyze the data here
    #print(election_data)
    
    # Read the file object with the reader function 
        # this allows us to read the CSV file using the csv module with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
        # Confirmed we have skipped header row, can now iterate througheach row
        # to gather data for analysis 
    headers = next(file_reader)
    # Print the header row
    #print(headers)

    # Print each row in the csv file
    for row in file_reader:
        #print(row)
        # 3.5.1 (2) Add to the total vote count. 
            # (iterate through the rows and incriment the total_votes variable by 1)
            # (For each row, add the total vote count.) 
        total_votes += 1 

        # 3.5.2 (5) Print the candidate name from each row
        candidate_name = row[2]

        # 3.5.2 (6) Add the candidate name to the candidate list
        #candidate_options.append(candidate_name)
        # 3.5.2 (8) If the candidate does not match existing candidate
        if candidate_name not in candidate_options: 
            # 3.5.2 (9) Add it to the list of candidates
            candidate_options.append(candidate_name)

# 3.5.1 (3) Print the total votes (369,711 without header)
#print(total_votes)
# 3.5.2 (7) Print the candidate list. 
print(candidate_options)

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