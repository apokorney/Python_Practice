# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'


def donuts(count):
  if count < 10:
    numberOfDonuts = count
  else:
    numberOfDonuts = "many"
  print ("Number of donuts: " + str(numberOfDonuts))

inpX = input("Enter the # of donuts: ")
donuts(inpX)

# what do you call it when inpX replaces count??
#  so you're "passing inpX into the donut function"
#   inpX (the global variable) is essentially replacing count (the local variable in the donut function/definition)


