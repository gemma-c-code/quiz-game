import random


def ask_question(q):
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    answer = input("Your Answer: ").strip().upper()

    while answer not in ["A", "B", "C", "D"]:
        answer = input("Please answer using A, B, C or D: ").strip().upper()

    if answer == q["answer"]:
        print("Correct")
        return 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}")
        return 0
    
def run_quiz(questions):
    score = 0

    q_copy = questions.copy()
    random.shuffle(q_copy)

    for q in q_copy:
        score += ask_question(q)
        print(f"Current Score: {score}/{len(q_copy)}")

    return score