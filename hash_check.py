#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import sys
import hashlib
import os

### This function will read through files in a directory, read each file as bytes, and then compare it
### to a hash that represents some type of malware

### HELPER FUNCTIONS (IF NECESSARY) ###
def hash_check(filename):

    byt = filename.read()
    HASH = '6859e1d10d08c1ea91f6e53ba6d601149b08d4efab8f8c2d586f6858ae1773a7'

    if hashlib.sha256(byt).hexdigest() == HASH:
        return (1)


def main():
    for filename in os.listdir('/home/kali/Burn/bin'):
        f = os.path.join('/home/kali/Burn/bin', filename)
        if os.path.isfile(f):
            with open(f, "rb") as f:
                if hash_check(f) == 1:
                    print("Here: " + filename)


### DUNDER CHECK ###
if __name__ == "__main__":
  main()