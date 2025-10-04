import random
emojis = {
    "r" : "🪨",
    "p" : "📃",
    "s" : "✂️"
}
choice = ( "s", "p", "r")
while True:
    play = input("sure you want to challage the python languge (y/n): ").lower()
    if play == "y":
        computer = random.choice(choice)
        player_choice = input("enter your choice(r/p/s): ").lower()
        if player_choice not in choice:
            print("something went wrong!!")
            continue
        print(f"your choice is {emojis[player_choice]}")
        print(f"computer choice is {emojis[computer]}")
        if player_choice == computer:
            print("😒match draw!!")
        elif (
            player_choice == "r" and computer == "s" or
            player_choice == "s" and computer == "p" or
            player_choice == "p" and computer == "r"
        ):
            print("😊you won!!")
            break
        else:
            print("😢you loss")
            break
    else:
        print("you are losser!! dont challange python again")
        break


