# Essentials 02: Reading Files
Each challenge will need the script to have a specific name for testing. The names are as follows:

  1. Is Even - `even.py`
  2. Forwards is Backwards - `forwards.py`
  3. Lines Lines Lines - `lines.py`

** Do not touch the `test_files` folder**

&nbsp;

## 1. Is Even

* `touch` a new script in the **replit shell** called `even.py`

* Give your script the proper permissions with `chmod +x even.py`

* Under the **Files** Tab on the left, click on your newly created script to edit it

* Copy/Paste the boilerplate code from `BOILERPLATE.md`

* In the **Helper Functions** section of the boilerplate, solve this challenge:

```python
'''is even'''
# Write a function called is_even with a parameter called file, which represents an open file containing a single number on each line. Your is_even function should go through the open file line by line, determine if the number on that line is even or not and print: '<number> <True/False>' depending on if the number is even or not. 

cat path/to/test_file # Note: this is the result of cat command
'''
0
11
2
33
4
55
6
77
8
99
100
'''

./even.py path/to/test_file # This is the result of code execution
'''
0 True
11 False
2 True
33 False
4 True
55 False
6 True
77 False
8 True
99 False
100 True
'''
```

* in the **Main Function** section of the boilerplate, create a variable called `file_name` and set it to the first command line argument (`sys.argv[1]`)

* using the `open()` method, open the file and save it as a variable called `open_file`

* Call your `is_even` helper function with `open_file` as an argument. Since your is_even function is handling the printing, you do not need to print out the function call

* remember to be a responsible programmer and close the `open_file` variable after then function call using the `.close()` method on it

* Run the test cases. If you did everything correctly, you should now be passing the **even** test cases

&nbsp;


## 2. Forwards is Backwards

* `touch` a new script in the **replit shell** called `forwards.py`

* Give your script the proper permissions with `chmod +x forwards.py`

* Under the **Files** Tab on the left, click on your newly created script to edit it

* Copy/Paste the boilerplate code from `BOILERPLATE.md`

* In the **Helper Functions** section of the boilerplate, solve this challenge:

```python
'''forwards is backwards'''
# Write a function called forwards_is_backwards with a parameter called file, which represents an open file containing a single word (str) on each line. Your forwards_is_backwards function should go through the open file line by line, determine if the word on that line is a palindrome or not, and print: '<True/False>' depending on if the string is a palindrome or not.

cat path/to/test_file # Note cat
'''
radar
creepy
Radar
'''

./forwards path/to/test_file # Note code execution
'''
True
False
False
'''
```

* in the **Main Function** section of the boilerplate, create a variable called `file_name` and set it to the first command line argument (`sys.argv[1]`)

* using with, open your file and use the as keyword to save the open file as the variable f: `with open(file_name) as f:`. Don't forget to indent following code you want to run with the open file 

* Call your `forward_is_backwards` helper function with `f` as an argument. Since your forwards_is_backwards function is handling the printing, you do not need to print out the function call

* Run the test cases. If you did everything correctly, you should now be passing the **forwards** test cases

&nbsp;


## 3. Lines Lines Lines

* `touch` a new script in the **replit shell** called `lines.py`

* Give your script the proper permissions with `chmod +x lines.py`

* Under the **Files** Tab on the left, click on your newly created script to edit it

* Copy/Paste the boilerplate code from `BOILERPLATE.md`

* In the **Helper Functions** section of the boilerplate, solve this challenge:

```python
'''lines lines lines'''
# Write a function called lines_lines_lines with a parameter called file, which represents an open file containing a single string of varying lengths on each line (including empty strings). Your lines_lines_lines function should go through the open file line by line, replace the newline characters with spaces, so the output is a single string with all of the lines combined into one. There should be exactly 1 space between each word in the output string.

cat path/to/test_file
'''
this is one line

this
is also
just one
l 
'''

./lines.py path/to/test_file
'''
this is one line this is also just one line maybe we should try something different ha ha haha
'''

```

* in the **Main Function** section of the boilerplate, create a variable called `file_name` and set it to the first command line argument (`sys.argv[1]`)

* using `with`, open your file and use the `as` keyword to save the open file as the variable `f`: (`with open(file_name) as f:`). Don't forget to indent following code you want to run with the open file 

* Call your `lines_lines_lines` helper function with `f` as an argument. Don't forget to print out your function call!

* Run the test cases. If you did everything correctly, you should now be passing the **lines** test cases

