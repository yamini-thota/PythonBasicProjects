import random
first_number=random.randint(1,6)
second_number=random.randint(1,6)
playing_dice=True

while playing_dice:
    dice_Number=(input("Roll the dice..?(Y/N): ")).lower()
    if dice_Number=='y':
        print(f'({first_number},{second_number})')
    elif dice_Number=='n':
        print(f'Thanks for Playing...!')
        print("Have a nice day...!")
        break
    else:
        print('Invalid Input...!')
