
print("Rules of game ROCK PAPER SCISSORS--Rock beats scissors--Scissors beats paper--Paper beats rock")

again = 'yes'

while (again == 'yes'):
    
    player1 = input("Player 1 Enter, Rock, Paper, Scissors " )
    player1 = player1.lower()
    
    print()
    
    player2 = input("Player 2 enter, Rock, Paper, Scissors? ")
    player2 = player2.lower()
    
    print()
    
    if (player1 == "rock"):
        if (player2 == "rock"):
            print("This game is a draw")
        elif (player2 == "paper"):
            print("Congratulations player 2 wins ")
        elif (player2 == "scissors"):
            print("Congratulations player 1 wins ")
    elif (player1 == "paper"):
        if (player2 == "rock"):
            print("Congratulations player 1 wins ")
        elif (player2 == "paper"):
            print("This game is a draw")
        elif (player2 == "scissors"):
            print("Congratulations player 2 wins ")
        elif (player1 == "scissors"):
            if (player2 == "rock"):
                print("Congratulations player 2 wins ")
        elif (player2 == "paper"):
            print("Congratulations player 1 wins ")
        elif (player2 == "scissors"):
            print("This game is a draw")
    else:
        print("Invalid input, try again")

again = input("Type yes to play again, or, anything else to stop: ")

print()
