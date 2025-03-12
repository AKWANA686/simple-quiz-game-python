def quiz_game():
    questions = [
        {"question": "What is the capital of France?", "choices": {"a": "Berlin", "b": "Madrid", "c": "Paris"}, "answer": "c"},
        {"question": "Which of the following is NOT a valid variable name in Python?", "choices": {"a": "my_var", "b": "2var", "c": "_var"}, "answer": "b"},
        {"question": "What is the result of 2 ** 3 in Python?", "choices": {"a": "6", "b": "8", "c": "9"}, "answer": "b"}
    ]
    
    score = 0
    
    for q in questions:
        print("\n" + q["question"])
        for key in q["choices"]:
            print(key + ". " + q["choices"][key])
            
        user_answer = input("Enter your choice (a, b, c): ")
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer is " + q["choices"][q["answer"]])
            
    print("\nYour final score: " + str(score) + " / " + str(len(questions)))
    
    if input("Play again? (yes/no): ") == "yes":
        quiz_game()
    else:
        print("Thanks for playing!")

quiz_game()