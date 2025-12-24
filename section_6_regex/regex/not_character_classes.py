import re

def main():
    tag = '<div id="123">Hello</div>'

    result = re.match(r"<[^>]+>[^<>]+<[^>]+>",tag)

    print(result.group())

main()