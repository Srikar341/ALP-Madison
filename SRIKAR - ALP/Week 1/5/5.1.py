# Example code 1

age = 18 
 
if age > 18: 
 print("You are old enough to drive") 
# The output will ask true or false if age is above 18 and if that is true, than it will say you are old enough to drive
# Example code 2

num1 = 1337 
 
if num1 == 10: 
  print("This text is output because the condition was true") 
else:
  print("This text is output because the condition was false") 
# The output will say that the condition was false because num1 was not equal to 10
# Example code 3

number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")
# It will ask you to guess a number from 1-10 and it will give Too High if you are above 5, Too Low is you are below 5, and Correct! is you pick 5