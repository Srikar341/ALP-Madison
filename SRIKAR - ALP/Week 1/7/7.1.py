# Example code 1

# Add comments to each line to say whehter it is inside or outside the loop and what it does.

# Explain the circumstances in which the loop will run.

print("What is the capital of France?")
answer = input() 
# It will ask you what is the capital of France
while answer != "Paris":
  print("Incorrect! Try again.")
  answer = input("What is the capital of France?")
# If you put anything but Paris, it will say that you are incorrect and try again.
print("Correct!")
# If you do put Paris it will stop the loop and say that you are correct.
# Example code 2

counter = 1
# the counter will be in a loop becayse it is less than 5
while counter < 5:
  print("This code is inside the loop")
  counter += 1
  #after a certain amount of times, the loop will end because the counter will go above 5

number = 3
int(input("guess a number between 1-10"))
while number != 3:
  print("Incorrect, try again")
  int(input("guess a number between 1-10"))
print("correct!")