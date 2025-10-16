def ask_user_status():
    status = input('Are you a student? (y/n): ').strip().lower()

    if status == 'y':
        print("Welcome, student!")
    elif status == 'n':
        print("Welcome, guest!")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

ask_user_status()