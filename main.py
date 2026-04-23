import json
from quiz import run_quiz
from storage import add_score, get_top_scores

# Load Data
with open("questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)


def main():
    print("================================")
    print("    WELCOME TO THE QUIZ GAME    ")
    print("================================\n")
    print("  ANSWER BY TYPING A, B, C or D \n")

    print("1. Play Quiz")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "2":
        print("Thanks for playing!")
        return "exit"

    elif choice == "1":
        name = input("Enter your name: ")
        score = run_quiz(questions)

        add_score(name, score)

        percentage = score / len(questions) if questions else 0

        print("\n============================")
        print(f"Final Score: {score}/{len(questions)}")
        print("============================\n")

        # feedback
        if percentage == 1:
            print("Perfect Score 🎉")
        elif percentage >= 0.5:
            print("Good Job!")
        else:
            print("Better Luck Next Time")

        # leaderboard
        print("\n🏆 Top Scores:")
        for i, entry in enumerate(get_top_scores(), start=1):
            print(f"{i}. {entry['name']} - {entry['score']}")

        return "done"

    else:
        print("Invalid option. Please choose 1 or 2.")
        return "invalid"


# replay loop
while True:
    result = main()

    if result == "exit":
        break

    again = input("\nPlay again? (y/n): ").lower()

    if again != "y":
        print("Thanks for playing!")
        break