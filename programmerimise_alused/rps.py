from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors ")
    player = player.capitalize()
    #Viik
    if player == computer:
        print ("Tie")
    #Kivi
    elif player == "Rock":
        if computer == "Paper":
            print ("You lose!", computer, "covers", player)
        else:
            print ("You win!", player, "smashes", computer)
    #Paber
    elif player == "Paper":
        if computer == "Scissors":
            print ("You lose!", computer, "cut", player)
        else:
            print ("You win!", player, "covers", computer)
    #Käärid
    elif player == "Scissors":
        if computer == "Paper":
            print ("You lose!", computer, "covers", player)
        else:
            print ("You win!", player, "cut", computer)
    else:
        print ("Bad spelling!")
    #Loop
    else:
        player1 = input("Try again? (Y/N) ")
        player1 = player.capitalize()
            if player1 == "Y":
                player = False
                computer = t[randint(0,2)]
            elif player1 == "N":
                exit()