import sys

# Create lists with the following properties, choose names like ex1 1, 2, 3 for them:
# numbers from 10 to 20(included) that are odd
if sys.argv[1] == "1":
    odd = range(10, 20, 1)
    for n in odd:
        if (n % 2 != 0):
            print(n)
            
            
#numbers from 100 to 0(included) that can be divided by 10 (use %, the
# modulus operator and list comprehension)
if sys.argv[1] == "2":
    numbers = range(0, 100, 1)
    for n in reversed(numbers):
        if(n % 10 == 0):
            print(n)
            
# numbers from 15 to 1 (included) that can be divided by 3
if sys.argv[1] == "3":
    numbers = range(1, 15, 1)
    for n in reversed(numbers):
        if(n %3 == 0):
            print(n)
            
#  string like “x”, “xx”, “xxx” repeated 10 times. Use the fact that, in
# Python, a string s multiplied by an integer n results in s repeated n
# times.
if sys.argv[1] == "4":
    numbers = range(1, 11, 1)
    for n in numbers:
        print(n * "x")
        
# the string ”stringX” repeated 5 times, where X goes from 5 to 0(excluded).
# Use the builtin function str() to convert numbers to strings and the fact
# that strings can be concatenated using the ”+” operator
if sys.argv[1] == "5":
    numbers = range(0, 6, 1)
    for n in reversed(numbers):
        print("string"+str(n))
        
# a list with the items ”1”, 1, 1.0, “one”
if sys.argv[1] == "6":
    numbers = ["1", 1, 1.0, "one"]
    for n in numbers:
        print(n)
        
# all the numbers from 0 to 99 that contain the digit ”5”. You may use
# the method find() that all strings possess to look for a substring. If it is
# found, the start index is returned, otherwise -1.
if sys.argv[1] == "7":
    numbers = range(0, 100, 1)
    for n in numbers:
        num = str(n)
        # if("5" in num):
        num.find("5") != -1 and print(num)