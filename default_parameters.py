def newPatient(name,type = 'cat',age = -1):
    print(name,type,age)

def main():
    newPatient('Biffy', 'dog', 5)
    newPatient('Tiddles','cat')
    newPatient('Bobble')

main()