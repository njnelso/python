# Reading Files


&nbsp;
## open():

 - Built in method in python

 - Opens the file passed in as an argument, defaults to read mode

 - Accepts full path or relative path, but the filename must be given as a string

 - If the full path is not provided, the file to be opened must be in the same directory as the script

 - It is best practice to save this to a variable


&nbsp;
### Examples:

```python

# CREATE A TEST FILE TO OPEN

root@kali:~ touch test.txt

root@kali:~ echo 'first line' >> test.txt

root@kali:~ echo 'second line' >> test.txt

root@kali:~ echo 'third line' >> test.txt

root@kali:~ touch my_script.py

root@kali:~ chmod +x my_script.py

root@kali:~ vi my_script.py


# OPEN THE FILE IN YOUR SCRIPT AND SAVE AS A VARIABLE

#!/usr/bin/env python3

f = open('test.txt')

print(f)     # prints: <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>

```




&nbsp;
## .read():

 - A method used on an open file object

 - Defaults to read the entire file

 - If an int is given as an arg for read (ex: `f.read(2)`) the read method will pop the given number of bytes off of the open file and return them


&nbsp;
### Examples:

```python

# OPEN THE FILE

f = open('test.txt')


# READ WITH THE .read() METHOD

print(f.read())     # prints:    first line
                    #            second line
                    #            third line
                    #                            # note the newline at the end


# .read() WITH OPTIONAL ARGS

print(f.read(1))     # prints:   f

print(f.read(2))     # prints:   ir              # note that read moves to the next chars

print(f.read(2))     # prints:   st              # again, read moves to the next chars


```




&nbsp;
## .readlines():

 - Gives a **list** of all the lines of the file

 - Each line in the list is a **string**, and preserves newline chars (`\n`)

 - It is best to save this list to a variable

 - We can go through this list line by line with a traditional for loop!


&nbsp;
### Examples:

```python

# OPEN THE FILE

f = open('test.txt')


# CREATE THE LIST OF LINES

line_list = f.readlines()

print(line_list)    # prints:   ['first line\n', 'second line\n', 'third line\n']


# ITERATE THROUGH THE LINE LIST

for line in line_list:

    print(line)     # prints:     first line
                    #                           
                    #             second line
                    #
                    #             third line
                    #                            # note the newlines between each

    
```




&nbsp;
## .rstrip():

 - Provides a way to remove unwanted chars at the end of a string (*like newlines!*)

 - Will remove any occurances of the char passed to it from the trailing end of the string it is called on

 - If no arguments are provided, .rstrip() will remove the trailing white spaces (*including newlines!*) by default



&nbsp;
### Examples:

```python

# OPEN THE FILE

f = open('test.txt')


# CREATE THE LIST OF LINES

line_list = f.readlines()


# ITERATE THROUGH THE LINE LIST

for line in line_list:

    line = line.rstrip()

    print(line)     # prints:     first line      
                    #             second line
                    #             third line     # note the newlines are gone!


```




&nbsp;
## .split():

 - Splits a string into a list of strings based on the delimiter given

 - If no delimiter is given as an argument, .split will split on spaces by default

 - An excellent way to iterate word for word through a file is to use the .split() method with another for loop!


&nbsp;
### Examples:

```python

# OPEN THE FILE

f = open('test.txt')


# CREATE THE LIST OF LINES

line_list = f.readlines()


# ITERATE THROUGH THE LINE LIST

for line in line_list:


    line = line.rstrip()        # these could also be chained together: 
                             
    line = line.split()         # line = line.rstrip().split()


    print(line)     # prints:     ['first', 'line']      
                    #             ['second', 'line']
                    #             ['third', 'line']     


    for word in line:

        print(word)     # prints:     first
                        #             line
                        #             second
                        #             line
                        #             third
                        #             line
    

```





&nbsp;
## .join():

 - Joins a list of strings together with whatever delimiter is specified

 - The delimiter is specified in front of the `.`

 - The list that is to be joined together is passed as an arg to join



&nbsp;
### Examples:

```python

# OPEN THE FILE

f = open('test.txt')


# CREATE THE LIST OF LINES

line_list = f.readlines()


# ITERATE THROUGH THE LINE LIST

for line in line_list:

    
    # SPLIT THE LINE INTO INDIVIDUAL WORDS (ANOTHER LIST)

    line = line.rstrip().split()   
   

    # JOIN THE WORD LIST

    joined_list = ''.join(line)

    print(joined_list)   # prints:     firstline
                         #             secondline
                         #             thirdline    # note we joined with an empty string


```




&nbsp;
## .close():

 - We opened the file, so we should close it

 - Make sure to close the file **after** you have called your necessary functions

 - Both open() and .close() should be done in the main function



&nbsp;
### Examples:

```python

#!/usr/bin/env python3                # specify the interpreter


### IMPORT STATEMENTS ###
import sys                            # import the sys library


### HELPER FUNCTIONS ###
def print_words(f):                   # define our line printing function

    for line in f:                    # loop through every line in the file

        line = line.rstrip().split()  # remove the trailing newlines, and split into a word list

        for word in line:             # loop through each line

            print(word)               # print each word



### MAIN FUNCTION ###
def main():                           # define a main function

    file_to_open = sys.argv[1]        # get the file name from the cmd line

    opened_file = open(file)          # open the file

    print_words(opened_file)          # call our print words function with the open file

    opened_file.close()               # close the file when done


### DUNDER CHECK ###
if __name__ == '__main__':            # dunder check
    main()                # call the main function 
```
&nbsp;
## with:

  - When we open a file, we need to remember to close it

  - Programmers forget to close their files all the time

  - `with` will automatically close the file for use

  - **Note:** the code run with the open file must be indented beneith the `with` statement

&nbsp;
### Examples:

```python

#!/usr/bin/env python3                # specify the interpreter


### IMPORT STATEMENTS ###
import sys                            # import the sys library


### HELPER FUNCTIONS ###
def print_words(f):                   # define our line printing function

    for line in f:                    # loop through every line in the file

        line = line.rstrip().split()  # remove the trailing newlines, and split into a word list

        for word in line:             # loop through each line

            print(word)               # print each word



### MAIN FUNCTION ###
def main():                           # define a main function

    file_to_open = sys.argv[1]        # get the file name from the cmd line

    with open(file) as open_file:             # use with to open the file

      print_words(open_file)          # call our function with the open file
      
      # no need to close the file, "with" will automatically close it when we are done



### DUNDER CHECK ###
if __name__ == '__main__':            # dunder check
    main()                # call the main function 
```

