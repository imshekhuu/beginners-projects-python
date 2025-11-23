MASTER_PASSWORD = '1234'

def add_password():
    account = input("enter account name: ")
    password = input("enter account password: ")


    with open('passwords.txt', 'a') as file:
        file.write(account + "|" + password + '\n')


    print('Password Saved!')


def view_password():
    try:
        with open("passwords.txt", 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("No Password saved yet.")
                return
            else:
                for line in lines:
                    print(line.strip())

    except FileExistsError:
        print("No Password files is exixtes. Add Password File first")

    
mp = input("Enter Master Password: ")
if mp != MASTER_PASSWORD:
    print("Wrong password! Access denied.")
    exit()

while True:
    choice = input("\nChoose an option:\n[a] Add Password\n[v] View Passwords\n[q] Quit\nYour choice: ").lower()

    if choice == 'a':
        add_password()
    elif choice == 'v':
        view_password()
    elif choice == 'q':
        print("Good Bye!!")
        break
    else:
        print("input not matched. Type correct input")
