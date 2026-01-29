import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        attempts += 1

        if guess < number:
            print("📉 Too low!")
        elif guess > number:
            print("📈 Too high!")
        else:
            print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
            break
    else:
        print(f"😢 You've used all attempts. The number was {number}.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        number_guessing_game()
    else:
        print("👋 Thanks for playing!")

# Start the game
number_guessing_game()
