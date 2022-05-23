import sys
import quick_game
import custom_game
import score

while(True):
    # print user interface
    print("\n Menu\n 1. Quick Game Play \n 2. Custom Game Play \n 3. View Scores \n 4. Help \n 5. Exit")
    
    #get users input
    choice = input("Enter selection: ")
    choice = int(choice) #convert to integer
    
    #call corresponding modules according to user input
    #Quick game
    if(choice == 1):
        quick_game.quickGame()
        
    #custom game
    elif(choice == 2):
        print()
        custom_game.customGame()
        
    #score
    elif(choice == 3):
        score.score()
    
    #help    
    elif(choice == 4):
        print("This game has two options quick game play and custom game play.Qiuck game play will require you to answer five questions on mathematical adding. In the custom game play you are given the option to choose a level you prefer and the number of questions you are willing to answer.  ")
     
    #exit
    elif(choice == 5):
        print("Exiting application...")
        break
        

