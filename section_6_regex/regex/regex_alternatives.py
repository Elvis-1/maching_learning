import re

def main():
    text = 'Hello Jack. Hello Zoe. How are you today?'

    # text = re.sub(r"Jack|Zoe|Mart","???",text)
    # text = re.sub(r"Hello (Jack|Zoe|Mart)","???",text)
    text = re.sub(r"Hello (Jack|Zoe|Mart)",r"Hi \1",text)

    print(text)

main()