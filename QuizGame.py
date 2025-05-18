import requests
import random
import html

def fetch_questions(amount=5):
    url = f"https://opentdb.com/api.php?amount={amount}&type=multiple"
    response = requests.get(url)
    data = response.json()
    return data['results']

def start_quiz():
    score = 0
    questions = fetch_questions()

    for i, question in enumerate(questions):
        print(f"\nQuestion {i + 1}: {html.unescape(question['question'])}")
        options = question['incorrect_answers'] + [question['correct_answer']]
        options = [html.unescape(opt) for opt in options]
        random.shuffle(options)

        for idx, opt in enumerate(options):
            print(f"{idx + 1}. {opt}")

        try:
            answer = int(input("Your answer (1-4): "))
            if options[answer - 1] == html.unescape(question['correct_answer']):
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer was: {question['correct_answer']}")
        except (ValueError, IndexError):
            print("❌ Invalid input. Skipping question.")

    print(f"\n🎯 Quiz Over! Your final score: {score}/{len(questions)}")

def main():
    print("🎉 Welcome to the Quiz Game! 🎉")
    while True:
        start_quiz()
        choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if choice not in ['yes', 'y']:
            print("👋 Thanks for playing! See you next time.")
            break

main()
