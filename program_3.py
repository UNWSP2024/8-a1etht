#Programmer: Alethea Lo
#Date: 3/16/25
#Title: Capital Quiz

import random

def state_capital_quiz():
    states_capitals = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Connecticut": "Hartford",
        "Delaware": "Dover",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta"
    }

    correct = 0
    incorrect = 0

    states = list(states_capitals.keys())
    random.shuffle(states)

    for state in states:
        answer = input(f"What is the capital of {state}? ").strip()
        if answer.lower() == states_capitals[state].lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect! The capital of {state} is {states_capitals[state]}.")
            incorrect += 1

    print(f"\nQuiz Complete! Correct: {correct}, Incorrect: {incorrect}")

state_capital_quiz()