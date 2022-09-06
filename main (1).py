'''sum_of_two_nums'''

# Define a function named sum_of_two_nums, which takes in two numbers and returns the sum of those numbers.


### YOUR CODE STARTS HERE ###
# define the function
def sum_of_two_nums(num1, num2):
  # return the sum of the two nums
  return num1 + num2

# IF YOU WANT TO TEST SOME OUTPUT FOR YOURSELF:
# print(sum_of_two_nums(1, 2))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''greater_than_ten'''

# Define a function named greater_than_ten, which takes in an integer and returns True if the number is greater than 10 and False if the number is less than 10.


### YOUR CODE STARTS HERE ###

def greater_than_ten(int1):
  # if variable is greater than 10
  if int1 > 10:
    return True
  # all else return False
  else:
    return False

# test it out
# print(greater_than_ten(9))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''odd_or_even'''

# Define a function named odd_or_even which takes in an integer and returns 'odd' if the number is odd, and 'even' if the number is even.


### YOUR CODE STARTS HERE ###

def odd_or_even(int2):
  #if divisible by 2
  if int2 % 2 == 0:
    return 'even'
  else:
    return 'odd'


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''how_many_legs'''

# Define a function named how_many_legs, which takes three parameters, num_cows, num_chickens, and num_spiders and returns the total number of legs.


### YOUR CODE STARTS HERE ###

def how_many_legs(num_cows, num_chickens, num_spiders):
  # define the number of legs of every animal and multiply each num_ variable by the number of legs
  cows = 4 * num_cows
  chickens = 2 * num_chickens
  spiders = 8 * num_spiders
  return cows + chickens + spiders
  

#test it out

print(how_many_legs(1, 1, 1))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''multiple_of_3'''

# Define a function named multiple_of_3, which takes one argument, an integer, and returns True if the integer is a multiple of 3 and False otherwise.


### YOUR CODE STARTS HERE ###

def multiple_of_3(int3):
  #if a multiple of 3, zero remainder
  if int3 % 3 == 0:
    return True
  else:
    return False

#test it out

print(multiple_of_3(6))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''area_of_triangle'''

# Define a function named area_of_triangle, which takes two arguments as integers, base, and height and returns the area of a triangle of those dimensions. Note: The formula for area of a triangle is base times height divided by 2


### YOUR CODE STARTS HERE ###

def area_of_triangle(base, height):
  return base * height / 2

# test it out
print(area_of_triangle(5, 4))


### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''concatenator'''

# Define a function named concatenator, which takes in two strings and returns them concatenated together.


### YOUR CODE STARTS HERE ###

def concatenator(str1, str2):
  return str1 + str2

#test it out

print(concatenator('base', 'ball'))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''less_than_ten'''

# Define a function named less_than_ten, which takes in a string and returns True if the length of the string is less than 10 and False otherwise.


### YOUR CODE STARTS HERE ###

def less_than_ten(str3):

  #local variables
  counter = 0

  #for loop counting characters
  for char in str3:
    counter += 1

  #if counter is greater than 10
  if counter < 10:
    return True
  else:
    return False

# test it out

print(less_than_ten('Oogabooga'))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''even_or_odd'''

# Define a function named even_or_odd which takes in a string and returns 'odd' if the length of the string is odd, and 'even' if the length of the string is even.


### YOUR CODE STARTS HERE ###

def even_or_odd(str4):

  #local variables
  count = 0

  #for loop counting characters
  for char in str4:
    count += 1

  #if divisible by two then it's even
  if count % 2 == 0:
    return 'even'
  else:
    return 'odd'

#test it out
    
print(even_or_odd('baseball'))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''space_count'''

# Define a function named space_count, which takes a string as an argument, and returns the number of spaces in the string. Note: If there are no spaces, it should return 0.


### YOUR CODE STARTS HERE ###

def space_count(str5):

  #local variables
  count = 0

  #counting spaces using an empty string
  for spaces in str5:
    if spaces == ' ':
      count += 1
  return count

# test it out

print(space_count('noSpaces'))
  
### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''how_many_vowels'''

# Define a function named how_many_vowels, which takes in a strings and returns the total number of vowels of the string.


### YOUR CODE STARTS HERE ###

def how_many_vowels(str6):

  #local variables
  vowels = 0

  #for loop that lower cases the string and checks for vowels
  for char in str6.lower():
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
      vowels += 1
    else: #if no vowels detected, add zero
      vowels += 0
  return vowels

# test it out

print(how_many_vowels('Plan'))
  
### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''three_es'''

# Define a function named three_es, which takes in one argument, a string, and returns True if the string contains at least 3 e's and False otherwise. Don't forget to account for capitalization.


### YOUR CODE STARTS HERE ###

