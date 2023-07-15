# This program tests whether a number is a palindrome
number = 155512 # test case
strNum = str(number)
if strNum[::-1] == strNum:
    print ("True")
else:
    print ("False")