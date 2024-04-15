import random
import prompt
def brain_calc():
    score = 0
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression")
    for _ in range(3):
        num1 = random.randint(1, 30)
        num2 = random.randint(1, 30)
        operator = random.choice(['+', "-", "*"])
        question = f"{num1} {operator} {num2}"
        print(f"Question: {question}")
        answer = prompt.string("Your Answer: ")
        correct_answer = eval(question)
        if int(answer) == correct_answer: 
            print("Correct!")
            score += 1
            continue
        else: 
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}")
            return
    print(f"Congratulations! {name}")
def main():
    brain_calc()
if __name__ == "__main__":
    main()
