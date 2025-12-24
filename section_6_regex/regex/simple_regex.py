import re
def main():
    text = 'dig'
    #result = re.match("dog",text)
    result = re.match("d.g",text) # checking for any single character between between d and g
    print(result is not None)


main()