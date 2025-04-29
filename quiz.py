import random

# Sample questions categorized by topic
quiz_data = {
    "Science": [
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "O2", "CO2", "NaCl"],
            "answer": "H2O"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "answer": "Mars"
        }
    ],
    "History": [
        {
            "question": "Who was the first president of the United States?",
            "options": ["George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams"],
            "answer": "George Washington"
        },
        {
            "question": "In which year did World War II end?",
            "options": ["1945", "1939", "1918", "1963"],
            "answer": "1945"
        }
    ]
}

def display_categories():
    print("\nAvailable Categories:")
    for i, category in enumerate(quiz_data.keys(), 1):
        print(f"{i}. {category}")

def get_category_choice():
    while True:
        try:
            choice = int(input("\nChoose a category number: "))
            categories = list(quiz_data.keys())
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Enter a valid number.")

def run_quiz(questions):
    score = 0
    user_answers = []

    random.shuffle(questions)  # Shuffle question order

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        options = q["options"]
        random.shuffle(options)

        for j, option in enumerate(options, 1):
            print(f"  {j}. {option}")

        while True:
            try:
                answer = int(input("Your answer (number): "))
                if 1 <= answer <= len(options):
                    selected = options[answer - 1]
                    correct = q["answer"]
                    if selected == correct:
                        print("✅ Correct!")
                        score += 1
                    else:
                        print(f"❌ Wrong. Correct answer: {correct}")
                    user_answers.append((q["question"], selected, correct))
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Enter a valid number.")

    print(f"\n🎉 Quiz Over! Your score: {score}/{len(questions)}")
    print("\n📋 Review:")
    for idx, (question, user_ans, correct_ans) in enumerate(user_answers, 1):
        status = "✅" if user_ans == correct_ans else "❌"
        print(f"{idx}. {question}\n   Your Answer: {user_ans} | Correct Answer: {correct_ans} {status}")

def main():
    print("=== Welcome to the Quiz Game ===")
    display_categories()
    category = get_category_choice()
    print(f"\n📚 Starting quiz in category: {category}")
    run_quiz(quiz_data[category])

if __name__ == "__main__":
    main()
