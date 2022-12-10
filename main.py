from random import randint
import os

def take_a_guess(correct_number, number_of_tries):
    if number_of_tries == 0:
        print("⛔ GAME OVER - You've run out of guesses.")
    else:
        user_guess = int(input("Make a guess: "))

        if user_guess == correct_number:
            print(f"👍 You got it! The answer was {correct_number} 👍")
        if user_guess > correct_number:
            number_of_tries -= 1
            print(f"👇 Too high.\nGuess again\nYou have {number_of_tries} remaining to guess the number.")
            take_a_guess(correct_number, number_of_tries)
        elif user_guess < correct_number:
            number_of_tries -= 1
            print(f"☝️ Too low.\nGuess again\nYou have {number_of_tries} remaining to guess the number.")
            take_a_guess(correct_number, number_of_tries)

def game():
    num_of_tries = 0
    rand_num = randint(1,100)

    difficulty_level = (input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()

    if difficulty_level == 'easy':
        num_of_tries = 10
    elif difficulty_level == 'hard':
        num_of_tries = 5
    else:
        print("\nYou have entered an invalid choice!")
        game()

    print(f"\nYou have {num_of_tries} attempts remaining to guess the number.")

    take_a_guess(rand_num, num_of_tries)

def main():
    if __name__ == "__main__":
        os.system('cls')
        print("\n🕵️  Welcome to the Number Guessing Game!\n🔢 I'm Thinking of a number between 1 and 100.")
        game()

main()