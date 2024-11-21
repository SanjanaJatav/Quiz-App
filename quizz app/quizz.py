# In-memory data storage
users = {}
scores = {}
logged_in_user = None

def register():
    global users
    print("\n--- Register a New User ---")
    username = input("Enter a Username: ")
    password = input("Enter a Password: ")
    if username in users:
        print("Username already exists. Please try a different one.")
    else:
        users[username] = password
        print("Registration successful!")

def login():
    global logged_in_user
    print("\n--- Login ---")
    username = input("Enter your Username: ")
    if username in users:
        for _ in range(3):  
            password = input("Enter your Password: ")
            if users[username] == password:
                logged_in_user = username
                print("Login successful!")
                return True
            else:
                print("Incorrect password. Try again.")
        print("Maximum attempts exceeded.")
        return False
    else:
        print("Username not found. Please register first.")
        return False

def attempt_quiz():
    
    global scores, logged_in_user
    if logged_in_user is None:
        print("You must log in first to take the quiz.")
        return
    
    quiz = [
        {"question": "What does HTML stand for?", 
         "options": ["A. HyperText Markup Language", "B. High Text Machine Language", "C. Hyper Trainer Markup Language", "D. None of the above"],
         "answer": "A"},
        {"question": "Which programming language is known for its use in web development alongside HTML and CSS?", 
         "options": ["A. Java", "B. Python", "C. JavaScript", "D. C++"],
         "answer": "C"},
        {"question": "Which symbol is used to comment a line in Python?", 
         "options": ["A. #", "B. //", "C. /*", "D. --"],
         "answer": "A"},
        {"question": "What is the value of `2 + 2` in Python?", 
         "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
         "answer": "B"}
    ]
    
    score = 0
    for q in quiz:
        print(f"\n{q['question']}")
        for opt in q['options']:
            print(opt)
        answer = input("Enter your answer (A-D): ").upper()
        if answer == q["answer"]:
            print("Correct!")
            score += 10  
        else:
            print("Incorrect.")
    
    scores[logged_in_user] = score
    print(f"Quiz complete! Your score: {score} points.")

def view_results():
    
    global scores, logged_in_user
    if logged_in_user is None:
        print("You must log in first to see your score.")
        return
    
    if logged_in_user in scores:
        print(f"{logged_in_user}, your score is {scores[logged_in_user]} points.")
    else:
        print("You haven't taken the quiz yet.")

def main():
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Take Quiz")
        print("4. View Results")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            register()
        elif choice == "2":
            if login():
                pass  
        elif choice == "3":
            attempt_quiz()
        elif choice == "4":
            view_results()
        elif choice == "5":
            print("Goodbye! Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
