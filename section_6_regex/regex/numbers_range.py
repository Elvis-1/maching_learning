import re

"""
{number} - the number of the preceding pattern
{minimum_num, maximum_num} - range of the preceding pattern
"""
def main():
    email = "elvis@ifnotGod.com"
    result = re.match(r"\w{5}@\w{2,30}\.\w{3,10}",email)

    print('No match' if result is None else f'Match: {result.group()}')

main()