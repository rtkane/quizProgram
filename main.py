quiz = {
    "question1": {
        "question": "What is the capitol of Utah",
        "answer": "Salt Lake City"
    },

    "question2": {
        "question": "what is the capitol of Arizona",
        "answer": "Phoenix"
    },
    "question4": {
        "question": "what is the capitol of California",
        "answer": "Sacramento"
    },

    "question5": {
        "question": "what is the capitol of Oregon",
        "answer": "Salem"
    },
    "question6": {
        "question": "what is the capitol of Washington",
        "answer": "Olympia"
    },
    "question7": {
        "question": "what is the capitol of Idaho",
        "answer": "Boise"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer?")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Your score is: " + str(score) + "\n")
    else:
        print("Wrong")
        print("The answer is: " + value['answer'])
        print("Your score is: " + str(score) + "\n")

print("Final score: " + str(score) + " out of 7")
print("Your percentage is " + str(int(score / 7 * 100)) + "%")
