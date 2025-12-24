
from datetime import datetime,timedelta
"""

A library tracks books, borrowers, and loans. Write a function that:

Input:
- books: list of (book_id, title, max_loan_days)
  Example: [(1, "Python Guide", 14), (2, "Java Basics", 7), (3, "C++ Advanced", 21)]
  
- borrowers: list of (borrower_id, name, max_books)
  Example: [(101, "Alice", 3), (102, "Bob", 2), (103, "Charlie", 5)]
  
- loans: list of (loan_id, book_id, borrower_id, checkout_date, return_date)
  Example: 
  [
    (1001, 1, 101, "2024-01-01", "2024-01-10"),
    (1002, 2, 101, "2024-01-05", "2024-01-20"),  # Late return
    (1003, 3, 102, "2024-01-10", "2024-01-25"),  # Late return
    (1004, 1, 103, "2024-02-01", ""),  # Currently borrowed
  ]

Return:
- A list of borrower names who have any overdue books, sorted alphabetically
- A book is overdue if:
  1. It's not returned (empty return_date) AND current_date > checkout_date + max_loan_days
  2. OR it was returned late: return_date > checkout_date + max_loan_days
- Use current_date = "2024-02-15" for calculations
- Return empty list on any error

Example output: ["Alice", "Bob", "Charlie"] (all have overdue books)
"""


# Step 1: Understand the Domain

# My thought process:

"""
This is about returning a list of those with overdue books by comparing return date with checkout day and max loan days

"Real-world context: Library book tracking"

"Core concept:  return a list of names"
"""

# Key understanding:
"""
Each book has max loan days
Each borrower has maximum number of books

"""

# Step 2: Identify Core Components
#Entities

"""
book: id,title and load days
borrower: id, name and max number of books

Relationships:
borrower -> many books
one book -> many borrowers 


Operations needed:
return the list of borrowers
handle errors
"""

# Step 3: Map Data Flow
# Let me visualize this

"""
input:

list of (book_id, title, max_loan_days)
books: [(1, "Python Guide", 14), (2, "Java Basics", 7), (3, "C++ Advanced", 21)]

list of (borrower_id, name, max_books)
borrowers: [(101, "Alice", 3), (102, "Bob", 2), (103, "Charlie", 5)]


list of (loan_id, book_id, borrower_id, checkout_date, return_date)
loans:
[
    (1001, 1, 101, "2024-01-01", "2024-01-10"),
    (1002, 2, 101, "2024-01-05", "2024-01-20"),  # Late return
    (1003, 3, 102, "2024-01-10", "2024-01-25"),  # Late return
    (1004, 1, 103, "2024-02-01", ""),  # Currently borrowed
]

  Step 1: Validate input
  Step 2: calculate loan status
  status = (return_date - checkout_date) > max_loan_days or current_date > checkout_date + max_loan_days
  Step 3: save in a DS
  {Alice: (name_of_book,status)}
  Step 4: return list of names
""" 

# Step 4: Find Edge Cases:

"""
Empty inputs
Borrower or Book ID not in loan
incomplete borrowers or book list
non numeric max_loan_days or max_books

"""


# Step 5: Design before coding:
def calculateOverDueLoans(books,borrowers,loans):
  if not books or not borrowers or not loans:
    return ''

  borrower_map = dict()
  current_date = datetime.strptime("2024-02-15", "%Y-%m-%d") 

  late_borrowers = []
  book_dict = {}
  borrowers_dict ={}
  loan_status = False


  try:
      # for fast lookup lets convert borrowers and books to dictionary
      #  book_dict = {book_id: (book_name,book_max_days) for (book_id,book_name,book_max_days) in books}

       for book_details in books:
         if len(book_details) != 3:
           return []
         (book_id,book_name,book_max_days) = book_details
         book_dict[book_id] =  (book_name,book_max_days)
       

       for borrowers_details in borrowers:
         if len(borrowers_details) != 3:
           return []
         (borrower_id,borrower,max_books) = borrowers_details
         borrowers_dict[borrower_id] =  (borrower,max_books)
       

      #  borrowers_dict = {borrower_id:  (borrower,max_books) for (borrower_id,borrower,max_books) in borrowers}

    
       for loan in loans:
        
      # extract items from loan
        loan_id,book_id,borrower_id,checkout_date,return_date = loan

     # validate data

        if len(loan) != 5:
          return ''
      
        if not isinstance(checkout_date,str) or not isinstance(return_date,str) or not isinstance(borrower_id,int) or not isinstance(book_id,int) or not isinstance(loan_id,int):
          return []
        
        if not book_id in book_dict or not borrower_id in borrowers_dict:
          return []
       
      # extract book name and max days
        
        book_name,max_loan_days = book_dict[book_id]
        print('Max loan days: ', max_loan_days)

    # extract borrower name and max books
        borrower_name,max_books = borrowers_dict[borrower_id]

     # calculate status
  
        if return_date != '':
          return_date = datetime.strptime(return_date,"%Y-%m-%d")
        if checkout_date != '':
          checkout_date = datetime.strptime(checkout_date,"%Y-%m-%d")
        if return_date != '':
          return_days = return_date
    
        checkout_and_max_loan_days = checkout_date + timedelta(days=max_loan_days) 
        

        if return_date == '' and current_date > checkout_and_max_loan_days:
          loan_status = True
          print('first loan status: ', current_date > checkout_and_max_loan_days)

        if return_date != '':
          if return_days > checkout_and_max_loan_days:
            loan_status = True
            print('Second loan status: ', return_days > checkout_and_max_loan_days,)

        if not  borrower_name in borrower_map:
          borrower_map[borrower_name] = set()

        borrower_map[borrower_name].add(loan_status)
       print('Borrowers Map: ', borrower_map)
        
       
  except  Exception as e:
    print(e)
    return []
 

  
  for name,book_status in borrower_map.items():
    #  print(name,book_status)
     if True in book_status:
      print(name,book_status) 
       
      late_borrowers.append(name)

  return late_borrowers
     
     

     


def main():
    #     list of (book_id, title, max_loan_days)
  books = [(1, "Python Guide", 14), (2, "Java Basics", 7), (3, "C++ Advanced", 21)]

# list of (borrower_id, name, max_books)
  borrowers = [(101, "Alice", 3), (102, "Bob", 2), (103, "Charlie", 5)]


# list of (loan_id, book_id, borrower_id, checkout_date, return_date)
  loans = [
    (1001, 1, 101, "2024-01-01", "2024-01-10"),
    (1002, 2, 101, "2024-01-05", "2024-01-20"),  # Late return
    (1003, 3, 102, "2024-01-10", "2024-01-25"),  # Late return
    (1004, 1, 103, "2024-02-01", ""),  # Currently borrowed
  ]
  print(calculateOverDueLoans(books,borrowers,loans))

main()




