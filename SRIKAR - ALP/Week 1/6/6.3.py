# Starter Code

number1 = int(input("Please enter a number"))
number2 = int(input("Please enter another number"))

if number1 > number2:
  print("Number 1 is bigger than number 2")
elif number2 > number1: 
  print("Number 2 is bigger than number 1")
else:
  print("Both numbers are the same")
  
number3 = int(input("Please enter another number"))
if number3 > number1:
  print("Number 3 is bigger than number 1")
if number3 > number2:
  print("Number 3 is bigger than number 2")
elif number1 > number3: 
  print("Number 1 is bigger than number 3")
elif number2 > number3: 
  print("Number 2 is bigger than number 3")
elif number2 == number3:
  print("both numbers 2 and 3 are the same")
elif number1 == number3:
  print("both numbers 1 and 3 are the same")
else:
  print("all numbers are the same")