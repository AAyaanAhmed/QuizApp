import json

def read_questions(file_name):
    try:
        with open(file_name, "r") as f:
            return json.load(f)
    except:
        return []

def result(score, total):
    percent = (score * 100) / total

    if percent >= 80:
        return "Excellent"
    if percent >= 60:
        return "Good"
    if percent >= 40:
        return "Average"
    return "Needs Improvement"

def start(questions):
    marks = 0
    total = len(questions)

    for num, item in enumerate(questions, 1):
        print(f"\nQuestion {num}")
        print(item["question"])

        for choice in item["options"]:
            print(choice)

        ans = input("Enter option: ").strip().upper()

        if ans == item["answer"]:
            print("Correct!")
            marks += 1
        else:
            print("Incorrect")
            print("Answer:", item["answer"])

    print("\nQuiz Finished")
    print("-" * 25)
    print(f"Score      : {marks}/{total}")
    print(f"Percentage : {(marks/total)*100:.1f}%")
    print(f"Grade      : {result(marks, total)}")

def main():
    data = read_questions("questions.json")

    if not data:
        print("Unable to load quiz questions.")
        return

    print("Welcome to the Quiz")
    print("-" * 25)

    start(data)

main()
