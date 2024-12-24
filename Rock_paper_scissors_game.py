import random

emojis={'R' : '🤜', 'S' : '✂','P' : '📃'}
choices = ('R', 'P', 'S')

while True:
    user_choice = input("Rock, Paper or Scissors(r,p,s)?: ").upper()
    if user_choice not in choices:
        print("Invalid Choice, Please check the input..!")
        continue

    computer_choice = random.choice(choices)

    print(f"Computer chose:{emojis[computer_choice]}")
    print(f"You chose:{emojis[user_choice]}")

    if user_choice == computer_choice:
        print('Tie..!')
    elif (
        (user_choice == 'R' and computer_choice == 'S') or
        (user_choice == 'S' and computer_choice=='P') or
        (user_choice == 'P' and computer_choice=='R')):
        print('You win..!')
    else:
        print('You lose..!')

    want_to_continue = input("Do you want to play again? (y/n): ").upper()
    if want_to_continue=='n':
        break
    else:
        print('Thank you for playing!')