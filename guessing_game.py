"""
Project 1 - Number Guessing Game
--------------------------------

For this first project you can use Workspaces. 

NOTE: If you prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
import statistics

   
def start_game():
  
  
  attemptNumber = [] 
  
  while True:
    print("**** Welcome to Guess THAT Number Game ****")
    secretNumber =  random.randrange(0, 100)
    guessedNumber = int(input("Please, guess a number between 1 to 100 -> "))
    attempts = 1
    while guessedNumber != secretNumber:
              if guessedNumber > secretNumber:
                attempts +=1
                print ("It's lower. Try again!")
                guessedNumber = int(input("Please, guess another number: "))
              
              elif guessedNumber < secretNumber: 
                attempts +=1
                print ("It's higher. Try again!")
                guessedNumber = int(input("Please, guess another number: "))
              
    else:
        print("***** You Got it! ******")
        print("It took you " + str(attempts) + " attempts to get the correct number" )
        attemptNumber.append(attempts)
        print ("*** Overall Statistics ***" )
        print (f"MEAN: {str(statistics.mean(attemptNumber))}" )
        print(f"MEDIAN: {str(statistics.median(attemptNumber))}" )
        print(f"MODE: {str(statistics.mode(attemptNumber))}" )

        restart = input("Would like to play again? [Y/N] ? ")
    if restart != "N":
       continue

    else:
      print("Thanks for playing" )
      exit()

        
start_game()

