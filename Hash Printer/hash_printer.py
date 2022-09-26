#!/usr/bin/env python3

import sys
import hashlib

### HELPER FUNCTIONS (IF NECESSARY) ###
def hash_print(filename):   ### Note this only prints the first letter of each hash due to the challenge requirements

    byt = filename.read()

    md5 = hashlib.md5(byt).hexdigest()
    print(md5[0])
  
    sha1 = hashlib.sha1(byt).hexdigest()
    print(sha1[0])
  
    sha256 = hashlib.sha256(byt).hexdigest()
    print(sha256[0])
  
    sha512 = hashlib.sha512(byt).hexdigest()
    print(sha512[0])


def main():
    file = sys.argv[1]
    with open(file, "rb") as f:
        hash_print(f)


### DUNDER CHECK ###
if __name__ == "__main__":
    main()
