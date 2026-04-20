text = """
Day         Electriciy  Coffea      Cleaning
Monday      50          40          20
Tuesday     30          30          10
Wednessday  20          10          10
"""

def put_in_list():
    text.split(' ')
    print(list(map(lambda x:x.split(),  list(filter(lambda x:x if x is not ' ' else '', text.split('\n'))))))

def main():
    put_in_list()

if __name__ == '__main__':
    main()