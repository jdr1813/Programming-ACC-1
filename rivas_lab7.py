"""
This program will allow the user to enter the name of an MLB baseball team and display the number of times the team has won the World Series in the years from 1903 through 2009. 

Name: Justin Rivas
Date: 7/27/2021
Version: 1.0.0
"""


def main():
    try: 
        # open the file and read the contents
        file = open('WorldSeriesWinners.txt', 'r')

        # if filename incorrect give this error. 
    except IOError as error:
        print(f"Trouble opening file. Try again.{error}")
        exit()

    # create a list called champions and store the teams in the list.
    champions = file.readlines() 
    
    
    try:
        # iterate over the list and strip the white space off the end of the name. Convert the names to title case as well.
        for champs in range(len(champions)):
            champions[champs] = champions[champs].rstrip('\n').title()

    except IndexError:
        print("There was an index error.")
    
    # ask the user to input a team they want to check 
    user_input = input("Enter the name of a team.").title()


    try:
        win_count = 0
        
        # check if user input is in the list champions, if it is count how many times they've won the World Series. 
        if user_input in champions:
            for team in champions:
                if team == user_input:
                    win_count += 1
            print(f"The {user_input.title()} have won the World Series {win_count} times between 1903 and 2009.")
        else:
            print(f"The {user_input.title()} have not won a World Series between 1903 and 2009....sorry")

    except:
        print("Something went wrong.")

main()
