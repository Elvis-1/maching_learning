"""
Day         Electriciy  Coffea      Cleaning
Monday      50          40          20
Tuesday     30          30          10
Wednessday  20          10          10
"""

"""
Exercise:
1. Get the total for each day
2. Get the total amount spent on electricity etc 
Make it extensible incase more days are added
"""

# analysis steps:
# Step 1: Understand the domain
"This is about calculating weekday budget"
"Real-world context: Budget"
"Core concept: Day = electricity + coffea + cleaning"

# Key understanding:
"""
Each day has expenses"
"We need total for each day"

# Identify Core Components
"Days and utility"
"Relationships:"
One days -> many utilities
One utility -> many days

Operations needed:

Calculate total per day
Calculate total for a utility for the whole days

"""

# Step 3: Map Data Flow
# Lets visualize this:

"""
Input:
Total_Per_day = electricity + coffea + cleaning
Total_usage:
electricity = day1 + day2 + ...
"""

import re

def main():

    text =  """
    Day         Electriciy  Coffea      Cleaning Grossary
    Monday      50          40          20          10
    Tuesday     30          30          10          40
    Wednessday  20          10          10          60
    Thursday    10          5           3           4
"""

  
    lines = re.split(r"\n",text)
    for line in lines:
       
       if re.search(r"^\s$",line):
           continue
       print(f"{line}")

       
       

        

main()







