import re

def main():
    text = ' Say Hello Bob'
    # result = re.match(r"^\w+\s\w+",text) # no match
    # result = re.search(r"\w+\s\w+",text) # match
    result = re.match(r".*bob",text, re.IGNORECASE) 

    result = re.sub(r"bob",'Zoe',text,flags=re.IGNORECASE)

    print(result)

main()