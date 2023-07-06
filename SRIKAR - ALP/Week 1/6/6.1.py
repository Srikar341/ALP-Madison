# Example code 1

number = 7
# number is a varaible that is 7 in this code
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))
#It will ask you to guess a number between 1 through 10
if guess == number:
  print("Correct!")
elif guess < number:
  print("Too Low!")
else:
  print("Too High!")
# If the guess is equal to 7, it will say correct. If the guess is less than 7, it will say that it is too low. If the guess is greater 7, it will say Too high
# Example code 2

number1 = int(input("Please enter a number"))
number2 = int(input("Please enter another number"))
#It will ask you to enter 2 numbers in
if number1 > number2:
  print("Number 1 is bigger than number 2")
elif number2 > number1: 
  print("Number 2 is bigger than number 1")
else:
  print("Both numbers are the same")
# If the number you chose first is greater than the second, that it will say number 1 is bigger than number 2. If the second number is greater, than it will say that number 2 is bigger than number 1. If both are the same, than it will say that both numbers are the same
