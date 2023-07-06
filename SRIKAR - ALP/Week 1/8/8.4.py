'''
Reference Link
https://docs.google.com/document/d/1Lf221krWqB0vv5zSaQDvzBi6you6AuKdfn5x1TETh7Q/edit?usp=sharing
'''
'''
## Task Instructions - Beat The Zombie

This task requires you to combine lots of skills from earlier lessons. Don't be afraid to look at your old code, google ideas and have fun with the dialogue.  Good luck!

Write a program that simulates an encounter with a zombie in an RPG

1- Create a list of possible weapons.
2- In a variable called ‘zombieWeakness’ store the name of one of the weapons from the list.
3- Output messages telling the user that they have encountered a zombie and should prepare to fight.
4- Output the list of weapons to the user.  Ask if they want to type 1 to use one from the list or 2 to pick their own.  
  4.1- If they type 1 then they should input the weapon name - store it to a new variable. 
  4.2- If they type 2 they should input the weapon name - add it to the list and save it to a new variable.
5- If the weapon picked matches the zombieWeakness, output a message telling the user that they have won the fight.  
  5.1- Otherwise output a message saying that they have lost.

'''

Weapons = ["1. Sword" , "2. Gun" , "3. Poison" , "4. Bow and Arrow"]
zombieWeakness = Weapons[2]
print("1. Pick our from our weapons")
print("2. Pick your own weapon")
choice =int(input("Which Option will you choose? "))
if choice != 1:
  if choice != 2:
        print("You don't have a weapon to fight with!")
if choice == 2:
  Choose = input("Type your own weapon ")
  Weapons.append(Choose)
  if Choose == ("Sword"):
    print("you won")
  if Choose == ("Gun"):
    print("you won")
  while Choose != ("Sword"):
    while Choose != ("Gun"):
     print("you lost. Try Again")
Choose = input("Type your own weapon ")
Weapons.append(Choose)
if Choose == ("Sword"):
    print("you won")
if Choose == ("Gun"):
    print("you won")
while choice == 1:
   print(Weapons)
if choice == 1:
  number = int(input("Choose a number between one of the weapons "))
  if number == 1:
    print("You won")
  if number == 2:
    print("You won")
  if number == 3:
    print("You lost")
  if number == 4:
    print("You lost")
Weapon = input()


