print('''
.______       __       _______                     _______         ___         .___  ___.     _______ 
|   _  \     |  |     /  _____|                   /  _____|       /   \        |   \/   |    |   ____|
|  |_)  |    |  |    |  |  __                    |  |  __        /  ^  \       |  \  /  |    |  |__   
|   ___/     |  |    |  | |_ |                   |  | |_ |      /  /_\  \      |  |\/|  |    |   __|  
|  |         |  |    |  |__| |                   |  |__| |     /  _____  \     |  |  |  |    |  |____ 
| _|         |__|     \______|                    \______|    /__/     \__\    |__|  |__|    |_______|

\n\n
Welcome to the Pig Adventure Island.
Your mission is to survive by making the correct decisions.

''')

direction = input('You\'re at a crossroad, where do you want to go, "Left" or "Right"? Select L or R.\n').lower()
if direction == "l":
  if input('You\'ve come to a huge lake. There\'s an island in the middle of the lake. Do you want to want to "wait" for a Boat or "swim" across the lake? Select S or W.\n').lower() == "w":
    door = input('You\'ve arrived at the island of mystery. There are three mysterious doors. Which door you want to enter, "Red", "Blue" or "Yellow"? Select R, B or Y.\n').lower()
    if  door == "y":
      print("Well done piggy! You survived the adventure island.\n")
    elif door == "r":
      print("Roasted in Tandoor. Game up Piggy.\n")
    elif door == 'b':
      print("Time to open up the piggy bank. Game up Piggy!\n")
    else:
      print("No such door. You are being sent to a mud pit. I guess you win!")
  else:
    print("Delicious snack for the fish. Game up Piggy!\n")

else:
  print("You are now trapped in the Bear's Honey game. Game up Piggy!\n")
