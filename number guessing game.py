import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    lower_bound = 1
    upper_bound = 100
    max_attempts = 7
    play_again = 'y'

    while play_again.lower() == 'y':
        secret_number = random.randint(lower_bound, upper_bound)
        attempts = 0

        print(f"\nI'm thinking of a number between {lower_bound} and {upper_bound}.")
        print(f"You have {max_attempts} attempts to guess it.")

        while attempts < max_attempts:
            try:
                guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess: "))
                attempts += 1

                if guess < lower_bound or guess > upper_bound:
                    print(f"Please enter a number between {lower_bound} and {upper_bound}.")
                elif guess < secret_number:
                    print("📉 Too low!")
                elif guess > secret_number:
                    print("📈 Too high!")
                else:
                    print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
                    break
            except ValueError:
                print("❌ Invalid input. Please enter a number.")

        else:
            print(f"\n😢 Out of attempts! The number was {secret_number}.")

        play_again = input("\nDo you want to play again? (y/n): ")

    print("\n👋 Thanks for playing the Number Guessing Game!")

if __name__ == "__main__":
    number_guessing_game()
