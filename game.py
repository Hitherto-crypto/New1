import random
win =0
while True:
    game_choices=["Rock","Paper","Scissors"]
    guess=input("choice fate:Rock,Paper,Scissors").lower()
    computer_guess=random.choice(game_choices)
    if guess=="Rock":
        if computer_guess=="Rock":
            print("Tie")
        elif computer_guess=="Paper":
            print("you lose, my guess was paper")
        elif computer_guess=="Scissors":
            print("you lose, my guess was Scissors")
    if guess=="Scissors":
        if computer_guess=="paper":
            print("you win, my guess was paper")
        elif computer_guess=="Scissors":
            print("tie")
        elif computer_guess=="Rock":
            print("you lose, my guess was Rock")
    elif guess=="Paper":
        if computer_guess=="Paper":
            print("Tie")
        elif computer_guess=="Scissors":
            print("you lose, my guess was Scissors")
        elif computer_guess=="Rock":
            print("you win")
    elif guess == "exit":
        break
    else:
        print("Invalid Input")