def three_es(str7):

  #local variable
  count = 0

  #for loop that lower cases the string and counts the number of Es
  for char in str7.lower():
    if char == 'e':
      count += 1

  #if there are more than 3 Es
  if count >= 3:
    return True
  else:
    return False

# test it out

print(three_es('Melee'))
    
### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''
1. LOG GENERATOR - THIS IS A BONUS QUESTION
  Write a Function called log_generator that takes 5 arguments:
    a string date in the form 'mm-dd-yyyy' (exactly 10 characters)
    a string ip_addr in the form 'xxx.xxx.xxx.xxx' (minimum 7 characters, maximum 15 characters)
    a string proto (either 'TCP' or 'UDP')
    an int src_port (in the range of 0-65535)
    an int dst_port (in the range of 0-65535)
  
  Your function should test for proper date length:
    if the length of the given date is not exactly 10 charaters (dashes included), return "Error: Incorrect date format given. Date must be formatted as mm-dd-yyyy"
  
  Your function should test for proper IP address length:
    if the length of the given ip address is less than 7 or greater than 15, your function should return "Error: Impossible IP address length given"
  
  Your function should test for proper protocols:
    if a string other than "TCP"or "UDP" is given (capitalization counts), your function should return "Error: Incorrect protocol given. Must be TCP or UDP"
  
  Your function should test for proper src_port ranges:
    if an int smaller than 0 or larger than 65535 is given for either the src or dst port, your function should return "Error: Incorrect port number given for src_port: <src_port>"

  Your function should test for proper dst_port ranges:
    if an int smaller than 0 or larger than 65535 is given for either the src or dst port, your function should return "Error: Incorrect port number given for dst_port: <dst_port>"

  If everything is formatted correctly, your function should create a log entry and return it in the format:

"<date> | <ip_addr> | <proto> | <src_port> | <dst_port>"'''


### YOUR CODE STARTS HERE ###

def log_generator(date, ip_addr, proto, src_port, dst_port):

  #local variables
  date_count = 0
  ip_count = 0

  #date format
  for char in date:
    date_count += 1
  if date_count != 10:
    return "Error: Incorrect date format given. Date must be formatted as mm-dd-yyyy"

  #IP address format
  for char in ip_addr:
    ip_count += 1
  if ip_count < 7 or ip_count > 15:
    return "Error: Impossible IP address length given"

  #protocol format
  if proto == "TCP":
    proto = "TCP"
  elif proto == "UDP":
    proto = "UDP"
  else:
    return "Error: Incorrect protocol given. Must be TCP or UDP"

  #source port format
  if src_port < 0:
    return "Error: Incorrect port number given for src_port: " + str(src_port)
  elif src_port > 65535:
    return "Error: Incorrect port number given for src_port: " + str(src_port)
    
  #destination port format, another way of writing it out
  if dst_port < 0 or dst_port > 65535:
    return "Error: Incorrect port number given for dst_port: " + str(dst_port)

  return date + " | " + ip_addr + " | " + proto + " | " + str(src_port) + " | " + str(dst_port)

# test it out
  
print(log_generator("09-06-2022", "10.10.10.10", "UDP", 1, 1))

### YOUR CODE ENDS HERE ###


# ------------------------------------------------ #
'''
2. ASCII BATTLE OF THE B AND P CHARACTER CLANS
  The Bs and the Ps are two warring ASCII Character Clans and they cannot decide who is the better ASCII Character Clan. The B's think they are better because they have an even number of humps, while the Ps think their odd number of humps are more artistically pleasing.

  Write a function Bs_or_Ps that takes a string battle as an argument, that only contains the characters "B" and "P" (capitalization counts) in varying amounts.

  If there are more Bs than Ps, return "The B Character Clan is victorious!"
  If there are more Ps than Bs, return "The P Character Clan is victorious!"
  In the event of a tie:
    If there are an even amount of Bs and Ps, then the Bs ultimately win and return "The B Character Clan is victorious!"
    If there are an odd amount of Bs and Ps, then the Ps ultimately win and return "The P Character Clan is victorious!"
  BONUS: Only use one return statement in the entire function'''


### YOUR CODE STARTS HERE ###

def Bs_or_Ps(string):

  #local variables
  B_count = 0
  P_count = 0
  
  winner = ''

  # counting Bs and Ps in the string
  for char in string:
    if char == "B":
      B_count += 1
    elif char == "P":
      P_count += 1

  #which one has more Bs and Ps? if they tie, how many of each? is it even or odd?
  if B_count > P_count:
    winner = 'B'
  elif P_count > B_count:
    winner = 'P'
  elif B_count == P_count and B_count % 2 == 0:
    winner = 'B'
  else:
    winner = 'P'

  # one return statement
  return "The " + winner + " Character Clan is victorious!"

#test it out
  
print(Bs_or_Ps("PBPBBBPP"))


### YOUR CODE ENDS HERE ###