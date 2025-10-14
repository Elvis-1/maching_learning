def add_description(**description):
    for prop in description:
        print(prop, ':', description[prop])
    
    print()

def main():
    add_description(name='Elvis', likes ='Singing',church='RCCG',)
    add_description(height='70km', location='United State')
    add_description(city='Lagos State')


main()