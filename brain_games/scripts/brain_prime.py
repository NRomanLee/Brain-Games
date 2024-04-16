import random
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def brain_prime():
    score = 0
    print("Welcome to The Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello {name}")
    print("Answer yes if given number is prime. Otherwise answer 'no'.")
    for _ in range(3):
        random_number = random.randint(1, 50)
        print(f"Question: {random_number}")
        correct_answer = "yes" if is_prime(random_number) else "no"
        user_answer = input("Your answer: ")
        if user_answer.lower() == correct_answer:
            print("Correct!")
            score += 1
        else: 
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}")
            return
    print(f"Congratulations! {name}")
def main():
    brain_prime()
if __name__ == "__main__":
    main()
           


    