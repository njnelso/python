#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys


### HELPER FUNCTIONS (IF NECESSARY) ###
def both_ends(s):

  new = ''            # new string variable to write to
  new += s[0:1 + 1]   # add the 0 index of the string through the 1st index
  new += s[-2:]       # add the 2nd to last index followed by the last of the string
  
  if len(s) < 2:      # if length is less than two, return an empty string
    return ''
  else:               # otherwise return the new variable
    return new 

### MAIN FUNCTION ###
def main():
  arg_1 = sys.argv[1]
  print(both_ends(arg_1))


### DUNDER CHECK ###
if __name__ == "__main__":
    main()
