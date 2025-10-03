import random
computer_choice = random.randint(1,100)
while True:
    try:
        player_choice = int(input("Enter your choice: "))
        if player_choice > computer_choice:
            print("too high!")
        elif player_choice < computer_choice:
            print("too low!")
        else:
            print("you win!")
            break
    except ValueError:
        print("invalid choice!")
