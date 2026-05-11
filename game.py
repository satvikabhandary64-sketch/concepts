'''player1=input("Player 1,Enter rock, paper or scisssors: ").lower()
player2=input("Player 2,Enter rock, paper or scisssors: ").lower()
if (player1=="rock" and player2=="scissors")or (player2=="rock" and player1=="scissors" ):
    print("The winner is rock")
elif (player1=="scissors" and player2=="paper")or (player2=="scissors" and player1=="paper" ):
    print("The winner is paper")
elif (player1=="paper" and player2=="rock")or (player2=="paper" and player1=="rock" ):
    print("The winner is rock")
elif (player1=="rock" and player2=="rock")or (player1=="scissors" and player2=="scissors") or (player1=="paper" and player2=="paper"):
    print("Draw")
else:
    print("Invalid input")'''

player1=input("Player 1,Enter rock, paper or scisssors: ").lower()
player2=input("Player 2,Enter rock, paper or scisssors: ").lower()
if (player1=="rock" and player2=="scissors")or (player1=="scissors" and player2=="paper") or (player1=="paper" and player2=="rock"):
    print("The winner is player 1")
elif (player2=="rock" and player1=="scissors" ) or (player2=="scissors" and player1=="paper") or (player2=="paper" and player1=="rock" ):
    print("The winner is player 2")
elif player1==player2:
    print("Draw")
else:
    print("Invalid input")


import random
computer_choice=random.choice(['rock','paper','scissors'])
player=input("Player: Enter rock, paper or scisssors: ").lower()
action_list=['rock','paper','scissors']
if player in action_list:
    if player==computer_choice:
        print("It is a tie")
    elif (player=='rock' and computer_choice=='scissors') or (player=='scissors' and computer_choice=='paper') or (player=='paper' and computer_choice=='rock'):
        print("Player wins")
    elif (computer_choice=='rock' and player=='scissors') or (computer_choice=='scissors' and player=='paper') or (computer_choice=='paper' and player=='rock'):
        print("Computer wins", computer_choice)
    else:
        print("Invalid input")
else:
    print("player not in action list")