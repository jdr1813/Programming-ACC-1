"""

"At one college, the tuition for a full-time student is $8,000 per semester.  It has
been announced that the tuition cost per semester will increase by 3 percent each year for the next 5 years."

This program will calculate the projected semester tuition cost per semester for the next 5 years. 

Name: Justin Rivas
Date: 7/12/2021 
Version: 1.0.3
"""

# tuition increases 3% per year
TUITION_INCREASE = .03

# this program runs for 5 years set year to 1 and loop 5 times.
year = 1

# starting tuition at $8000
starting_tuition = 8_000

#set total = to 0 so I can keep assigning it a new value
total = 0

print(f"The tuition starting cost is ${starting_tuition:.2f} and will raise 3% each year for the next 5 years.\n")

while year < 6:
    # Get the original total increase 
    total = starting_tuition * TUITION_INCREASE

    # create new current_tuition variable and store the sum of "starting_tuition" and the current total.
    current_tuition = starting_tuition + total

    # set starting tuition to the current tuition price for the next loop
    starting_tuition = current_tuition

    #print the total per year 
    print(f"The total for year {year + 1} is: ${starting_tuition:.2f}")
    
    #increment year by 1 so we have a way to break out of the loop
    year += 1
