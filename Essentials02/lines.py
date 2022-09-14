#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys




### HELPER FUNCTIONS (IF NECESSARY) ###
def lines_lines_lines(file):

  lines = file.readlines()
  new = ''
  
  for each in lines:
    each = each.rstrip()
    new += each
    if ' ' in each:
      new += ''
    
  print(str(new))
  
### MAIN FUNCTION ###
def main():
  file_name = sys.argv[1]
  with open(file_name) as f:
    lines_lines_lines(f)
  
  


### DUNDER CHECK ###
if __name__ == "__main__":
  main()