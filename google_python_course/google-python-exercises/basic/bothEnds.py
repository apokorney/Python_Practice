# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.


def both_ends(s):
    if len(s) > 2:
        print s[0:2] + s[-2:]
    else:
        print "do nothing"

inpZ = raw_input("Enter a string to slice up: ")
both_ends(inpZ)