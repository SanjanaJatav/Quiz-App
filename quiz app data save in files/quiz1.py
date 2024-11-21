logged_in = False
logged_user = ''

def register():
    with open('register.txt', 'a') as reg_file:
        username = input("Enter your Username: ")
        password = input("Enter your Password: ")
        enrollment = input("Enter your Enrollment Number: ")
        college = input("Enter your College Name: ")
        reg_file.write(f"{enrollment},{username},{password},{college}\n")
    
    with open('logindetails.txt', 'a') as login_file:
        login_file.write(f"{enrollment},{password}\n")
    
    print("Registration successful!\n")

def login():
    global logged_in, logged_user
    enrollment = input("Enter your Enrollment Number: ")
    
    try:
        with open('logindetails.txt', 'r') as login_file:
            for line in login_file:
                stored_enrollment, stored_password = line.strip().split(',')
                if stored_enrollment == enrollment:
                    attempts = 3 
                    while attempts > 0:
                        entered_password = input("Enter your Password: ")
                        if entered_password == stored_password:
                            print("Login successful!")
                            logged_in = True
                            logged_user = enrollment
                            return True
                        else:
                            attempts -= 1
                            print(f"Incorrect password! {attempts} attempts left.")
                    print("Too many incorrect attempts. Try again later.")
                    return False
            print("Enrollment number not found. Please register first.")
    except FileNotFoundError:
        print("Error: Login details file not found.")
    
    return False

def attempt_quiz():
    if not logged_in:
        print("Please log in first to attempt the quiz.")
        return

    total_score = 0
    try:
        with open("D:\Sanjana\sanjana 02\quizz app\quiz app data save in files\questions.txt", "r") as quiz_file:
            questions = quiz_file.readlines()
            for question in questions:
                parts = question.strip().split(',')
                if len(parts) < 6:  
                    print(f"Skipping invalid question: {question}")
                    continue
                
                print(f"\n{parts[0]}")
                for i in range(1, 5):
                    print(parts[i])

                answer = input("Enter Answer (A-D): ").upper()
                while answer not in ['A', 'B', 'C', 'D']:  
                    print("Invalid input! Please choose A, B, C, or D.")
                    answer = input("Enter Answer (A-D): ").upper()
                
                if answer == parts[5]:
                    total_score += 10
                    print("Correct!\n")
                else:
                    print("Incorrect.\n")

        with open("score.txt", "a") as score_file:
            score_file.write(f"{logged_user},{total_score}\n")
        
        print(f"Quiz complete! Your total score is: {total_score} points.")
    except FileNotFoundError:
        print("Error: Question file not found.")

def show_result():
    if not logged_in:
        print("Please log in first to view your score.")
        return
    
    try:
        with open("score.txt", "r") as score_file:
            found = False
            for line in score_file:
                roll, score = line.strip().split(',')
                if roll == logged_user:
                    print(f"Your score: {score} points.")
                    found = True
                    break
            if not found:
                print("No score found for your user.")
    except FileNotFoundError:
        print("Error: Score file not found.")

def main_menu():
    while True:
        print("\nMenu:")
        print("1. Attempt Quiz")
        print("2. View Result")
        print("3. Logout")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                attempt_quiz()
            elif choice == 2:
                show_result()
            elif choice == 3:
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please choose between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

def main():
    global logged_in
    while True:
        print("\nWelcome to the Quiz System!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                register()
            elif choice == 2:
                if login():  
                    main_menu()
            elif choice == 3:
                print("Goodbye! Thanks for using the Quiz System.")
                break
            else:
                print("Invalid choice. Please choose between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

main()
