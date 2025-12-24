import re

# capture groups and non capture groups

def main():
    email = 'one.two.three.four@itestified.com'

    # result = re.match(r'(\w+\.)*',email) # we successfully repeated a match using capture groups

    result = re.match(r'((?:\w+\.)*)\w+@\w+\.\w+',email) # ?: turns the capture group bracket into a normal grouping bracket and nothing is saved in the capture groups. Adding an external capture group bracket, captures the group

    if result is None:
        print('No match')

    else:
        print(result.group(0))
        print(result.groups())

main()