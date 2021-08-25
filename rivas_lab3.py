"""
This is a color mixer program.
You will be able to mix primary colors red, yellow and blue and see the output.

Name: Justin Rivas
Date: 6/18/2021 
Version: 1.0.4

"""
# primary colors the user can choose from 
RED = "red"
BLUE = "blue"
YELLOW = "yellow"

# welcome message 
print("This is a color mixer program.")
print("You will be able to mix primary colors red, yellow and blue and see the output.")

#storing first color input 
color_1 = input("\nPlease enter the first color: red, yellow or blue. ").lower()


# Checking if the input is a valid selection
while color_1 != RED and color_1 != BLUE and color_1 != YELLOW:

    print("You entered an invalid color")
    color_1 = input("\nPlease enter the first color: red, yellow or blue. ").lower()

#sending confirmation that the selection is valid
print(f"You entered {color_1} which is a valid color")

#storing second color input 
color_2 = input("\nPlease enter a second color: red, yellow or blue.")

#checking if second color is valid
while color_2 != RED and color_2 != BLUE and color_2 != YELLOW:

    print("You entered an invalid color")
    color_2 = input("\nPlease enter the second color: red, yellow or blue. ").lower()

#sending confirmation that the selection is valid
print(f"You entered {color_2} which is a valid color")

#storing possible mixtures
red_and_blue = "purple"
red_and_yellow = "orange"
blue_and_yellow = "green"

#checking their first and second inputs and printing the mixture based on their selections. 
if color_1 == RED and color_2 == BLUE or color_1 == BLUE and color_2 == RED:
    print(f"\nThe mixture of {color_1} and {color_2} is {red_and_blue}")
elif color_1 == RED and color_2 == YELLOW or color_1 == YELLOW and color_2 == RED:
    print(f"\nThe mixture of {color_1} and {color_2} is {red_and_yellow}")
elif color_1 == color_2:
    print(f"\nThe mixture of {color_1} and {color_2} is {color_1}")
else:
    print(f"\nThe mixture of {color_1} and {color_2} is {blue_and_yellow}")

