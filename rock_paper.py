import random
emojis = {
    "s" : "✂️",
    "p" : "📃",
    "r" : "🪨"
}
choice = ("r","p","s")
while True:
    name = input("enter your name: ").capitalize()
    play = input("if you want to challange the computer press(y/n): ").lower()
    if play == "y":
        computer_choice = random.choice(choice)
        user_choice = input("it your turn choice(r/p/s): ").lower()
        if user_choice not in choice:
         print("something want wrong!!")
         continue
        print(f"computer choice is {user_choice}")
        print(f"your choice {user_choice}")
        if computer_choice == user_choice:
             print("😒match draw!!")
        elif(
            computer_choice == "r" and user_choice == "p" or
            computer_choice == "p" and user_choice == "s" or
            computer_choice == "s" and user_choice == "r" 
        ):
            print(f"🤩you won {name.capitalize()}!!")
        else:
            print(f"😭you loss {name.capitalize()}!!")
    else:
        print(f"chal chutiye {name.capitalize()}")


