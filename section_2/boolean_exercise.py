'''
Ask the user:

1. Are you a student?
2. Do you have pets?
3. Do you smoke?

The program automatically decides whether a property you've applied to rent is available to you.

It should print an appropraite response, like "Property available or Property not available"

The program applies these criteria:

If you are a student, you can only rent the property if you don't have pets and don't smoke.

If you are not a student, you can only rent the property if you smoke or have pets, but not both.

'''
areYouAStudent = input("Are you a student? (yes/no): ").strip().lower() == 'yes'
havePets = input("Do you have pets? (yes/no): ").strip().lower() == 'yes'
smoke = input("Do you smoke? (yes/no): ").strip().lower() == 'yes'

propertyAvailable = False

# if areYouAStudent:
#     propertyAvailable = not havePets or not smoke

#     if propertyAvailable:
#         print("Property available")
#     else:
#         print("Property not available")

# else:   
#     propertyAvailable = havePets or smoke

#     if propertyAvailable:
#         print("Property available")
#     else:
#         print("Property not available")



# Alternative solution

student_can_rent = not havePets and not smoke
non_student_can_rent = not areYouAStudent and not(havePets and smoke)

can_rent = student_can_rent or non_student_can_rent

print("Property available" if can_rent else "Property not available")