import random
import time

rock = 1
paper = 2
scissors = 3
spock = 4
lizard = 5

names = {rock: "Rock", paper: "Paper", scissors: "Scissors", spock: "Spock", lizard: "Lizard"}
rules = {rock: scissors, paper: rock, scissors: paper, spock: rock, lizard: spock}

player_score=0
computer_score=0

def start():
    print("Lest's play a game of Rock, Paper,LizardScissors,Spock")
    while game():
        pass
    scores()

def game():
    player = move()
    computer= random.randint(1,2)
    result(player, computer)
    return play_again()

def move():
    while True:
        print("")
        player=input("Rock= 1\nPaper =2\nScissors = 3\nSpock =4\nLizard =5\nMake a move")
        try:
            player=int(player)
            if player in(1,2,3,4,5):5
                return player
        except ValueError:
            print(" Opps,I did not understand that please enter 1,2,3")

def result(player, computer):
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3...")
    time.sleep(0.5)
    print("Computer throw {0}".format(names[computer]))
    global player_score, computer_score
    if player == computer:
        print("Tie!")
    else:
        if rules[player]==computer:
            print("Victory Assured!")
            player_score +=1
        else:
            print("The computer laughs at you.\You have been defeated")
            computer_score += 1

def play_again():
    answer= input("Would you like play again Y/N")
    if answer in ("Y","y"):
         return answer
    else:
        print(" Tank you fro playing.Goodbye")

def scores():
    global player_score,computer_score
    print("HIGH SCORES:")
    print("PLAYER:",player_score)
    print("COMPUTER:",computer_score)

if __name__== '__main__':
        start()
