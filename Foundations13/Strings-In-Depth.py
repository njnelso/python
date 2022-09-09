# ------------------------------------------------ #
'''first_letter'''

# Write a function called first_letter that takes in a string and returns the first character of that string.


### YOUR CODE STARTS HERE ###

def first_letter(str1):
  return str1[0] # return the first letter of string

print(first_letter('Apple'))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''last_three'''

# Write a function called last_three that takes in a string and returns the last three characters of the string. You can assume the string argument will always be at least three characters long.


### YOUR CODE STARTS HERE ###

def last_three(str1):
  return str1[-3:] # return the last three characters of string

print(last_three('Apple'))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''char_count'''

# Write a function called char_count that takes in a string of a single character as well as a larger string. char_count will return the amount of times the character is found within the larger string (upper or lowercase).



### YOUR CODE STARTS HERE ###

def char_count(sample_str, lg_str):

  count = 0 # set a counter
  
  for char in lg_str: # iterate over string
    if char.lower() == sample_str.lower(): # if char lower case is equal to the single character of sample string
      count += 1 # increase count by one
  return count

print(char_count('o', 'Kaboom!'))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''remove_vowels'''

# Write a function called remove_vowels that takes in a string and returns a string with all the vowels removed.



### YOUR CODE STARTS HERE ###

def remove_vowels(str1):

  result = '' # new variable to write string to
  
  for char in str1: # iterate over string
    if char.lower() != 'a' and char.lower() != 'e' and char.lower() != 'i' and char.lower() != 'o' and char.lower() != 'u': # if any vowels listed here (converted to lower case) are not char
      result += char # write all non-vowels to the result string
  return result

print(remove_vowels('What are you doing?'))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''hello_goodbye'''

# Write a function called hello_goodbye that takes in a string representing a name and an integer. If the integer is 1, return the string "Hello, <NAME>". If the integer is 2, return the string "Goodbye, <NAME>"



### YOUR CODE STARTS HERE ###

def hello_goodbye(str1, int1):

  if int1 == 1: # if the integer = 1 then it will start the return statement with "Hello"
    return "Hello, " + str1
  elif int1 == 2: # if the integer = 2 then it will start the return statement with "Goodbye"
    return "Goodbye, " + str1


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''spooky'''

# Write a function called spooky which takes in a string and returns a string, composed of the same characters, in alternating case (beginning with lowercase).



### YOUR CODE STARTS HERE ###

def spooky(str1):

    # local variables for counter and new string
    count = 0
    new_str = ''

    # iterate over string
    for char in str1:
      count += 1 # add to the count before the loop begins
        # if the number is even, make it uppercase and vice versa
      if count % 2 == 0:
          new_str += char.upper()
      else:
          new_str += char.lower()
          
    return new_str # return that new string


print(spooky('Pancake'))


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''initials'''

# Write a function called initials which takes in a string of a full-name, where each name is separated by a space. Return back a string representing the initials of a string passed to this function.



### YOUR CODE STARTS HERE ###

def initials(str1):

  # local variables
  result = ''
  first_letter = True

  # interate over string
  for char in str1:

    # if the first letter variable is equal to true, add that char to string 'result'
    if first_letter == True:
      result += char
      first_letter = False # reset the first letter variable since it's not the first letter anymore

    # once char encounters a space or ' ' it then resets the first_letter variable to True, indicating that the next letter will be a first letter in the for loop
    elif char == ' ':
      first_letter = True
      
  return result

# test
print(initials("Nicholas J Nelson"))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''mixup'''

# Write a function called mixup which takes in two strings. Return a string that is the concatenation of the two inputted strings (space-separated) except the first characters have been swapped.



### YOUR CODE STARTS HERE ###

def mixup(str1, str2):

  result1 = str2[0] # write the first index of the first string to the second string and vice versa
  result2 = str1[0]

  for char in str1[1::]: # loop through the rest of the characters, adding each character to the string
    result1 += char

  for char in str2[1::]: # same as above, but for second string
      result2 += char

      
  return result1 + ' ' + result2 # concatenate the strings with a space added

# test
print(mixup("Hello", "World"))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''mixup_extended'''

# When you are done with the mixup function above, go ahead and copy the functionality and name it mixup_extended. This new function will instead take in two strings AND a number. This number represents how many characters you should swap from the beginning of each string. You can assume that the number will always be valid, that is it will be less than the number of characters in the shorter string.



### YOUR CODE STARTS HERE ###

def mixup_extended(str1, str2, num1):

  x = num1 # i use x variable because math and set it equal to num1
  
  result1 = str2[0:x] # result from index[0] all the way to x variable or num1
  result2 = str1[0:x] # same as above but for the first string
  

  for char in str1[x::]: # loop through the rest of the characters and print to their respective strings
    result1 += char

  for char in str2[x::]: # same as above
      result2 += char

      
  return result1 + ' ' + result2 # concatenate with an added space

# test
print(mixup_extended("Hello", "World", 3))


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''not_bad'''

# Write a function called not_bad that takes in a string. Assume this string always has the substrings 'not' and 'bad'. Replace all of the words from the word 'not' until the word 'bad' with 'good'.


### YOUR CODE STARTS HERE ###

def not_bad(string):
  
  not_index = string.find('not') # find the index where 'not' starts
  bad_index = string.find('bad') # find the index where 'bad' starts
  
  string = string[0:not_index] + 'good' + string[bad_index + 3:] # starting from index[0] rewrite until first 'not', add 'good' string, and all the way up until the start of 'bad' + 3 to cover the rest of that word
  
  return string # return new string

# test
print(not_bad("this is not that bad"))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''h4ck3r_sp33k'''

# Write a function called h4ck3r_sp33k that takes in a string and returns the string in "h4cker sp33k" by replacing characters the following way:

  # 'A','a' => '4'
  # 'E','e' => '3'
  # 'L','l' => '1'
  # 'T','t' => '+'  

### YOUR CODE STARTS HERE ###

def h4ck3r_sp33k(string):

  new = '' # new string for h4ck3r_sp33k to write to
  
  for char in string: # iterate through every character
    if char == 'A' or char == 'a': # if 'Aa' rewrite 'new' as 4
      new += '4'
    elif char == 'E' or char == 'e': # if 'Ee' rewrite 'new' as 3
      new += '3'
    elif char == 'L' or char == 'l': # if 'Ll' rewrite 'new' as 1
      new += '1'
    elif char == 'T' or char == 't': # if 'Tt' rewrite 'new' as +
      new += '+'
    else: # else add all other characters
      new += char
  return new

# test
print(h4ck3r_sp33k("Apples too!"))


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''same_x_and_o'''

# Write a function called same_x_and_o that takes in a string and returns true if it has the same number of "x" and "o" characters in it.


### YOUR CODE STARTS HERE ###

def same_x_and_o(string):
  
  count_x = 0 # local variables, counter for each x and o
  count_o = 0

  for char in string: # iterate through every character
    if char == 'x': # if character is an 'x' increase one to x count
      count_x += 1
    elif char == 'o': # if character is an 'o' increase one to o count
      count_o += 1
  if count_x == count_o: # compare count x and o to see if equal
    return True
  else:
    return False

# test    
print(same_x_and_o('xoxoxo'))

### YOUR CODE ENDS HERE ###
