import re

def main():
    text = """
        one
        two
        three
    """

    print(re.match(r".*one",text,re.DOTALL)) # . matches basically all character except newlines, to match new lines, add the flag DOTALL

main()