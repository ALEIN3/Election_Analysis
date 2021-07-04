# Election_Analysis

## Overview
The purpose of this project is to make an audit to a dataset, and this dataset contains data for an election, where we have provided for each vote the following, the Ballot ID, County, and the candidate name.
Our mission is to discover how many voters were involved in this election, how many votes were received in each county, which county has the largest turnout, how many votes were obtained for each candidate, and the candidate who won the election.
In the end, we will provide the election commission department with our audit. For this project, we will use the programing language Python.

## Election-Audit Results
I will introduce the analysis outcomes in the following section, and I will provide a few examples from my code that I used to get some of those outcomes:
### There are total votes of 369,711
I was able to generate this outcome by using the following pieces of codes, where I created a variable and assigned to it the value of zero (0), then I used a (For) loop that goes over all the rows in the sheet, except the header (it’s part of the script to ignore the first row), and it increases the variable by 1 for each vote(row) that part of the loop.
### we can see that we have three counties, and the results for those counties came as following:
#### Jefferson: 10.5% (38,855)
We can translate the numbers above as following, Jefferson County received 38,855 votes out of the total votes, which equal 369,711 votes, and that means the votes of Jefferson County equal to 10.5% of the total votes 
#### Denver:82.8% (306,055)
We can translate the numbers above as following, Denver County received 306,055 votes out of the total votes, which equal 369,711 votes, and that means the votes of Denver County equal to 82.8% of the total votes
#### Arapahoe:6.7% (24,801)
We can translate the numbers above as following, Arapahoe County received 24,801 votes out of the total votes, which equal 369,711 votes, and that means the votes of Arapahoe County equal to 6.7% of the total votes 
### Based on the previous outcomes, we found that the county of Denver has the highest number of votes 
I created two variables. The first variable is (Counties_votes), and I assigned to it Zero value (0), the second one is (County_with_highest_count), and assigned to it an empty value (“ ”), so it will be recognized as a string. The next step was starting a loop to go over the names of the counties which represent the keys in the County_votes dictionary that I created in the previous step, to get back the count of votes for each county, which represent the values from the County_votes dictionary, and they will be under the county_count variable. The next step will be creating a conditional statement to compare the county_count with the Counties_votes, then assign the highest value to the Counties_votes variable and assign the county's name to the County_with_highest_count. By the end of the loop, we will end up with the highest count of votes among all the counties which was assigned to the Counties_votes variable, and the name of that county was assigned to the County_with_highest_count variable.
I can show here a few pieces of the code that I used for this outcome as following in the images

### after checking the counties results, it is time to check the candidates' results, we have here three candidates and the results for those candidates came as following:

#### Charles Casper Stockham: 23.0% (85,213)
We can translate the numbers above as following, Charles Casper Stockham received 85,213 votes out of the total votes, which equal 369,711 votes, and that means the votes of Charles Casper Stockham equal to 23.0% of the total votes 

#### Diana DeGette: 73.8% (272,892)
We can translate the numbers above as following, Diana DeGette received 272,892 votes out of the total votes, which equal 369,711 votes, and that means the votes of Diana DeGette equal to 73.8% of the total votes

#### Raymon Anthony Doane: 3.1% (11,606)
We can translate the numbers above as following, Raymon Anthony Doane received 11,606 votes out of the total votes, which equal 369,711 votes, and that means the votes of Raymon Anthony Doane equal to 3.1% of the total votes	

### Based on the above candidates’ outcomes, we can say that Diana DeGette won the election race with 73.8% of the votes, which equals 272,892 votes.

# Election-Audit Summary:
At the end of this audit, and after analyzing the data that we received from the election commission department, we found plenty of helpful, clean, and neat results. The main factor in reaching those outcomes is the programing language that we used, and it is Python.
I recommend to the election commission department to consider the following script to audit future elections data. The reason for my proposal is how easy the use of this script is. 
I will explain how we can change few entries, and you will be able to use it for many other datasets with the same structure
-We can change the file that we read the data from in the script and can get the same analysis for the new dataset, plus we can do the same for the file that we are writing to, 
-The flexibility does not stop at this level. So, for example, if we have more data like more columns included in the dataset, we can change a small number in the script, and that will change the column that we pull the data from, and we still can get the same analysis.
