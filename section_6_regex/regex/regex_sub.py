import re

def main():
    text = "Hello Elvis, how are you?"

    result = re.sub(r"E\w+",'Precious',text)
    
    

    print(result)

main()