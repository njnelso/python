#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys

### HELPER FUNCTIONS (IF NECESSARY) ###


def match_ends(str_list):

    counter = 0  # set a counter variable

    for elem in str_list:  # iterate through str_list
        if len(elem) >= 2 and elem[0] == elem[-1]:  # if the length of each element is 2 or greater and element index 0 and 1 match
            counter += 1  # add to counter
    return counter  # return the count


### MAIN FUNCTION ###
def main():
    args = sys.argv[1:]
    print(match_ends(args))


### DUNDER CHECK ###
if __name__ == "__main__":
    main()
