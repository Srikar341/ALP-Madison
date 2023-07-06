number = 7
print("I'm thinking of a number, can you guess it?")
guess = int(input())
while guess != number:
  print("Wrong! Guess again!")
  guess = input()
print("You guessed it!")

# Give the line number where iteration starts.
  # Answer 3

# What does '!=' mean?
  # Answer not equal to

# How many variables are there in the code?
  # Answer 2

# How can you tell which lines of code are inside the loop?
  # Answer Lines that make the statment in line 4 true are inside the loop, line 7 isn't because the answer is correct and line 4 says that it is supposed to be wrong

# How many times will the loop repeat?
  # Answer Until the person gets the right number

# What has to happen to make the program run the last line of code? 
  # Answer If the person gets the answer right

number = 3
guess = int(input("guess a number between 1-10 "))
while guess != 3:
  print("Incorrect, try again")
  guess = input()
print("correct!")