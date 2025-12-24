import re

def main():
    text = 'zigzag'
    result = re.match("z.g",text)
    print("No result" if result is None else f"Match: {result.group()}")

    text = 'zigzagfkfkfg'
    result = re.match("z.*g",text) # .* is greedy
    print("No result" if result is None else f"Match: {result.group()}")

    text = 'zigzag'
    result = re.match("z.*?g",text) # ? limits .*
    print("No result" if result is None else f"Match: {result.group()}")

    text = 'zigzag'
    result = re.match("z.*?",text)
    print("No result" if result is None else f"Match: {result.group()}")

    text = 'zigzag'
    result = re.match("z.*?$",text) # ? limits .*
    print("No result" if result is None else f"Match: {result.group()}")

main()