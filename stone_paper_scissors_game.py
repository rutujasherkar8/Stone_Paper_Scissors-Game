
#Stone,Paper,Scissors Game
#Developer Name:-Rutuja Dnyaneshwar Sherakar
#Date:- 09 September 2022

import random
import sys

stone = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

l = [stone,paper,scissors]

while True:
    print("-----------------------------------------------------------------------------")
    print("***************WELCOME!!! Rock, Paper, Scissors Game*************************")
    user = int(input("Press 0 for Rock, 1 for Paper, 2 for Scissors...Press -1 for Exit : "))

    if user < 0 or user > 2:
        print("Invalid Input")
        sys.exit()

    computer = random.randint(0,2)
    
    print("User Input = ")
    print(l[user])
    print("Computer Input = ")
    print(l[computer])


    if user == computer:
        print("Both select same choice...Match Draw...")

    elif user == 0 and computer == 2:
        print("Hey, You Won")

    elif user == 0 and computer == 1:
        print("You Lose")

    elif user == 1 and computer == 0:
        print("Hey, You Won")

    elif user == 1 and computer == 2:
        print("You Lose")

    elif user == 2 and computer == 0:
        print("You Lose")

    elif user == 2 and computer == 1:
        print("Hey, You Won")
        
    elif user == -1:
        break
        
    
            
         
            
            
    
