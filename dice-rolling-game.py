# dice rolling game
import random
while True:
    dice = input("roll the dice? (y/n): ").lower()
    if dice == "y":
        dic1 = random.randint(1, 6)
        dic2 = random.randint(1, 6)
        print(f"{dic1}, {dic2}")
    elif dice == "n":
        print("thanks for playing!")
        break
    else:
        print("sorry, try again")