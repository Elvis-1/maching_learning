import re
"""
[] -> matches one character at a time
"""
def main():
    text = 'abc'

    result = re.match(r"[abc]",text) # match a or b or c

    #print('No match' if result is None else f'"Match: "{result.group()}')


    text = 'abc'

    result = re.match(r"[a-z]+",text) # this matches the first letter from a-z and then the + extends it

    print('No match' if result is None else f'"Match: "{result.group()}')


    text = 'a3b-c.d'

    result = re.match(r"[a-z\d\-\.]+",text) 

    print('No match' if result is None else f'"Match: "{result.group()}')

    'assignment'
    email = 'john.purcell@caveofprogramming.com'

    # result = re.match(r'.*\.\w+',email)

    # result = re.match(r'([a-z\.\-]+)@(\w+)\.(\w+)',email)

    # tutor solution
    result = re.match(r'([a-z][a-z\.\-]+)@(\w+)\.(\w+)',email)

    name,domain, suffix = result.groups()
    print(name,domain,suffix)

    # print('No match' if result is None else f"Match: first group: {result.group(1)}, second group: {result.group(2)} third group: {result.group(3)}")

    'Write a regular expression that would match the email address and extract the different bits of it using capture groups. john.purcell - this bit should be allowed to contain dot and hypen and must start with a lower case letter'


main()