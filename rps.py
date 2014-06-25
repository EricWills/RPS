from starters import choice

def compare(choice1,choice2):
    if choice1 == choice2:
        print("it is a tie!")
    elif choice1 == 'rock':
        if choice2 == 'scissors':
            print("Rock Wins")
        elif choice2 == 'paper':
            print("paper wins")
        elif choice1 == 'paper':
            if choice2 == 'scissors':
                print("scissors wins")
            elif choice2 == 'rock':
                print("paper wins")
        elif choice1 == 'scissors':
            if choice2 == 'paper':
                print("scissors wins")
            elif choice2 == 'rock':
                print("rock wins")
        else:
            print("something wrong")

rounds = int(raw_input("enter number of rounds: "))
player1_name = raw_input("Enter Player 1 name: ")
player2_name = raw_input("Enter Player 2 name: ")
counter = 0
while counter != rounds:
    choice1 = choice()
    choice2 = choice()
    compare(choice1, choice2)
    counter += 1
print("{} and {} thanks for playing".format(player1_name, player2_name))

