# DON'T TOUCH THESE TWO LINES OF CODE
from io import StringIO
import sys




# ---------------------------------------------------------------------- #
'''FOR LOOPIN' Q1 summation'''

# Store the sum of the numbers between num_1 and num_2 (inclusive) in a variable named result. Note that the variables num_1, num_2, and result have already been defined for you in the summation function definition.

def summation(num_1:int, num_2:int)->int:
  result = 0

# ^^^ Do not worry about this code, we will learn about functions later, but this is is neccessary for your tests to run properly.
  
  ### YOUR CODE STARTS HERE ###
  for x in range(num_1, num_2 + 1):
    result += x
  
  
  
  
  ### YOUR CODE ENDS HERE ###
  return result

'''SUMMATION TESTING'''
# In order to test your implementation of summation uncomment the next three lines and edit the values in test_num_1 and test_num_2 as if they were going to be set to num_1 and num_2 above
test_num_1 = 1
test_num_2 = 3
print(summation(test_num_1, test_num_2))




# ---------------------------------------------------------------------- #
'''FOR LOOPIN' Q2: vowels'''

# Loop through the characters in the variable word. Store a string with all of the vowels in word in a variable called result. Note the variables word and result have already been defined for you in the vowels function definition.

def vowels(word:str)->int:
  result = ""

# ^^^ Do not worry about this code, we will learn about functions later, but this is is neccessary for your tests to run properly.
  
  ### YOUR CODE STARTS HERE ###
  
  for x in word.lower():
    if x == 'a':
      result += x
    elif x == 'e':
      result += x
    elif x == 'i':
      result += x
    elif x == 'o':
      result += x
    elif x == 'u':
      result += x
      
  ### YOUR CODE ENDS HERE ###
  return result

'''VOWELS TESTING'''
# In order to test your implementation of vowels uncomment the next two lines and edit the value in test_word as if it were going to be set to word above
test_word = "apple"
print(vowels(test_word))




# ---------------------------------------------------------------------- #
'''WHILE LOOPIN' Q1: times_divisable'''

# Store in a variable called result: the number of times you can divide num in half until it is less than or equal to 1. Note the variables num and result have already been defined for you in the times_divisable_by_two function definition.


def times_divisible_by_two(num:int)->int:
  result = 0

# ^^^ Do not worry about this code, we will learn about functions later, but this is is neccessary for your tests to run properly.
  
  ### YOUR CODE STARTS HERE ###
    #set result to 0 to start counting
  result = 0
    #while the variable is greater than 1
  while num > 1:
    #divide the variable in half
    num = num / 2
    #add 1 for every time it divides
    result += 1
  
  
  
  ### YOUR CODE ENDS HERE ###
  return result

'''TIMES_DIVISIBLE_BY_TWO TESTING'''
# In order to test your implementation of times_divisible_by_two uncomment the next two lines and edit the value in test_num as if it were going to be set to num above
test_num=10
print(times_divisible_by_two(test_num))




# ---------------------------------------------------------------------- #
'''WHILE LOOPIN' Q2: blast_off'''

# NOTE: For this challenge you will be using print statements instead of assigning to a variable.
  
# Count down from num_1 to num_2 by 1 inclusively. When you're done, print out "Blast Off!". Assume num_1 is greater than num_2. Note that the variables num_1 and num_2 have already been defined for you in the blast_off function definition.


def blast_off(num_1:int, num_2:int)->str:
  old_stdout = sys.stdout
  sys.stdout = mystdout = StringIO()
  try:
    pass

# ^^^ Do not worry about this code, we will learn about functions later, but this is is neccessary for your tests to run properly.
    
    ### YOUR CODE STARTS HERE ###
    while num_1 >= num_2:
      print(num_1)
      num_1 = num_1 - 1
    print("Blast Off!")
    

    ### YOUR CODE ENDS HERE ###
  except Exception as e:
    print(e)
  sys.stdout = old_stdout
  result = mystdout.getvalue()
  mystdout.close()
  return result

'''BLAST_OFF TESTING'''
# In order to test your implementation of blast_off uncomment the next three lines and edit the values in test_num_1 and test_num_2 as if they were going to be set to num_1 and num_2 above respectively
test_num_1 = 5
test_num_2 = 2
print(blast_off(test_num_1, test_num_2))




# ---------------------------------------------------------------------- #
'''WHILE LOOPIN' bonus'''

# NOTE: For this challenge you will be using print statements instead of assigning to a variable.

# Solve blast_off with a for loop and the range function. Note that the variables num_1 and num_2 have already been defined for you in the blast_off function definition.

