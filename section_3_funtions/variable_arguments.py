def describe_person(name,*attributes):
    print(name)
    print(type(attributes))
    for attribute in attributes:
        print(attribute)

def main():
    describe_person('Brilliant Gulder', 'Joyful','Funny','Playful','God loving')
    print()
    describe_person('Mary Blaster',)

main()
   