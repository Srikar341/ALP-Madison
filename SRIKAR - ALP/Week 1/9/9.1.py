# Example Code 1

def say_hi():
  print("Why hello there!")
#it is making a subroutine so that whenver you call it by saying say_hi, it will give the output
def offer_drink():
  print("Would you care for a spot of tea?")
#same thing excpet the call will be offer_drink and the output would be would you care for a spot of tea?
def offer_food():
  print("Biscuit?")
# same thing except the call will be offer_food and the output wil be Biscuit?
def say_bye():
  print("Cheerio then.")
# same thing except the call will be say_bye and the output will be Cheerio then.

offer_drink()#this is callling for the subroutine so the output will be would you care for a spot of tea?
say_hi() #this is calling for why hello there!
offer_food() #this is calling for Biscuit?

# Example code 2
def maths1():# This is substituing for num1 and num2 below and the return
  num1 = 50
  num2 = 5
  return num1 + num2

def maths2():#same thing except the return in a substraction equation
  num1 = 50
  num2 = 5
  return num1 - num2

def maths3():#same thing except the return is a multiplication equation
  num1 = 50
  num2 = 5
  return num1 * num2

outputNum = maths2()#OutputNum is a variable for maths2, not another subroutine because it doesnt have a def or an underscore as a space
print(outputNum)#this will do the second return equation with is 50-5 = 45

# Example Code 3
def location(country):#This subroutine will say I am from and give you an input for the country
  print("I am from " + country)


location("Brazil")#It will say I am from Brazil

