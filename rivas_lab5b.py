"""
This program will convert Celsius to Fahrenheit and Fahrenheit to Celsius based on user input.

Name: Justin Rivas
Date: 7/26/2021
Version: 1.0.0

"""

# units needed to convert temperatures 
SCALE_DELTA = 32.0
CONVERSION_CELSIUS = 1.80
CONVERSION_FAHRENHEIT = 0.5556


def main():
    print("Welcome to temperature conversion program.\n")
    menu()

    menu_selection = input("Please make a selection from the menu.\t").upper()

# check user input to see what they want to do.
    while menu_selection != 'X':
        if menu_selection == 'C':
            convert_f_to_c()
        elif menu_selection == 'F':
            convert_c_to_f()
        else:
            print("Invalid option.")
        menu()
        menu_selection = input("Please make a selection from the menu.\t").upper()
    print("Goodbye")
    exit()

# function to convert fahrenheit to Celsius 
def convert_f_to_c():
    print("\nYou chose to convert Fahrenheit to Celsius.")
    fahrenheit = float(input("Enter the value you'd like to convert to Celsius."))
    #Calculation from F to C
    celsius = fahrenheit - SCALE_DELTA * CONVERSION_FAHRENHEIT
    print(f"\t{fahrenheit} degrees Fahrenheit is {celsius} degrees Celsius")

#function to convert Celsius to Fahrenheit
def convert_c_to_f():
    print("\nYou chose to convert Celsius to Fahrenheit.")
    celsius = float(input("Enter the value you'd like to convert to Fahrenheit."))
    #calculation from C to F
    fahrenheit = celsius * CONVERSION_CELSIUS + SCALE_DELTA
    print(f"\t{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit")

# menu for user to select what they'd like to do. 
def menu():
    print("\nSelect F to convert from Celsius to Fahrenheit")
    print("\nSelect C to convert from Fahrenheit to Celsius")
    print("\nSelect X to exit the program.")


main()