'''
Author....: Matt Verini
Assignment: HW 03
Date......: 2/12/2020
Program...: Program to play the game Lucky Sevens
'''

'''
In the Lucky Sevens game, a player rolls a pair of dice. If the dots add
up to 7, the player wins $4; otherwise the player loses $1. Suppose that,
to entice the gullible, a casino tells players that there are lots of ways
to win: (1, 6), (2, 5) and so on. A little mathematical analysis reveals
that there are not enough ways to win to make the game worthwhile; however,
because many people's eyes glaze over at the first mention of mathemtics,
your challenge is to write something that demonstrates the futility of
playing the game.
'''

import random


def dice_rolls():
    moneyToPlay = float(input("\nEnter how much money ($) you would like to put in the pot: "))
    MAX_ROLLS = 0
    keepPlaying = str(input("\nWould you like to roll the dice? (y/n): "))
    if keepPlaying == 'y':
        while moneyToPlay > 0 and MAX_ROLLS < 7:
            MAX_ROLLS += 1
            if MAX_ROLLS == 7:
                print("\nYou are out of rolls.")
            else:
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                if dice1 + dice2 == 7:
                    moneyToPlay += 4
                    print("\nYou have ($)", moneyToPlay)
                    keepPlaying = str(input("\nWould you like to keep roll again? (y/n): "))
                    if keepPlaying == 'y':
                        continue
                    elif keepPlaying == 'n':
                        print("\nCome on try again! There are 4 ways to win!")
                        continue
                    else:
                        print("Please try entering a y or a n.")
                        continue
                else:
                    moneyToPlay -= 1
                    print("\nYou have ($)", moneyToPlay)
                    keepPlaying = str(input("\nWould you like to keep roll again? (y/n): "))
                    if keepPlaying == 'y':
                        continue
                    elif keepPlaying == 'n':
                        print("\nCome on try again! There are 4 ways to win!")
                        continue
                    else:
                        print("Please try entering a y or a n.")
                        continue
                break
    elif keepPlaying == 'n':
        print("\nCome on try again! There are 4 ways to win!")
        
                    
dice_rolls()

    

    

