#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys




### HELPER FUNCTIONS (IF NECESSARY) ###
def forwards_is_backwards(file):
  lines = file.readlines()  # read through each line

  for each in lines:  # iterate through each line item
    each = each.rstrip()  # remove spaces so only the string is left
    if each == each[::-1]:  # check if each is equal to 'reverse order' each
      print('True')
    else:
      print('False')

# I tried using the reversed() method, but it tells me that the attribute doesn't exist for a string


### MAIN FUNCTION ###
def main():
  file_name = sys.argv[1]
  with open(file_name) as f:
    forwards_is_backwards(f)
  
  


### DUNDER CHECK ###
if __name__ == "__main__":
  main()