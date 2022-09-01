# NOTE: The test cases for this section are cumulative.  You need to solve the challenges in order, and as you do, don't comment out the print statements from previous problems, as the test cases build upon themselves. Also note that some questions have multiple parts

# ---------------------------------------------------------------------- #
'''Q1. Set the Season'''

# Declare a variable called season and assign its value to be "spring"


### YOUR CODE STARTS HERE ###

#variable season assigned value of 'spring'
season = 'spring'

### YOUR CODE ENDS HERE ###


# ---------------------------------------------------------------------- #
'''Q2. Dance!'''

# Declare another variable (named whatever you'd like!) and set its value to be the season variable plus the string "fling".


### YOUR CODE STARTS HERE ###

#concatenate the season variable with 'string' to form the party variable
party = season + ' ' + 'fling'

### YOUR CODE ENDS HERE ###


# Print out the concatenation of the season variable and your newly created variable holding the string "fling". Add a space for readability.


### YOUR CODE STARTS HERE ###

#I added the space in the variable definition and printed
print(party)

print('\n')
### YOUR CODE ENDS HERE ###


# ---------------------------------------------------------------------- #
'''Q3. Season of Change?'''

# Print out the original season value, Before you run your code, predict whether season has changed or not? Were you right?


### YOUR CODE STARTS HERE ###

#I don't think it will change the old variable by declaring a new one that just *uses* it
print(season)

print('\n')

### YOUR CODE ENDS HERE ###


# ---------------------------------------------------------------------- #
'''Q4. Change of Season'''

# Assign a variable called temp to be equal to the current value of season.


### YOUR CODE STARTS HERE ###

temp = season

### YOUR CODE ENDS HERE ###


# Change the value of the variable season to "summer"


### YOUR CODE STARTS HERE ###

season = 'summer'

### YOUR CODE ENDS HERE ###


# Predict what will happen to temp. Print out the value of temp. Were you right?


### YOUR CODE STARTS HERE ###

#temp will change because its reading in line order
print(temp)

print('\n')

### YOUR CODE ENDS HERE ###


# ---------------------------------------------------------------------- #
'''Q5. See the Seasons'''

# Use print with concatenation to see the values of both temp and season side by side. Add a space between them for readability.


### YOUR CODE STARTS HERE ###

#print both variables with a ' ' in between to add space
print(temp + ' ' + season)

### YOUR CODE ENDS HERE ###


# ---------------------------------------------------------------------- #
