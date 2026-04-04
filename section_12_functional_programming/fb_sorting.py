def main():
    animals = ['dog','lion','badger','elephant','cat']
    animals = sorted(animals)
    print(animals)


    def order(item):
        return len(item)
    
    animals = sorted(animals, key=order, reverse=True)
    print(animals)

    animals.sort(key=lambda i:len(i), reverse=True)
   

    print('Using lambda')
    print(animals)


    


if __name__ == '__main__':
    main()