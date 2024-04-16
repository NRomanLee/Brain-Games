import random
def gcd(a, b):
    while b != 0:
        a, b = b, a % b 
    return a 
def brain_gcd():
    score = 0
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    for _ in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        question = f"{num1} {num2}"
        print(f"Question: {question}")
        correct_answer = gcd(num1, num2)
        answer = input("Your answer: ")
    
        if int(answer) == correct_answer: 
            print("Correct!")
            score += 1
        else: 
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}")
            return
    print(f"Congratulations! {name}")
def main():
    brain_gcd()
if __name__ == "__main__":
    main()


     
