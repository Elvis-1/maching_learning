"""
Problem: Book Inventory
Given:
- book_titles: ["Python Guide", "Java Basics", "C++ Advanced"]  
- book_copies: [5, 3, 7]
- book_prices: [29.99, 24.99, 34.99]

Return the title of the book with highest total value (copies × price)
Return empty string on error.

"""

#  STEP 1 - UNDERSTAND THE DOMAIN

"""
it is about calculating the highest total value of a book and returning its title
Real world - book inventory in a library or book shop

Core concept = totol number of book_copy * book price
"""

# STEP 2 - CORE COMPONENTS
"""
book: list of book titles
book value: price * copies

Operations needed:
Calc value (price * copies)
Compare value
Take highest
Handle Errors
"""

# Step 3 - Map data flow:
# lets visualize it

"""
inputs:
- book_titles: ["Python Guide", "Java Basics", "C++ Advanced"]  
- book_copies: [5, 3, 7]
- book_prices: [29.99, 24.99, 34.99]

step 1: Validate inputs
step 2: calculate values

Python Guide: (5*29.99) = ...
Java Basics: (3*24.99) = ...
C++ Advanced: (7*34.99) = ...

find the higest value (244.93)

return C++ Advanced (244.93)
"""

# Step 4: Find Edge Cases

"""
Empty inputs:

book_titles = []
book_copies = []
book_prices = []

mismatched length

len(book_titles) != len(book_copies)
"""

# Coding

def find_highest_book_value(book_titles,book_copies,book_prices):
    
    # validation
    if not book_titles or not book_copies or not book_prices:
        print('Invalid input')
        return
    if len(book_titles) != len(book_copies):
        print('Invalid data')
        return
    if len(book_titles) != len(book_prices):
        print('Invalid data')
        return
    if len(book_prices) != len(book_copies):
        print('Invalid data')
        return
    
    # initialize data
    max_value = 0
    book_title = ''
    # calulate value
    # value = [book_copy * book_price for book_copy,book_price in zip(book_copies,book_prices)]
    for i in range(0,len(book_titles)):

        # data validation
        try:
            copies = int(book_copies[i])
            price = float(book_prices[i])

            if copies < 0 or price < 0:
                return "No Negative values allowed"
            value = copies * price
            if max_value < value:
                max_value = value
                book_title = book_titles[i]
            
            

            
        except Exception as e:
            print('This is the error'+ str(e))
            return ''      
    
    return [book_title,max_value]


   



def main():
    book_titles = ["Python Guide", "Java Basics", "C++ Advanced"]  
    book_copies = [5, 3, 7]
    book_prices = [29.99, 24.99, 34.99]
    print(find_highest_book_value(book_titles,book_copies,book_prices))
        # Edge case: empty input
    print(find_highest_book_value([], [], []))  # ""
    
    # Edge case: mismatched lengths
    print(find_highest_book_value(["A", "B"], [1], [2, 3]))  # ""
    
    # Edge case: negative values
    print(find_highest_book_value(["A", "B"], [1, -1], [2, 3]))  # "

main()



