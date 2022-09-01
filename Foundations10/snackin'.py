# NOTE: The test cases for this section are cumulative.  You need to solve the challenges in order, and as you do, don't comment out the print statements from previous problems, as the test cases build upon themselves. Also note that some questions have multiple parts.

# ---------------------------------------------------------------------- #
'''Q1. Favorite Snack'''

# Declare a variable called favorite_snack and set its value to be the name of your favorite snack.

# NOTE: ALL SNACK NAMES MAY ONLY BE ONE WORD AND MAY ONLY CONSIST OF LETTERS


### YOUR CODE STARTS HERE ###

#string variable
favorite_snack = 'chips'

### YOUR CODE ENDS HERE ###


# Print out the string "My favorite snack is <YOUR_SNACK>;" using the variable favorite_snack that you created.


### YOUR CODE STARTS HERE ###

#print the string defined above
print('My favorite snack is ' + favorite_snack + ';')


### YOUR CODE ENDS HERE ###


# ---------------------------------------------------------------------- #
'''Q2. Eating Chips'''

# Define the variable called a, with the value of the string "I could eat "


### YOUR CODE STARTS HERE ###

#string variable
a = 'I could eat'

### YOUR CODE ENDS HERE ###


# Define the variable called b, and assign it with the integer value 100


### YOUR CODE STARTS HERE ###

#integer variable
b = 100

### YOUR CODE ENDS HERE ###


# Define the variable called c, and assign it with the value of a string that is the name of your favorite snack


### YOUR CODE STARTS HERE ###

# string variable
c = 'chips'

### YOUR CODE ENDS HERE ###


# Concatenate a, b, the literal value ' ' and c together and print the results


### YOUR CODE STARTS HERE ###

#print variable 'a', add ' ', convert 'b' integer to string in order to concatenate, add another ' ', and print 'c' variable
print(a + ' ' + str(b) + ' ' + c)

### YOUR CODE ENDS HERE ###


# ---------------------------------------------------------------------- #
'''Q3. Lots of Snacks'''

# Print out the string "My favorite snack is <YOUR_SNACK>;" 77 times


### YOUR CODE STARTS HERE ###

#same print phrase as Q1 multiplied 77 times
print(('My favorite snack is ' + favorite_snack + ';') * 77)

### YOUR CODE ENDS HERE ###


# ---------------------------------------------------------------------- #
