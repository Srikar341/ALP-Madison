# Program to calculate the area of a rectangle

# Get input for height & width. Convert to integers and store in variables

# Calculate the area & store the result in the area variable

# Output the area variable (converted to string)

height = int(input("enter the height of a rectangle "))
width = int(input("enter the width of a rectangle "))
area = height * width
print(str(height) , " times " , (width))
perimeter = (2 * height) + (2 * width)
print(str(height) , " plus " , (width))
price = int(input("enter a price "))
RestaurantTipCalculator = (float(0.2) * price)
print(str(0.2) , " times " , (price))
PriceTotal = price + RestaurantTipCalculator
print(str(price) , " plus " , RestaurantTipCalculator)
Base = int(input("enter the base of a rectanglular prism " ))
Height = int(input("enter the height of a rectanglular prism " ))
Width = int(input("enter the width of a rectanglular prism " ))
Volume = height * Width * Base
print(str(height) , " times " , (Base) , " times " , (Width))
Bases = 6
SurfaceArea = Bases * area
print(str(Bases) , " times " , (area))



'''
Extra Challenges
Perimeter Calc
Create a program that allows the user to enter 2 numbers representing the width and length of a rectangle. The program calculates and displays the perimeter of the rectangle. 
Restaurant Tip Calculator 
Create a program that allows the user to enter the price of a meal at a restaurant. The program calculates the amount of the tip to be paid at 20%. The tip and total price are then displayed separately.
Volume and Surface Calc 
Create a program that allows the user to enter 3 numbers representing the height, width and length of a cuboid. The program calculates and displays the volume and total surface area of the cuboid. 
'''



