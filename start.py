print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride")
  age = int(input("What's your age?"))
  if age < 12:
    ticket = 5
  elif age<= 18:
    ticket = 7
  elif age >= 45 and age < 55:
      ticket = 0
  else:
    ticket = 12
  photo = input("Do you want a photo? Select Y or N.")
  if photo == "Y":
    ticket += 3
  print(f"Please pay ${ticket}.")
else:
  print("You can't ride")