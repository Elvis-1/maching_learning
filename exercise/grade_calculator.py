"""
Write a function that takes:
- A list of students: ["Alice", "Bob", "Charlie"]
- A list of grades: [[85, 90, 78], [92, 88, 95], [76, 82, 80]]
- Return the student with the highest average grade

If inputs are invalid, return empty string.


"""

# Step 1: Understand the Domain

# My thought process:

"This is about calculating student averages and finding the best performer"

"Real-world context: teacher grading students, academic ranking"

"Core concept: average = sum of grades / count of grades"

# Key understanding:

"""
Each student has multiple grades

We need averages for comparison

Simple ranking system
"""

# Step 2: Identify Core Components
# Entities:

"""
Student: name + list of grades

Grade Set: collection of numerical scores

Relationships:

One student → multiple grades

Grades → average calculation

Averages → comparison

Operations needed:

Calculate averages

Compare averages

Find maximum

Handle errors
"""


# Step 3: Map Data Flow
# Let me visualize this:

"""
Input:
Students: ["Alice", "Bob", "Charlie"]
Grades:   [[85,90,78], [92,88,95], [76,82,80]]

Step 1: Validate input
Step 2: Calculate averages
  Alice: (85+90+78)/3 = 84.33
  Bob: (92+88+95)/3 = 91.67  
  Charlie: (76+82+80)/3 = 79.33

Step 3: Find maximum average → Bob (91.67)
Step 4: Return "Bob"

"""


#Step 4: Find Edge Cases
# Let me brainstorm potential issues:

"""
Empty inputs:

students = []

grades = []

Mismatched lengths:

3 students but 2 grade lists

2 students but 3 grade lists

Invalid data:

Negative grades

Grades > 100 (if that's our scale)

Non-numeric grades

Empty grade lists

Tie scenarios:

Two students with same average

(Problem doesn't specify tie-breaker)

Boundary cases:

Single student

Single grade per student

Very large grade lists

"""
# Step 5: Design Before Coding
def find_top_student(students, grades):
    # 1. Validate input
    if not students or not grades:
        return ""
    if len(students) != len(grades):
        return ""
    
    # 2. Process each student
    best_student = ""
    best_average = -1
    
    for i in range(len(students)):
        student_grades = grades[i]
        
        # Validate grades
        if not student_grades:
            continue  # or return "" depending on requirements
            
        # Calculate average
        try:
            average = sum(student_grades) / len(student_grades)
        except:
            return ""  # Invalid grades
            
        # Check if this is the best so far
        if average > best_average:
            best_average = average
            best_student = students[i]
    
    return best_student


def fnd_top_student(students,grades):
    if not students  or not grades:
        print('invalid input')
        return
    if len(students) != len(grades):
        print('invalid length')
        return
    
    max_average = -1
    best_student = ''
    student_total_grade = 0

    for i in range(0,len(grades)):
        student_grades  = grades[i]
        try:
            student_total_grade = sum(student_grades)
        except:
            return ""
        
        # average
        average = student_total_grade / len(student_grades)

        if average > max_average:
            max_average = average
            best_student = students[i]
        
    return [max_average,best_student]



    
def main():

    students =    ["Alice", "Bob", "Charlie"]
    grades =    [[85,90,78], [92,88,95], [76,82,80]]

    print(fnd_top_student(students,grades))
main()