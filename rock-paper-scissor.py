import random

emojis = {
    "r" : "🪨",
    "s" : "✂️",
    "p" : "📃"
}
choices = ("r", "p", "s")
while True:
    computer_choice = random.choice(choices)
    player_choice = input("what is your choice? (r/s/p): ").lower()
    if player_choice not in choices:
        print("try again!")
        continue
    print(f"you choose {emojis[player_choice]}")
    print(f"computer chose {emojis[computer_choice]}")
    if player_choice == computer_choice:
        print("match draw!")
    elif(
         computer_choice == "r" and player_choice == "p" or
         computer_choice == "p" and player_choice == "s" or
         computer_choice == "s" and player_choice == "r"
    ):
     print("you win!")
    else:
            print("you lose!")
    user_more = input("want to play again?(y/n) ").lower()
    if user_more == "y":
        break




# elif(
#     computer_choice == "s" and computer_choice == "r" or
#     computer_choice == "p" and computer_choice == "s" or
#     computer_choice == "r" and computer_choice == "p"
# ):
#     print("you win!")
# else:
#     print("you lose!")
# user_more = input("want to play again?(y/n) ").lower()
#     if user_more == "y":
#         break