#!/usr/bin/python

# a selection of simple Python code to give you a taste of the language ...
#
# Just a few notes about Python:
# Python has a very efficient built-in memory manager.
# Python does not need variable types declared, it is smart enough to figure that out!
# Python uses whitespaces to group statements, this avoids the begin/ends and {}
#   of other languages.  Let's face it, you use whitespaces anyway in these 
#   languages to make the code more readable!  In other words, Python forces you 
#   to make code more readable.  You get used to the indentations naturally.
#   Use the number of spaces you like, the de facto standard is four spaces.
#   Important caveat: 
#     keep the spacing uniform for the group of statements
#     that belong together, and don't mix tabs and spaces.  Avoid tabs!
#
# I used  Python-2.3.4.exe  (the Windows installer package for Python23) 
# from http://www.python.org/2.3.4/ 
# code tested with Python23    vegaseat   16jan2005
 
 
print "Simple math like 12345679*63 = ", 12345679*63
 
# print just an empty line
print
 
# display numbers 0 to 9
# the indentation before print makes it part of the loop
for number in range(10):
    print number
 
# print also adds a newline, use a comma to prevent the newline
for number in range(10):
    print number,
 
print
 
# import the math module for the sqrt() function
import math
 
# a little more complex this time
# \n is the newline character, % starts the format specifier
# Python does have its roots in the C language
# notice how we use the sqrt() function from the math module
# CYA: more specifically, sqrt() is a function in module math
print "\nSquare root of integers 0 to 9 formatted as a float with 4 decimals:"
for value in range(10):
    squareRoot = math.sqrt(value)
    print "sqrt(%d) = %.4f" % (value, squareRoot)
 
# now it gets a bit more hairy
print "\nDisplay integers 0 to 15 formatted to use 6 spaces ..."
print "(plain, zero-padded, hex and octal)"
print "   %s      %s      %s     %s" % ('%6d', '%06d', '%6x', '%6o')
for value in range(16):
    print "%6d    %06d   %6x  %6o" % (value, value, value, value)
 
print
 
print "\nA not so typical for loop:"
for food in "spam", "eggs", "cumquats":
    print "I love", food
 
print
 
# a short intro to string slicing
# a little cryptic at first blush, but very powerful
# [begin : < end : step]  end is exclusive, step is optional
# defaults are index begin = 0, index end = length, step = 1
animal = "hippopotamus"
print "this is the string    = ", animal
print "length of string      = ", len(animal)
print "exclude first 3 char  = ", animal[3: ]
print "exclude last 4 char   = ", animal[:-4]
print "reverse the string    = ", animal[::-1]
 
# define/create a function
# the indented lines are part of the function
def convertFahrenheit2Celsius(fahrenheit):
    celcius = 0.555 * (fahrenheit - 32)
    return celcius
 
print
 
# and use the function
# (make sure you define/create the function before you call it)
print "A Fahrenheit to Celcius table:"
# range is from -40 to < 220 in steps of 10
for tf in range(-40, 220, 10):
    print "%5.1fF = %5.1fC" % ( tf, convertFahrenheit2Celsius(tf) )
 
print
 
print "A limited set:"
# another variation of the for loop
for tf in -40,0,32,98.6:
    print "%5.1fF = %5.1fC" % ( tf, convertFahrenheit2Celsius(tf) )
 
print
 
# test boolean results
print "Is 3 > 5? Result =", 3 > 5  # result = False
print "Is 3 < 5? Result =", 3 < 5  # result = True
 
# optional wait for keypress
raw_input('Press Enter...')
