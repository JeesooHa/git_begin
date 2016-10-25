import random



"""

========

Rock scissors paper games

========



play rock scissors paper games 10 times and terminate.

"""

play = True

i = 0

while play :



    #player_choice

    player = input("Enter your choice (rock/paper/scissors): ")

    player = player.lower()

    while (player != "rock" and player != "paper" and player != "scissors"):

        player = input("Enter your choice (rock/paper/scissors): ")

        player = player.lower()



    #computer_random

    computer = random.randint(1,3)  #random number generate

    if (computer == 1):     #case of computer

        computer = "rock"

    elif (computer == 2):

        computer = "paper"

    elif (computer == 3):

        computer = "scissors"

    else:

        print ("Error. Enter your choice from rock, paper, scissors.")



    #result

    if (player == computer):    #case of result

        print ("Draw!")

    elif (player == "rock"):

        if (computer == "paper"):

            print ("You won.");

        if (computer == "scissors"):

            print ("You lost.");

    elif (player == "paper"):

        if (computer == "rock"):

            print ("You won.");

        if (computer == "scissors"):

            print ("You lost.");

    elif (player == "scissors"):

        if (computer == "rock"):

            print ("You lost.");

        if (computer == "paper"):

            print ("You won.");

    i = i + 1


    #define end condition

    if (i >= 10):

        play = False

        print ("See you again.")

    else:

        play = True
