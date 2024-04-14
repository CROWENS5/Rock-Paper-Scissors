import random as r
# want to get it so the numbers are linked to rock paper scissors 
user = input("What are you going to choose:")
print("User chooses: " + user)
# 1 = "Rock"
# 2 = "Paper"
# 3 = "Scissor"


AIoptions = {

    1:'Rock',
    2:'Paper',
    3:'Scissors'

}


AIoptions1 = ["Rock","Paper","Scissors"]
if AIoptions1 != " ":
    choiceByComputer = r.choice(AIoptions1)
    print("AI choices: " + choiceByComputer)


if user == choiceByComputer:
    print("Its a tie")
elif user == "Rock" or "rock" and choiceByComputer == "Paper":
    print("Paper beats Rock -  Computer wins")
elif user == "Rock" or "rock" and choiceByComputer == "Scissors":
    print("Rock beats scissors - User Wins")
elif user == "Paper" or "paper" and choiceByComputer == "Rock":
    print("Paper Beats Rock - User Wins")
elif user == "Paper" or "paper" and choiceByComputer == "Scissors":
    print("Scissors beats Paper - Computers Wins")
elif user == "Scissors" or "scissors" and choiceByComputer == "Paper":
    print("Scissors beats Paper User Wins")
elif user == "Scissors" or "scissors" and choiceByComputer == "Rock":
    print("Rock beats Scissors Computer Wins")
