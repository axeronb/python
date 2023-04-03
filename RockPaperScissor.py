import random

def get_choices():
    player_choice=input("Enter a Choice \"Rock, Paper, Scissor\"")
    options= ["Rock","Paper","Scissor"]
    computer_choice=random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player,computer):
    print("You Chose "+ player+", & Computer Chose " + computer)
    
    if player==computer:
        return "It's a tie"
    elif player=="Rock":
        if computer=="Scissor":
            return "Player Wins Rock smashes Scissor"
        else:
            return "Paper cover rocks you lose"
    elif player=="Paper":
        if computer=="Scissor":
            return "Player lose Scissor Cuts paper"
        else:
            return "Paper cover rocks you win"
    elif player=="Scissor":
        if computer=="Rock":
            return "Player looses Rock smashes scissor"
        else:
            return "Player wins scissor cuts paper"

choices= get_choices()
result=check_win(choices["player"],choices["computer"])
print(result)

        

   
    
    
    
    
    
    
    