def bonus(num_1:int, num_2:int)->str:
  old_stdout = sys.stdout
  sys.stdout = mystdout = StringIO()
  try:
    pass

# ^^^ Do not worry about this code, we will learn about functions later, but this is is neccessary for your tests to run properly.
    
    ### YOUR CODE STARTS HERE ###
    for num_1 in range(num_1, num_2 - 1, -1):
      print(num_1)
    print("Blast Off!")
    


    ### YOUR CODE ENDS HERE ###
  except Exception as e:
    print(e)
  sys.stdout = old_stdout
  result = mystdout.getvalue()
  mystdout.close()
  return result

'''BONUS TESTING'''
# In order to test your implementation of bonus uncomment the next three lines and edit the values in test_num_1 and test_num_2 as if they were going to be set to num_1 and num_2 above respectively
test_num_1 = 5
test_num_2 = 2
print(bonus(test_num_1, test_num_2))




# ---------------------------------------------------------------------- #
'''PUTTING IT ALL TOGETHER Q1: lower_upper_lower'''

# Write a control flow that uppercases any lowercase letters and lowercases any uppercase letters in word and stores the new string in a variable called result. Look into the documentation for str.upper(), str.lower(), str.isupper() and str.islower(). Note the variables word and result have already been defined for you in the lower_upper_lower function definition.


def lower_upper_lower(word:str)->str:
  result = ""

# ^^^ Do not worry about this code, we will learn about functions later, but this is is neccessary for your tests to run properly.
  
  ### YOUR CODE STARTS HERE ###
  for x in word:
    if x == x.upper():
      result += x.lower()
    elif x == x.lower():
      result += x.upper()
  


  ### YOUR CODE ENDS HERE ###
  return result

'''LOWER_UPPER_LOWER TESTING'''
# In order to test your implementation of lower_upper_lower uncomment the next two lines and edit the value stored in test_word as if it were going to be stored in word above
test_word = "oOGABOOGA"
print(lower_upper_lower(test_word))




# ---------------------------------------------------------------------- #
'''PUTTING IT ALL TOGETHER Q2: fizz_buzz_fllstack'''

# NOTE: For this challenge you will be using print statements instead of assigning to a variable.

# Write control flow that prints every number from 1 up to num inclusively. However, if the current number is evenly divisible by 3, print "Full" instead, if the current number is evenly divisible by 5, print "Stack" instead, and if the current number is evenly divisible by BOTH 3 and 5, print out "FullStack" instead. Note that the variable num has already been defined for you in the fizz_buzz_fullstack function definition.

def fizz_buzz_fullstack(num:int)->str:
  old_stdout = sys.stdout
  sys.stdout = mystdout = StringIO()
  try:
    pass

# ^^^ Do not worry about this code, we will learn about functions later, but this is is neccessary for your tests to run properly.
    
    ### YOUR CODE STARTS HERE ###
    for num in range(1, num + 1):
      if num%3 == 0 and num%5 == 0:
        print("FullStack")
      elif num%3 == 0:
        print("Full")
      elif num%5 == 0:
        print("Stack")
      else:
        print(num)




    ### YOUR CODE ENDS HERE ###
  except Exception as e:
    print(e)
  sys.stdout = old_stdout
  result = mystdout.getvalue()
  mystdout.close()
  return result

'''FIZZ_BUZZ_FULLSTACK TESTING'''
# In order to test your implementation of fizz_buzz_fullstack uncomment the next two lines and edit the value stored in test_num as if it were going to be stored in num above
test_num = 100
print(fizz_buzz_fullstack(test_num))




# ---------------------------------------------------------------------- #
'''PUTTING IT ALL TOGETHER Q3: variable_variable'''

# NOTE: For this challenge you will be using print statements instead of assigning to a variable.

# The parameter called variable can accept a str, an int or a float. You need to print out each character or digit on a new line. You will need to account for input that is not a string. Note that the variable variable has already been defined for you in the variable_variable function definition.

def variable_variable(variable) -> str:
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    try:
      pass

# ^^^ Do not worry about this code, we will learn about functions later, but this is is neccessary for your tests to run properly.
      
      ### YOUR CODE STARTS HERE ###
      for x in str(variable):
        print(x)
  



      ### YOUR CODE ENDS HERE ###
    except Exception as e:
      print(e)
    sys.stdout = old_stdout
    result = mystdout.getvalue()
    mystdout.close()
    return result

'''VARIABLE_VARIABLE TESTING'''
# In order to test your implementation of variable_variable above uncomment the next two lines and edit test_variable as if it were going to be stored in variable above
test_variable = 3.14159
print(variable_variable(test_variable))




# ---------------------------------------------------------------------- #
