# NOTE: The test cases for this section are cumulative.  You need to solve the challenges in order, and as you do, don't comment out the print statements from previous problems, as the test cases build upon themselves. Also note that some questions have multiple parts.

# ---------------------------------------------------------------------- #
'''Q1. Grocery List'''

# Print 5 things you need from the grocery store, each item should be output on its own line


### YOUR CODE STARTS HERE ###
#create a list with 5 strings
list = ['apples', 'flour', 'coffee', 'milk', 'napkins']
#print out the defined list while separating each string on a new line
print(*list,sep='\n')

#keep it nice and neat, new line
print('\n')

### YOUR CODE ENDS HERE ###


# ---------------------------------------------------------------------- #
'''Q2. Grocery Receipt'''

# Your groceries ring up as 5.63, 13.40, 3.99, 4.57, and 2.47, respectively. Use the 5 items you printed in Q1 and declare variables named after each item. Assign each item with a price listed above.


### YOUR CODE STARTS HERE ###
#variables declared and assigned a value
apples = 5.63
flour = 13.40
coffee = 3.99
milk = 4.57
napkins = 2.47
#print out the value of each variable, separated by new line 
print(apples, flour, coffee, milk, napkins, sep='\n')

### YOUR CODE ENDS HERE ###


# Use python as a calculator to add your variables together and print out the total cost of all the items


### YOUR CODE STARTS HERE ###
#print the sum of the variables while embedding the round() function to limit the output to 2 decimal places
print(round(apples + flour + coffee + milk + napkins, 2))

#keep it nice and neat, new line
print('\n')

### YOUR CODE ENDS HERE ###


# ---------------------------------------------------------------------- #
'''Q3. Buy Lots'''

# Pick your favorite snack from the 5 things you listed in Q1 and save it as a string in a variable called favorite_snack. Use the * operator to print 123 copies of it.


### YOUR CODE STARTS HERE ###

#define my favorite snack
favorite_snack = 'coffee'

#print the new favorite snack variable, concatenate with a space to make it readable and print that result 123 times
print((favorite_snack + ' ') * 123)

### YOUR CODE ENDS HERE ###


# Use the corresponding variable you declared in Q2 that contains the price for your favorite snack and the * operator to calculate the final price for those 123 snacks and print the total cost.


### YOUR CODE STARTS HERE ###

#again applying the same rounding principle, variable cost x 123
print(round(coffee * 123, 2))

#keep it nice and neat, new line
print('\n')

### YOUR CODE ENDS HERE ###


# ---------------------------------------------------------------------- #
'''Q4. Formatting'''

# Replicate the code from the first part of Q3 but modified to separate each entry with a comma and a space. (Don't worry about having a trailing comma and space at the end). You might need to use some additional parens here.


### YOUR CODE STARTS HERE ###

#I didn't read far enough down, added a comma to the previous statement
print((favorite_snack + ', ') * 123)

#keep it nice and neat, new line
print('\n')

### YOUR CODE ENDS HERE ###


# ---------------------------------------------------------------------- #
'''Q5. BONUS''' # there are no test cases for this bonus

# Can you figure out how to get the same output as Q1 above with only 1 print statement? If so, can you do it all on one line?


### YOUR CODE STARTS HERE ###

#again I didn't read this far down, I think my solution to Q1 answers this question
#the '*' identifies the list i would like to print and the sep option causes a new line after every list item
print(*list,sep='\n')

### YOUR CODE ENDS HERE ###


# ---------------------------------------------------------------------- #
