import random

people = ['Liam','Olivia','Noah','Ava','James','Amelia','William','Emma']

skills = ['coding','art','testing','management','marketing',]

days = ['Monday', 'Tuesday','Wednessday','Thursday','Friday']


"""
1.  Randomly assign the two skills to each person. Store this information in a suitable data structure

2.  Write a program which prints the list of days four times, and for each day prints the names of three people who will work on that day. Also print the total set of skills from all the people combined for each day

The people should be chosen for each day in the order they are found in the people list, with no one person being chosen to work more often than any other
"""

# Step 1: Understand the Domain
# My thought process: 
"""
1. This is about randomly assigning skills
"Core concept: person = 'skill1,skill2"

2. This is about printing days four times with three names
"Core concept: 

"""

# Step 2: Identify Core Components
# Entities:
"""
People: a list of persons
Skills: a list of skills

Operations needed:
random assignment of skills
handle errors
"""

# Step 3: Map Data Flow
# Let me visualize this:

"""
inputs
people = ['Liam','Olivia','Noah','Ava','James','Amelia','William','Emma']

skills = ['coding','art','testing','management','marketing',]

Step 1: Validate input
Step 2: Randomly assign
Liam:'coding','art'
Olivia: 'art','testing'
Noah:'testing','management'
Ava: 'management','marketing'

Step 3: Store in a suitable container
Step 4: Return {'Liam:{'coding','art'}',...}
"""
#Step 4: Find Edge Cases
# Let me brainstorm potential issues:

"""
Empty inputs
Data validation
"""

# Step 5: Design Before Coding

def randonly_assign_skills(people,skills):

    if not people or not skills:
        return 'Invalid inputs'
    
    
    person_with_skills = {}
    
    for person in people:
        skillset = set()
        while len(skillset) < 2:
            random_choice = random.choice(skills)
            skillset.add(random_choice)
        person_with_skills[person] = skillset

    

            
          
    return person_with_skills
person_index = 0
def choose_person():
    global person_index
    person = people[person_index % len(people)]
    person_index += 1
    return person
def main():
    people = ['Liam','Olivia','Noah','Ava','James','Amelia','William','Emma']

    skills = ['coding','art','testing','management','marketing',]

    days = ['Monday', 'Tuesday','Wednessday','Thursday','Friday']


  
    skills_set = randonly_assign_skills(people,skills)

    for i in range(4):
        for day in days:
            skill = set()
            people = [choose_person() for x in range(3)]
            for person in people:
               skill.update(skills_set[person])
            print(day,end=': ')
            print(', '.join(people), end='---')
            print(', '.join(skill))



main()






