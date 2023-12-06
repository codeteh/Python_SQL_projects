import random

""" This is intended to an educational game 
to be used as as sort of interview prep warmup for python newbies 
and career switchers """


# List of questions, choices, answers, and explanations.
# The following are questions/explanations in the form of a list consisting of dictionaries consisting of list


interview_questions = [
    {
        'question': "Which of the following is an immutable data type in Python?",
        'choices': ["List", "Tuple", "Set", "Dictionary"],
        'answer': "Tuple",
        'explanation': "Tuples are immutable in Python, which means their elements cannot be changed after creation. Lists (a) are mutable, as their elements can be modified."
    },
    {
        'question': "What is the result of 2 ** 3 ** 2 in Python?",
        'choices': ["64", "512", "12", "72"],
        'answer': "512",
        'explanation': "In Python, the right-to-left order of evaluation is followed, so 3 ** 2 is calculated first, resulting in 9, and then 2 ** 9 is calculated, resulting in 512."
    },
    {
        'question': "What does the pass statement do in Python?",
        'choices': ["It generates a runtime error.", "It is a no-operation statement.", "It is used to declare a variable.", "It is used to exit a loop."],
        'answer': "It is a no-operation statement.",
        'explanation': "The pass statement is a no-operation statement, meaning it does nothing and is often used as a placeholder."
    },
    {
        'question': "What is a dictionary in Python?",
        'choices': ["A mutable data type that stores key-value pairs enclosed in curly braces", "A function that takes a key and a value as arguments and returns a new key-value pair.", "A data type that stores a collection of values in a sequential order.", "Consist of explanations for what variables and functions in the code do"],
        'answer': "A mutable data type that stores key-value pairs enclosed in curly braces",
        'explanation': "A dictionary is a mutable data type that stores key-value pairs. Dictionaries are enclosed in curly braces."
    },
    {
        'question': "Given a list my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5], what will my_list.count(1) return?",
        'choices': ["1", "2", "3", "4"],
        'answer': "2",
        'explanation': "The count() method counts the number of occurrences of a specified element in a list. In this case, it counts how many times 1 appears in my_list."
    },
    {
        'question': "In Python, what does the join() method do when used with strings?",
        'choices': ["It splits a string into a list of substrings", "It concatenates multiple strings into one, using a specified delimiter", "It finds the common elements in two strings", "It reverses the characters of a string"],
        'answer': "It concatenates multiple strings into one, using a specified delimiter",
        'explanation': "The join() method is used to concatenate a list of strings into a single string, using the specified delimiter to separate them."
    },
    {
        'question': "What is the difference between pass and None in Python?",
        'choices': ["pass is a keyword that tells Python to do nothing, while None is a special object that represents the absence of a value", "pass is often used as a placeholder for code that will be written later, while None is often used as the default return value for functions.", "pass can only be used inside functions, while None can be used anywhere in the program.", "pass is a feature used exclusively in JavaScript to skip a step in a loop."],
        'answer': "pass is a keyword that tells Python to do nothing, while None is a special object that represents the absence of a value",
        'explanation': "The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed. Empty code is not allowed in loops, function definitions, class definitions, or in if statements. The None keyword is used to define a null value, or no value at all."
    },
]

# Shuffle the order of questions.
random.shuffle(interview_questions)

# Initialize the score.
score = 0

# Define a function to present a question.
def present_question(question_data, score):
    print(question_data['question'])

    # Shuffle the order of choices.
    random.shuffle(question_data['choices'])

    for i, choice in enumerate(question_data['choices'], start=1):
        print(f"{i}. {choice}")

    # Get the user's choice (1, 2, 3, or 4).
    user_choice = int(input("Enter the number of your choice: "))

    # Check if the user's choice is correct.
    if question_data['choices'][user_choice - 1] == question_data['answer']:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Display the explanation.
    print(question_data['explanation'])
    print("\n")

    return score

# Define a function to present the score.
def present_score(score, total_questions):
    print(f"Your score: {score}/{total_questions}")

# Run the quiz.
for i, question_data in enumerate(interview_questions, start=1):
    print(f"Question {i}:")
    score = present_question(question_data, score)

# Display the final score.
print("Quiz completed!")
present_score(score, len(interview_questions))
