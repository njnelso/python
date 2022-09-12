#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys

### HELPER FUNCTIONS (IF NECESSARY) ###


def donuts(count):  # number of donuts
    if count < 10:  # if the count is greater than 10
        return 'Number of donuts: ' + str(count)  # don't forget to cast count to a string
    else:
        return 'Number of donuts: many'


### MAIN FUNCTION ###
def main():
    arg_1 = int(sys.argv[1])
    print(donuts(arg_1))


### DUNDER CHECK ###
if __name__ == "__main__":
    main()
