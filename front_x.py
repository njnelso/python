#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys


### HELPER FUNCTIONS (IF NECESSARY) ###
def front_x(str_list):

    list1 = []  # create two new lists to write to
    list2 = []

    for elem in str_list:  # iterate through each element
        if elem.startswith(
                'X'):  # if each element starts with 'x', store in list1
            list1.append(elem)

        elif elem.startswith('x'):  # don't forget lower/uppercase
            list1.append(elem)

        else:  # all others store in list2
            list2.append(elem)

    list1.sort()  # sort the lists alphabetically
    list2.sort()  # ^

    return list1 + list2  # use the sorted function


### MAIN FUNCTION ###
def main():
    args = sys.argv[1:]
    print(front_x(args))


### DUNDER CHECK ###
if __name__ == "__main__":
    main()
