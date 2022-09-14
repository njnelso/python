#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys




### HELPER FUNCTIONS (IF NECESSARY) ###
def is_even(file):
  
  lines = file.readlines()  # read through each line
 
  for each in lines:  # iterate through each line item
    if int(each) % 2 == 0:  # if the number is divisible by 2 
      print(each.rstrip() + ' True')  # print True for even
    else:
      print(each.rstrip() + ' False')  # print False if it's not


### MAIN FUNCTION ###
def main():
  file_name = sys.argv[1]
  with open(file_name) as open_file:
    is_even(open_file)
  


### DUNDER CHECK ###
if __name__ == "__main__":
  main()