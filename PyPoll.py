################ Open and Read csv files using a direct path #######################
# Add our dependencies.
import csv
dir(csv)
# Assign a variable for the file to load and the path 
file_to_load = 'Resources\election_results.csv'
# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()
    
# Open the election results and read the file 
with open(file_to_load) as election_data:
    print(election_data)

################ Open and Read csv files using a indirect path #######################

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Print the file object.
    print(election_data)

################### Open a file and add to it ######################
import os
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")
# Write three counties to the file.
outfile.write("Arapahoe, ")
outfile.write("Denver, ")
outfile.write("Jefferson")
outfile.write("Arapahoe, Denver, Jefferson")
# Write three counties to the file.
outfile.write("Arapahoe\nDenver\nJefferson")
# Close the file
outfile.close()

################ Read and print the data from a file #################

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

     # Print each row in the CSV file.
    for row in file_reader:
        print(row)  


############ Read and print the header row in the dataset##############


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    header = next(file_reader)
    print (header)
