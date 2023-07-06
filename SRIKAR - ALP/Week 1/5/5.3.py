# Starter Code

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))
# The output will be asking you to guess a number between 1-10

if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")
  # if you are above 5 it will say Too High and if you are below 5 it  will say too low