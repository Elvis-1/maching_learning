import re

"""
. → one character
.* = any characters, unlimited length
* → “repeat previous thing 0 or more times”


Summary — rules of thumb


* applies to the preceding token (e.g. r* is zero-or-more r)

.* = any sequence of characters (most common for “anything in between”)

re.match checks from the start but doesn't require matching the whole string

""" 

def main():
    text = 'drooooooooooold'

  
    #result = re.match('dr.*l',text)
    result = re.match('dr*l',text)

    if result is None:
        print('Input does not match')
    else:
        print(result.group())

main()