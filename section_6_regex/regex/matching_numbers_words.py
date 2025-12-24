import re

"""
\w : Matches alphanumeric characters
+  : Matches one or more, as many as possible
\s : Maches a space
\d : Matches digits
"""
def main():
    text = "The temperature is 37."
    result = re.match('\w+\s\w+\s\w+\s\d+\.',text)
    print('No match' if result is None else f"'{result.group()}'")

main()