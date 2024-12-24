import random

secret_number = random.randint(1, 50)
guess_count = 0
guess_limit = 5

print("🎯 Welcome to the Guessing Game! 🎮")

while guess_count < guess_limit:
    try:
        guess = int(input("🔢 Guess a number between 1 to 50: "))
        guess_count += 1
        if guess == secret_number:
            print(f"🎉 You guessed it in {guess_count} guesses! 🏆")
            break
        elif guess < secret_number:
            print("📉 Too low! Try again. 👇")
        else:
            print("📈 Too high! Try again. 👆")
    except ValueError:
        print("⚠️ Please enter a valid number! 🛑")
else:
    print(f"😞 Sorry, you ran out of guesses. The secret number was {secret_number}. Better luck next time! 🍀")