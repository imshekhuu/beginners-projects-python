import random

robo = random.choice([1.-1,0])
you = input("enter your choice: ")
you_dic = {"s" : 1, "w" : -1, "g" : 0}
revers_dic = {  1:"snake" , -1 : "water" , 0 : "gun" }
alpha = you_dic[you]
print(f"your choice is {revers_dic[alpha]}\ncomputer choice is {revers_dic[robo]}")

if alpha == robo:
    print("match draw!!")

else:
    if robo == -1 and alpha == 1:
        print("you won!")
    elif robo == -1 and alpha == 0 :
        print("you lose!")
    elif robo == 1 and alpha == 0:
        print("you won!")
    elif robo == 1 and alpha == -1:
        print("you win")
    elif robo == 0 and alpha == 1:
        print("you lose")
    elif robo == 0 and alpha == -1:
        print("you win")
    else:
        print("something went wrong!!")