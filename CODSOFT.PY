import random

users_scores = 0
computers_scores = 0

def playing_again():
    play = input("Do you want to play again? (Y/N): ")
    if play.upper() == 'Y':
        game()
    else:
        print("Thanks for playing!")
        exit()

def game():
    global users_scores, computers_scores

    users_choices = input("Choose rock, paper, or scissors: ")
    computers_choices = random.choice(['rock', 'paper', 'scissors'])

    print("You choose:", users_choices)
    print("Computer choose:", computers_choices)

    if users_choices == computers_choices:
        print("It's a tie!")
    elif (users_choices == 'rock' and computers_choices == 'scissors') or (users_choices == 'scissors' and computers_choices == 'paper') or (users_choices == 'paper' and computers_choices == 'rock'):
        print("You win!")
        users_scores += 1
    else:
        print("Computer wins!")
        computers_scores += 1

    print("CurrentScore: User:", users_scores, "Computer:", computers_scores)

    playing_again()

game()