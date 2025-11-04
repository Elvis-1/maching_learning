def main():
    months = {
        'Jan':'January',
        'Feb':'February',
        'Mar':'March'
    }

    print(months)
    months2 = months.copy()
    print(months2)
    print()

    months.pop('Jan')
    print(months)
    print(months2)

    months3 = {key:value for (key,value) in months.items()}
    print()
    print(months3)



main()