"""
This program will ask the user for a file name and read the numbers from the file and then calculate the average of all the numbers stored in the file. 

Name: Justin Rivas
Date: 7/27/2021
Version: 1.0.0
"""


def main():
    file = file_open()
    avg, total, count = calculate_average(file)


    # provide the user with the total number of numbers in the file, the sum and the avg of all the numbers. 
    print(f"This file had a total of {count} numbers.")
    print(f"The sum of all numbers in the file is {total}")
    print(f"The average of the numbers in the file is {avg}")


def file_open():
    # user input so they can choose the file to be read
    file_name = input("Please enter a filename to be read: ")
    try: 
        # open the file and read the contents
        file = open(file_name, "r")

        # if filename incorrect give this error. 
    except IOError:
        print("Trouble opening file. Try again.")
        exit()
    
    return file

def calculate_average(file):

    total = 0
    count = 0

    # iterating through the file and grabbing the numbers in the file
    for line in file:
        try: 
            # adding each number in the file to total so I can get the sum
            total += int(line)
            # incrementing count to keep track of how many numbers are in the file 
            count += 1

            # if the file contains a character that's not an int you'll get this error. 
        except ValueError:
            print(f"File must have only numbers. Try again.")
            exit()
    
    # calculating the average of the numbers in the file 
    avg = total / count

    # returning all 3 values to show the user.
    return avg, total, count

main()
