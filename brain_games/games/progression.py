import random

def generate_progression(start, step, length):
    return [start + i * step for i in range(length)]

def brain_progression():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello {name}")
    print("What number is missing in the progression")
    score = 0 

    for _ in range(3):
        start = random.randint(1, 20)
        step = random.randint(1, 10)
        length = 10
        progression = generate_progression(start, step, length)
        hidden_index = random.randint(0, length - 1)
        correct_answer = progression[hidden_index]
        progression[hidden_index] = ".."
        question = " ".join(map(str, progression))
        print(f"Question: {question}")
        answer = input("Your answer: ")

        if int(answer) == correct_answer:
            print("Correct!")
            score += 1 

        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
    print(f"Congratulations, {name}!")
def main():
    brain_progression()
if __name__ == "__main__":
    main()