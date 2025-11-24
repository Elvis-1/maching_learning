"""
A company needs to schedule employees for shifts. Write a function that:

Input:
- employees: list of employee names ["Alice", "Bob", "Charlie"]
- shifts: list of shift durations in hours [8, 6, 4, 8, 4] 
- assignments: list of (employee_index, shift_index) pairs [(0,0), (1,1), (2,2), (0,3), (1,4)]

Return:
- The name of the employee with the most total hours worked
- If there's a tie, return the employee who appears first in the employees list
- Return empty string on any error

Example:
employees = ["Alice", "Bob", "Charlie"]
shifts = [8, 6, 4, 8, 4]
assignments = [(0,0), (1,1), (2,2), (0,3), (1,4)]

Alice: shifts[0] + shifts[3] = 8 + 8 = 16 hours
Bob: shifts[1] + shifts[4] = 6 + 4 = 10 hours  
Charlie: shifts[2] = 4 hours
Return: "Alice"

"""

# Step 1: Understand the Domain

# My thought process:

"""
This is about calculating the total hours of each employee and getting the name of the employee with the highest

Real-world context: Employee reward system 

Core concept: max of total list of hours

"""

# Step 2: Identify Core Components
# Entities:

"""
Employee: name + hours

Operations needed:
Calculate total hours of each employee
Find maximum
Handle errors
"""

# Step 3: Map Data Flow
# Let me visualize this:

"""
input:
employees = ["Alice", "Bob", "Charlie"]
shifts = [8, 6, 4, 8, 4]
assignments = [(0,0), (1,1), (2,2), (0,3), (1,4)]

step 1: validate inputs
step 2: calculate total hours of each employeee
Alice: shifts[0] + shifts[3] = 8 + 8 = 16 hours
Bob: shifts[4] + shifts[1] = 6 + 4 = 10 hours
Charlie: shifts[2] = 4 hours

step 3: find max: 16
step 4: return Alice
"""

# Step 4: Find Edge Cases
# Let me brainstorm potential issues:
"""
Empty inputs:
employee = []
shift = []
assignments = []

"""

# Step 5: Design Before Coding
def find_employee_with_heighest_hours(employees, shifts,assignments):


    if not employees or not shifts or not assignments:
        print('Invalid inputs')
        return
    
    employee_and_shift_index = dict()
    max_hours = 0
    highest_employee = ''

    # extract employee with their shift index from assignment list
    try:
        # data validatan

        for i in range(0,len(employees)):
            current_employee = str(employees[i])
            for j in range(0,len(assignments)):
                current_assigment = assignments[j]
            employee_index = int(current_assigment[0])
            shift_index = int(current_assigment[1])
            if employee_index < 0 or shift_index < 0:
                return 'No negative values is allowed'
            if i == employee_index:

                if not current_employee in  employee_and_shift_index:
                   employee_and_shift_index[current_employee] = set()
                
                employee_and_shift_index[current_employee].add(shift_index)
        for employee, shift in employee_and_shift_index.items():
        
        
            total = 0
            for i in shift:
                total += shifts[i]
                if total > max_hours:
                    max_hours = total
                    highest_employee = employee
    except:
         return ''
    return highest_employee









    

def main():
    employees = ["Alice", "Bob", "Charlie"]
    shifts = [8, 6, 4, 8, 4]
    assignments = [(0,0), (1,1), (2,2), (0,3), (1,4)]
    print(find_employee_with_heighest_hours( employees,shifts,assignments))

main()




