import re

"""
create a set with the character that are not white space
and a set containing all the character that not alphanumeric.

\S: not space = [^\s]
\W: not alphanumeric = [^\w]
\D: not a digit = [^\d]
"""



def main():
    text= r'''
    On 12/08/2024, Alex said:
    "I paid $45.50 for 3 books — unbelievable!"

    Later, at 9:30 PM, he emailed admin@book-store.io
    and wrote: Are returns allowed? Yes/No.
    '''



    character_with_no_white_space = re.findall(r'([^\s])', text)
    not_alphanumeric_text = re.findall(r'\W',text)

    not_white_space_set = set(character_with_no_white_space)
    not_alphanumeric_set = set(not_alphanumeric_text)
    print(not_alphanumeric_set)



main()