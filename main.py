from random import randint

def choose_level():
    difficulty_level = (input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
    rand_num = randint(1,100)

    if difficulty_level == 'easy':
        num_of_tries = 10
    elif difficulty_level == 'hard':
        num_of_tries = 5
    else:
        print("\nYou have entered an invalid choice!")
        choose_level()

    print(f"\nYou have {num_of_tries} attempts remaining to guess the number.")
    guess = input("Make a guess: ")

    if guess == rand_num:
        print(f"You got it! The answer was {rand_num}")
    elif guess > rand_num:
        num_of_tries -= 1
        print(f"Too high.\nGuess again\nYou have {num_of_tries} remaining to guess the number.")

def start():
    print("Welcome to the Number Guessing Game!\nI'm Thinking of a number between 1 and 100.")

    choose_level()

def main():
    if __name__ == "__main__":
        start()
main()