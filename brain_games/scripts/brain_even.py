import random
def is_even(number):
    return number % 2 == 0
def brain_even():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ").lower()
        if (is_even(number) and answer == "yes") or (not is_even(number) and answer == "no"):
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{'yes' if is_even(number) else 'no'}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
def main():
        brain_even()
if __name__ == "__main__":
    main()

