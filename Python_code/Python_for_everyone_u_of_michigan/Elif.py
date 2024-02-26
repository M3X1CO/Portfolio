print('1 : Rock 2 : Paper : Scissors')
player1 = int(input('Player #1: '))
player2 = int(input('Player #2: '))
if player1 == 1 and player2 ==1:
    print('Tie')
elif player1 == 1 and player2 ==2:
    print('Player 2 Wins')
elif player1 == 1 and player2 == 3:
    print('Player 1 Wins')

elif player1 == 2 and player2 ==1:
    print('Player 1 Wins')
elif player1 == 2 and player2 ==2:
    print('Tie')
elif player1 == 2 and player2 ==3:
    print('Player 2 Wins')

elif player1 == 3 and player2 ==1:
    print('Player 2 Wins')
elif player1 == 3 and player2 == 2:
    print('Player 1 Wins')
elif player1 == 3 and player2 ==3:
    print('Tie')
else:
    print('Incorrect Input Noob')
