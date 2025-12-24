import re

def main():
    text = "You could get a developer job. E.g. in robotics. Maybe. Or web development."


    # results = re.search(r'\w+\.', text)
    # results = re.findall(r'\w{2,}\.', text)

    results = re.findall(r'\s+(\w+)\.(?=\s+|$)',text)

    print(results)

main()