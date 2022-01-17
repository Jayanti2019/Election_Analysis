# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.63.2

## Summary
The analysis of the election show that:
-There were 369,711 votes cast in the election. 
-The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
  
## Challenge Overview
Election commission has requested some additonal data to complete the audit.

1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout

## Challenge Summary
Additional data shows that 
- Counties where the elections were held are:
  - Jefferson
  - Denver
  - Arapahoe
- Voters turn out and percentage of votes for each county:
  - Jefferson county received 10.5% of the toal votes and 38,855 number of votes.
  - Denver county received 82.8% of the toal votes and 306,055 number of votes.
  - Arapahoe county received 6.7% of the toal votes and 24,801 number of votes.
- The county with the highest turnout was:
  - Denver county which received 82.8% of the toal votes and 306,055 number of votes.

## Election-Audit Summary
How can we apply the same code to analyze any elections for Colorado Election Board
I am going to take an example of County election analysis here:
- We are defining county_list as a list and this list populated with different county names in a for loop
  - List definition 
  -  #1: Create a county list and county votes dictionary.
    county_list = []

  - populate the County names into list from the dataset. This is scalable script. If dataset has more counties in it, they will be automatically added to the list.  
  -     # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            
   - Here votes in each county are being counted. Again this is scalable code. We do not have to make any changes to the script evne if data set has more counties in it.
   -         if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0


        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
        
   - Here for each county, script is calculating the percentage of the vote and printing results to terminal
   -  for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        cvotes = county_votes.get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        cvote_percentage = float(cvotes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {cvote_percentage:.1f}% ({cvotes:,})\n")

         # 6d: Print the county results to the terminal.
        print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
  - in the code above Results for each county are saved to a text file for the convience of Colorado Election Board.

            

