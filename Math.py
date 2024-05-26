import random

def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    question = f"What is {num1} + {num2}?"
    correct_answer = num1 + num2
    return question, correct_answer

def main():
    print("Welcome to the Math Quiz!")
    number_of_questions = int(input("Enter the number of questions you want to answer: "))
    
    quiz_history = []
    correct_answers = 0

    for i in range(number_of_questions):
        question, correct_answer = generate_question()
        print(question)
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        is_correct = user_answer == correct_answer
        if is_correct:
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")
        
        quiz_history.append({
            'question': question,
            'correct_answer': correct_answer,
            'user_answer': user_answer,
            'is_correct': is_correct
        })
    
    percentage = (correct_answers / number_of_questions) * 100
    print(f"You answered {correct_answers} out of {number_of_questions} questions correctly.")
    print(f"Your score: {percentage}%")

    view_history = input("Do you want to see your quiz history? (yes/no): ").strip().lower()

    if view_history == 'yes':
        print("Quiz History:")
        for idx, q in enumerate(quiz_history, start=1):
            print(f"Question {idx}: {q['question']}")
            print(f"Your Answer: {q['user_answer']}")
            print(f"Correct Answer: {q['correct_answer']}")
            print(f"Status: {'Correct' if q['is_correct'] else 'Incorrect'}")
            print()

if __name__ == "__main__":
    main()
            