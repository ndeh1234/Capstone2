import random       #Import random module
min = 1             #Set minimum value of dice
max = 6              #Set Maximum value of dice

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":   #While loop gives user opportunity to roll again
  print ('Rolling the dice...')                  # Dice is being rolled
  print ('the values are....')                     # And the values are displayed
  print (random.randint(min, max))
  print (random.randint(min, max))

  roll_again = input("Roll the dice again?")      #Prompt user to roll again