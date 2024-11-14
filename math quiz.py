import random
import time
def math_quiz():
    count = 0
    max_questions = 5
    
    while count < max_questions:
        number1 = random.randint(0, 10)
        number2 = random.randint(0, 10)
        operators = ["+", "-", "*", "/"]
        selected_operator = random.choice(operators)

        if selected_operator == '+':
            question = f"What is {number1} + {number2}?"
            answer = number1 + number2
        elif selected_operator == '-':
            question = f"What is {number1} - {number2}?"
            answer = number1 - number2
        elif selected_operator == '*':
            question = f"What is {number1} * {number2}?"
            answer = number1 * number2
        else:  # division
            while number2 == 0:
                number2 = random.randint(1, 10)
            question = f"What is {number1} / {number2}?"
            answer = number1 / number2

        print(question)
        user_answer = float(input("Your answer: "))
        
        if user_answer == answer:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {answer:.2f}")
            
           
        
        count += 1

    return "Quiz over!"

print(math_quiz())
