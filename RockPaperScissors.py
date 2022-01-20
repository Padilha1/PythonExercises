import random

user_wins = 0
pc_wins = 0
options = ["rock", "paper", "scissor"]
#                   0            1             2

while True:
    user_input = input ("Type Rock/Paper/Scissor or  Q to quit. ").lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
            continue

    random_number = random.randint(0,2)
    # rock - 0 , paper: 1, scisssor: 2
    pc_pick = options[random_number]
    print("PC picked ", pc_pick + '.')

    if user_input == "rock" and pc_pick == "scissor":
        print("You won")
        user_wins += 1
    elif user_input == "paper" and pc_pick == "rock":
        print("You won")
        user_wins += 1
    elif user_input == "scissor" and pc_pick == "paper":
        print("You won")
        user_wins += 1
    # elif user_input == str(pc_pick):
    #     print("You DRAW, point for both")
    #     pc_wins += 1
    #     user_wins += 1
    else:
        print ("You LOST, LOSER")
        pc_wins += 1

print("You won ", user_wins, "times")
print("Computer won ", pc_wins, "times")
print('Goodbye!')
