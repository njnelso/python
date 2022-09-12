#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys

### HELPER FUNCTIONS (IF NECESSARY) ###

### MAIN FUNCTION ###
def main():
  arg_1 = sys.argv[1] # is not 5 ... it is '5'
  arg_2 = sys.argv[2]

  print(arg_1)
  print(type(arg_1))
  print(arg_1 + arg_2)
  
  


### DUNDER CHECK ###
if __name__ == "__main__":
  main()