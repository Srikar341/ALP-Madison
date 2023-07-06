'''
In the modify tasks, you are given some starter code. Use the instructions below to make changes to the code. Comment your changes to explain what you have done.

Run the program to see how it works.
Adapt the code to:

1. Get user input into the number variable.
2. Change the print statement so it outputs 'number' multiplied by 'counter' equals 'product'
3. Make the counter increase by 2 every loop
4. Add a line once the loop has finished to output 'The loop has finished' '''

number = int(input("guess a number "))
counter = 1
product = number * counter
while counter <= 13:
  print(number , "times" , counter , "equals" , product)
  counter = counter + 2
  product = number * counter
  counter >= 13
print("the loop has ended")


number = 7
counter = 1
product = number * counter
while counter <= 12:
  print(number , "times" , counter , "equals" , product)
  counter = counter + 1
  product = number * counter
  counter > 12
print("the loop has ended")

number = int(input("pick a number "))
number2 = int(input("pick another number "))
counter = 1
product = number * counter
while counter <= number2:
  print(number , "times" , counter , "equals" , product)
  counter = counter + 1
  product = number * counter
  counter > number2
print("the loop has ended")