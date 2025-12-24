import re

def main():
    text = 'Oranges are nice'

    regex = re.compile('O\w+s') # flags will be placed here

    result = re.sub(regex,'Bananas',text)

    print(result)

main()